from abc import ABC, abstractmethod
from typing import List, Optional
import requests
from bs4 import BeautifulSoup
from app.models.car import CarBase
from app.core.config import settings


class BaseScraper(ABC):
    """スクレイパーの基底クラス"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': settings.USER_AGENT
        })
        self.timeout = settings.REQUEST_TIMEOUT
        self.max_retry = settings.MAX_RETRY
    
    @abstractmethod
    def get_source_name(self) -> str:
        """情報源の名前を返す"""
        pass
    
    @abstractmethod
    async def scrape(
        self,
        make: Optional[str] = None,
        model: Optional[str] = None,
        **kwargs
    ) -> List[CarBase]:
        """
        中古車情報をスクレイピング
        
        Args:
            make: メーカー名
            model: 車種名
            **kwargs: その他の検索条件
        
        Returns:
            中古車情報のリスト
        """
        pass
    
    def _get_html(self, url: str) -> Optional[BeautifulSoup]:
        """
        URLからHTMLを取得してパース
        
        Args:
            url: 取得するURL
        
        Returns:
            BeautifulSoupオブジェクト
        """
        for attempt in range(self.max_retry):
            try:
                response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()
                return BeautifulSoup(response.content, 'lxml')
            except Exception as e:
                if attempt == self.max_retry - 1:
                    print(f"Failed to fetch {url}: {e}")
                    return None
        return None
    
    def _clean_text(self, text: Optional[str]) -> Optional[str]:
        """テキストをクリーニング"""
        if not text:
            return None
        return text.strip().replace('\n', ' ').replace('\r', '')
    
    def _parse_price(self, price_str: str) -> Optional[int]:
        """価格文字列を数値に変換"""
        try:
            # 「123.4万円」や「1,234,567円」などを処理
            cleaned = price_str.replace('万円', '0000').replace('円', '').replace(',', '').replace(' ', '')
            return int(float(cleaned))
        except (ValueError, AttributeError):
            return None
    
    def _parse_mileage(self, mileage_str: str) -> Optional[int]:
        """走行距離文字列を数値に変換"""
        try:
            # 「12,345km」や「1.2万km」などを処理
            cleaned = mileage_str.replace('万km', '0000').replace('km', '').replace(',', '').replace(' ', '')
            return int(float(cleaned))
        except (ValueError, AttributeError):
            return None
