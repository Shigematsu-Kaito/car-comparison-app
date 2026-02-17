import pytest
from app.scrapers.carsensor import CarSensorScraper
from app.scrapers.goonet import GoonetScraper
from app.scrapers.gulliver import GulliverScraper
from app.scrapers.utils import (
    normalize_make,
    normalize_fuel_type,
    normalize_transmission,
    format_price,
    format_mileage
)


class TestScrapers:
    """スクレイパーのテスト"""
    
    def test_carsensor_scraper_init(self):
        """カーセンサースクレイパーの初期化テスト"""
        scraper = CarSensorScraper()
        assert scraper.get_source_name() == "carsensor"
    
    def test_goonet_scraper_init(self):
        """Goo-netスクレイパーの初期化テスト"""
        scraper = GoonetScraper()
        assert scraper.get_source_name() == "goonet"
    
    def test_gulliver_scraper_init(self):
        """ガリバースクレイパーの初期化テスト"""
        scraper = GulliverScraper()
        assert scraper.get_source_name() == "gulliver"
    
    @pytest.mark.asyncio
    async def test_scrape_empty_result(self):
        """スクレイピングの空結果テスト"""
        scraper = CarSensorScraper()
        results = await scraper.scrape()
        # 現在の実装では空のリストを返す
        assert isinstance(results, list)


class TestScraperUtils:
    """スクレイパーユーティリティのテスト"""
    
    def test_normalize_make(self):
        """メーカー名正規化のテスト"""
        assert normalize_make("TOYOTA") == "トヨタ"
        assert normalize_make("toyota") == "トヨタ"
        assert normalize_make("honda") == "ホンダ"
    
    def test_normalize_fuel_type(self):
        """燃料タイプ正規化のテスト"""
        assert normalize_fuel_type("ガソリン") == "ガソリン"
        assert normalize_fuel_type("レギュラー") == "ガソリン"
        assert normalize_fuel_type("HV") == "ハイブリッド"
        assert normalize_fuel_type("EV") == "電気"
    
    def test_normalize_transmission(self):
        """トランスミッション正規化のテスト"""
        assert normalize_transmission("オートマ") == "AT"
        assert normalize_transmission("A/T") == "AT"
        assert normalize_transmission("マニュアル") == "MT"
        assert normalize_transmission("CVT") == "CVT"
    
    def test_format_price(self):
        """価格フォーマットのテスト"""
        assert format_price(1234567) == "123.5万円"
        assert format_price(5000) == "5000円"
    
    def test_format_mileage(self):
        """走行距離フォーマットのテスト"""
        assert format_mileage(12345) == "1.2万km"
        assert format_mileage(5000) == "5000km"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
