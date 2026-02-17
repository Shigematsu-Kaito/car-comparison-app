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
    ユーザーの検討リストを取得
    """
    try:
        response = db.table("watchlist").select("*").eq("user_id", user_id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"取得エラー: {str(e)}")


@router.post("/watchlist/{user_id}", response_model=WatchListItem)
async def add_to_watchlist(
    user_id: str,
    item: WatchListItemCreate,
    db: Client = Depends(get_db)
):
    """
    検討リストに追加
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
        raise HTTPException(status_code=500, detail=f"追加エラー: {str(e)}")


@router.put("/watchlist/{item_id}", response_model=WatchListItem)
async def update_watchlist_item(
    item_id: str,
    item: WatchListItemUpdate,
    db: Client = Depends(get_db)
):
    """
    検討リストアイテムを更新
    """
    try:
        data = {}
        if item.notes is not None:
            data["notes"] = item.notes
        
        response = db.table("watchlist").update(data).eq("id", item_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="アイテムが見つかりません")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"更新エラー: {str(e)}")


@router.delete("/watchlist/{item_id}")
async def delete_watchlist_item(
    item_id: str,
    db: Client = Depends(get_db)
):
    """
    検討リストから削除
    """
    try:
        response = db.table("watchlist").delete().eq("id", item_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="アイテムが見つかりません")
        return {"message": "削除しました"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"削除エラー: {str(e)}")
