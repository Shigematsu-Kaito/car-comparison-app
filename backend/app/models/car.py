from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class CarBase(BaseModel):
    """Base model for used car information"""
    source: str = Field(..., description="Source (carsensor/goonet/gulliver)")
    make: str = Field(..., description="Manufacturer")
    model: str = Field(..., description="Model")
    year: int = Field(..., description="Year")
    price: int = Field(..., description="Price (JPY)")
    mileage: int = Field(..., description="Mileage (km)")
    color: Optional[str] = Field(None, description="Color")
    fuel_type: Optional[str] = Field(None, description="Fuel type")
    transmission: Optional[str] = Field(None, description="Transmission")
    location: Optional[str] = Field(None, description="Location")
    url: str = Field(..., description="Detail page URL")
    image_url: Optional[str] = Field(None, description="Image URL")
    description: Optional[str] = Field(None, description="Description")


class Car(CarBase):
    """Used car information model (for DB storage)"""
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CarSearchQuery(BaseModel):
    """Car search query"""
    make: Optional[str] = None
    model: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    price_min: Optional[int] = None
    price_max: Optional[int] = None
    mileage_max: Optional[int] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    sources: Optional[List[str]] = Field(default=None, description="Sources to search")


class WatchListItem(BaseModel):
    """Watch list item"""
    id: Optional[str] = None
    user_id: str = Field(..., description="User ID")
    car_id: str = Field(..., description="Car ID")
    notes: Optional[str] = Field(None, description="Notes")
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class WatchListItemCreate(BaseModel):
    """Create watch list item"""
    car_id: str
    notes: Optional[str] = None


class WatchListItemUpdate(BaseModel):
    """Update watch list item"""
    notes: Optional[str] = None
