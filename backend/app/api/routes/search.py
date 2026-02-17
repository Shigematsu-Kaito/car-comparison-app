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
    中古車を検索
    
    - スクレイピングを実行して最新データを取得
    - データベースに保存
    - 検索条件に基づいてフィルタリング
    """
    try:
        # スクレイピングサービスで情報を取得
        scraping_service = ScrapingService()
        cars = await scraping_service.scrape_all(query)
        
        # データベースに保存
        car_service = CarService(db)
        saved_cars = await car_service.save_cars(cars)
        
        return saved_cars
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"検索エラー: {str(e)}")


@router.get("/cars", response_model=List[Car])
async def get_cars(
    skip: int = 0,
    limit: int = 100,
    db: Client = Depends(get_db)
):
    """
    保存済みの中古車情報を取得
    """
    try:
        car_service = CarService(db)
        cars = await car_service.get_cars(skip=skip, limit=limit)
        return cars
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"取得エラー: {str(e)}")


@router.get("/cars/{car_id}", response_model=Car)
async def get_car(
    car_id: str,
    db: Client = Depends(get_db)
):
    """
    特定の中古車情報を取得
    """
    try:
        car_service = CarService(db)
        car = await car_service.get_car(car_id)
        if not car:
            raise HTTPException(status_code=404, detail="車が見つかりません")
        return car
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"取得エラー: {str(e)}")
