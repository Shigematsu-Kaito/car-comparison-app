from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.car import WatchListItem, WatchListItemCreate, WatchListItemUpdate
from app.core.database import get_db
from supabase import Client

router = APIRouter()


@router.get("/watchlist/{user_id}", response_model=List[WatchListItem])
async def get_watchlist(
    user_id: str,
    db: Client = Depends(get_db)
):
    """
    Get user's watch list
    """
    try:
        response = db.table("watchlist").select("*").eq("user_id", user_id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fetch error: {str(e)}")


@router.post("/watchlist/{user_id}", response_model=WatchListItem)
async def add_to_watchlist(
    user_id: str,
    item: WatchListItemCreate,
    db: Client = Depends(get_db)
):
    """
    Add to watch list
    """
    try:
        data = {
            "user_id": user_id,
            "car_id": item.car_id,
            "notes": item.notes
        }
        response = db.table("watchlist").insert(data).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Add error: {str(e)}")


@router.put("/watchlist/{item_id}", response_model=WatchListItem)
async def update_watchlist_item(
    item_id: str,
    item: WatchListItemUpdate,
    db: Client = Depends(get_db)
):
    """
    Update watch list item
    """
    try:
        data = {}
        if item.notes is not None:
            data["notes"] = item.notes
        
        response = db.table("watchlist").update(data).eq("id", item_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Item not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Update error: {str(e)}")


@router.delete("/watchlist/{item_id}")
async def delete_watchlist_item(
    item_id: str,
    db: Client = Depends(get_db)
):
    """
    Delete from watch list
    """
    try:
        response = db.table("watchlist").delete().eq("id", item_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"message": "Deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Delete error: {str(e)}")
