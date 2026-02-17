from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class CarBase(BaseModel):
    """中古車情報の基本モデル"""
    source: str = Field(..., description="情報源（carsensor/goonet/gulliver）")
    make: str = Field(..., description="メーカー")
    model: str = Field(..., description="車種")
    year: int = Field(..., description="年式")
    price: int = Field(..., description="価格（円）")
    mileage: int = Field(..., description="走行距離（km）")
    color: Optional[str] = Field(None, description="色")
    fuel_type: Optional[str] = Field(None, description="燃料タイプ")
    transmission: Optional[str] = Field(None, description="トランスミッション")
    location: Optional[str] = Field(None, description="所在地")
    url: str = Field(..., description="詳細ページURL")
    image_url: Optional[str] = Field(None, description="画像URL")
    description: Optional[str] = Field(None, description="説明")


class Car(CarBase):
    """中古車情報モデル（DB保存用）"""
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CarSearchQuery(BaseModel):
    """車検索クエリ"""
    make: Optional[str] = None
    model: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    price_min: Optional[int] = None
    price_max: Optional[int] = None
    mileage_max: Optional[int] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    sources: Optional[List[str]] = Field(default=None, description="検索するソース")


class WatchListItem(BaseModel):
    """検討リストアイテム"""
    id: Optional[str] = None
    user_id: str = Field(..., description="ユーザーID")
    car_id: str = Field(..., description="車ID")
    notes: Optional[str] = Field(None, description="メモ")
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class WatchListItemCreate(BaseModel):
    """検討リストアイテム作成"""
    car_id: str
    notes: Optional[str] = None


class WatchListItemUpdate(BaseModel):
    """検討リストアイテム更新"""
    notes: Optional[str] = None
