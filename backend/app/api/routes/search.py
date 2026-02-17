from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.car import Car, CarSearchQuery
from app.services.scraping_service import ScrapingService
from app.services.car_service import CarService
from app.core.database import get_db
from supabase import Client

router = APIRouter()


@router.post("/search", response_model=List[Car])
async def search_cars(
    query: CarSearchQuery,
    db: Client = Depends(get_db)
):
    """
    Search used cars
    
    - Execute scraping to get latest data
    - Save to database
    - Filter based on search criteria
    """
    try:
        # Get information from scraping service
        scraping_service = ScrapingService()
        cars = await scraping_service.scrape_all(query)
        
        # Save to database
        car_service = CarService(db)
        saved_cars = await car_service.save_cars(cars)
        
        return saved_cars
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search error: {str(e)}")


@router.get("/cars", response_model=List[Car])
async def get_cars(
    skip: int = 0,
    limit: int = 100,
    db: Client = Depends(get_db)
):
    """
    Get saved used car information
    """
    try:
        car_service = CarService(db)
        cars = await car_service.get_cars(skip=skip, limit=limit)
        return cars
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fetch error: {str(e)}")


@router.get("/cars/{car_id}", response_model=Car)
async def get_car(
    car_id: str,
    db: Client = Depends(get_db)
):
    """
    Get specific used car information
    """
    try:
        car_service = CarService(db)
        car = await car_service.get_car(car_id)
        if not car:
            raise HTTPException(status_code=404, detail="Car not found")
        return car
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"取得エラー: {str(e)}")
