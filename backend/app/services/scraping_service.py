import asyncio
from typing import List, Optional
from app.models.car import CarBase, CarSearchQuery
from app.scrapers.carsensor import CarSensorScraper
from app.scrapers.goonet import GoonetScraper
from app.scrapers.gulliver import GulliverScraper


class ScrapingService:
    """スクレイピング実行サービス"""
    
    def __init__(self):
        self.scrapers = {
            'carsensor': CarSensorScraper(),
            'goonet': GoonetScraper(),
            'gulliver': GulliverScraper(),
        }
    
    async def scrape_all(
        self,
        query: CarSearchQuery
    ) -> List[CarBase]:
        """
        すべてのソースからスクレイピング
        
        Args:
            query: 検索クエリ
        
        Returns:
            すべてのソースから取得した車情報のリスト
        """
        # 検索対象のソースを決定
        sources = query.sources if query.sources else list(self.scrapers.keys())
        
        # 並列でスクレイピング実行
        tasks = []
        for source in sources:
            if source in self.scrapers:
                scraper = self.scrapers[source]
                task = scraper.scrape(
                    make=query.make,
                    model=query.model,
                    year_min=query.year_min,
                    year_max=query.year_max,
                    price_min=query.price_min,
                    price_max=query.price_max,
                    mileage_max=query.mileage_max,
                    fuel_type=query.fuel_type,
                    transmission=query.transmission
                )
                tasks.append(task)
        
        # すべてのタスクを並列実行
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # 結果を統合
        all_cars = []
        for result in results:
            if isinstance(result, list):
                all_cars.extend(result)
            elif isinstance(result, Exception):
                print(f"Scraping error: {result}")
        
        return all_cars
    
    async def scrape_source(
        self,
        source: str,
        make: Optional[str] = None,
        model: Optional[str] = None,
        **kwargs
    ) -> List[CarBase]:
        """
        特定のソースからスクレイピング
        
        Args:
            source: ソース名（carsensor/goonet/gulliver）
            make: メーカー名
            model: 車種名
            **kwargs: その他の検索条件
        
        Returns:
            取得した車情報のリスト
        """
        if source not in self.scrapers:
            raise ValueError(f"Unknown source: {source}")
        
        scraper = self.scrapers[source]
        return await scraper.scrape(make=make, model=model, **kwargs)
