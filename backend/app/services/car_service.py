from typing import List, Optional
from supabase import Client
from app.models.car import Car, CarBase


class CarService:
    """車情報に関するビジネスロジック"""
    
    def __init__(self, db: Client):
        self.db = db
        self.table_name = "cars"
    
    async def get_cars(
        self,
        skip: int = 0,
        limit: int = 100
    ) -> List[Car]:
        """
        車情報のリストを取得
        
        Args:
            skip: スキップする件数
            limit: 取得する最大件数
        
        Returns:
            車情報のリスト
        """
        try:
            response = self.db.table(self.table_name)\
                .select("*")\
                .range(skip, skip + limit - 1)\
                .execute()
            return [Car(**item) for item in response.data]
        except Exception as e:
            print(f"Error fetching cars: {e}")
            return []
    
    async def get_car(self, car_id: str) -> Optional[Car]:
        """
        特定の車情報を取得
        
        Args:
            car_id: 車ID
        
        Returns:
            車情報、見つからない場合はNone
        """
        try:
            response = self.db.table(self.table_name)\
                .select("*")\
                .eq("id", car_id)\
                .execute()
            if response.data:
                return Car(**response.data[0])
            return None
        except Exception as e:
            print(f"Error fetching car: {e}")
            return None
    
    async def save_cars(self, cars: List[CarBase]) -> List[Car]:
        """
        車情報をデータベースに保存
        
        Args:
            cars: 保存する車情報のリスト
        
        Returns:
            保存された車情報のリスト
        """
        if not cars:
            return []
        
        try:
            # 辞書に変換
            cars_data = [car.model_dump(exclude={'id', 'created_at', 'updated_at'}) for car in cars]
            
            # データベースに保存
            response = self.db.table(self.table_name)\
                .insert(cars_data)\
                .execute()
            
            return [Car(**item) for item in response.data]
        except Exception as e:
            print(f"Error saving cars: {e}")
            return []
    
    async def search_cars(
        self,
        make: Optional[str] = None,
        model: Optional[str] = None,
        year_min: Optional[int] = None,
        year_max: Optional[int] = None,
        price_min: Optional[int] = None,
        price_max: Optional[int] = None,
        mileage_max: Optional[int] = None
    ) -> List[Car]:
        """
        車を検索
        
        Args:
            make: メーカー名
            model: 車種名
            year_min: 最小年式
            year_max: 最大年式
            price_min: 最小価格
            price_max: 最大価格
            mileage_max: 最大走行距離
        
        Returns:
            検索結果のリスト
        """
        try:
            query = self.db.table(self.table_name).select("*")
            
            if make:
                query = query.eq("make", make)
            if model:
                query = query.eq("model", model)
            if year_min:
                query = query.gte("year", year_min)
            if year_max:
                query = query.lte("year", year_max)
            if price_min:
                query = query.gte("price", price_min)
            if price_max:
                query = query.lte("price", price_max)
            if mileage_max:
                query = query.lte("mileage", mileage_max)
            
            response = query.execute()
            return [Car(**item) for item in response.data]
        except Exception as e:
            print(f"Error searching cars: {e}")
            return []
