# スクレイパー実装ガイド

このガイドでは、実際のWebサイトから中古車情報をスクレイピングする方法を説明します。

---

## ⚠️ 重要な注意事項

### 法的・倫理的考慮事項

> [!CAUTION]
> スクレイピングを実装する前に、必ず以下を確認してください：
> 
> 1. **robots.txt**: サイトのスクレイピングポリシーを確認
> 2. **利用規約**: サイトの利用規約を熟読
> 3. **著作権**: 取得したデータの使用権限を確認
> 4. **個人情報**: 個人情報保護法に準拠
> 5. **アクセス頻度**: サーバーに過度な負荷をかけない

### 推奨事項

- **レート制限**: リクエスト間隔を3-5秒以上空ける
- **User-Agent**: 適切なUser-Agentを設定
- **robots.txt遵守**: 禁止されているパスにアクセスしない
- **APIの利用**: 公式APIが提供されている場合はそちらを優先

---

## 📋 スクレイパーの基本構造

すでに用意されている `BaseScraper` クラスを継承して実装します。

### 必須メソッド

```python
async def scrape(self, **kwargs) -> List[Dict]:
    """
    スクレイピングを実行
    
    Args:
        **kwargs: 検索条件（make, model, price_max など）
        
    Returns:
        List[Dict]: 車情報のリスト
    """
    pass

def _parse_car_item(self, item) -> Optional[Dict]:
    """
    1つの車情報をパース
    
    Args:
        item: BeautifulSoup要素
        
    Returns:
        Dict: 車情報の辞書
    """
    pass
```

---

## 🛠️ 実装例: カーセンサースクレイパー

### ステップ1: HTML構造の調査

1. カーセンサーのサイトにアクセス
2. 開発者ツール（F12）を開く
3. 車情報の要素を確認

**例:**
```html
<article class="car-item">
    <div class="item-img">
        <img src="..." alt="...">
    </div>
    <div class="item-info">
        <h2 class="item-title">トヨタ プリウス</h2>
        <p class="item-price">250万円</p>
        <p class="item-year">2020年</p>
        <p class="item-mileage">3.0万km</p>
    </div>
</article>
```

### ステップ2: パース処理の実装

```python
from typing import Dict, List, Optional
from bs4 import BeautifulSoup
from .base import BaseScraper
from .utils import normalize_make, format_price, format_mileage

class CarSensorScraper(BaseScraper):
    """カーセンサー用スクレイパー"""
    
    BASE_URL = "https://www.carsensor.net"
    
    def _build_search_url(self, make: str = None, model: str = None, 
                         price_max: int = None, **kwargs) -> str:
        """検索URLを構築"""
        # 実際のカーセンサーの検索URLパラメータに合わせて実装
        url = f"{self.BASE_URL}/usedcar/search.php?"
        params = []
        
        if make:
            # メーカーコードに変換（要実装）
            params.append(f"STID=CS210610&brand={make}")
        if model:
            params.append(f"model={model}")
        if price_max:
            # 価格を万円単位に変換
            price_man = price_max // 10000
            params.append(f"PRICE={price_man}")
            
        return url + "&".join(params)
    
    async def scrape(self, **kwargs) -> List[Dict]:
        """
        カーセンサーから車情報をスクレイピング
        
        Args:
            make: メーカー名
            model: 車種名
            price_max: 最大価格
            
        Returns:
            List[Dict]: 車情報のリスト
        """
        url = self._build_search_url(**kwargs)
        html = await self._fetch_html(url)
        
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'lxml')
        
        # 車リストの要素を取得（実際のCSSセレクタに合わせる）
        car_items = soup.select('.car-item, article.usedcar')
        
        cars = []
        for item in car_items:
            car = self._parse_car_item(item)
            if car:
                cars.append(car)
        
        return cars
    
    def _parse_car_item(self, item) -> Optional[Dict]:
        """
        1つの車情報をパース
        
        Args:
            item: BeautifulSoup要素
            
        Returns:
            Dict: 車情報
        """
        try:
            # タイトルから車種情報を抽出
            title = self._clean_text(
                item.select_one('.item-title, h2').get_text()
            )
            # "トヨタ プリウス" -> メーカーと車種に分割
            parts = title.split()
            if len(parts) < 2:
                return None
            
            make = normalize_make(parts[0])
            model = parts[1]
            
            # 価格
            price_text = self._clean_text(
                item.select_one('.item-price, .price').get_text()
            )
            price = self._parse_price(price_text)
            
            # 年式
            year_text = self._clean_text(
                item.select_one('.item-year, .year').get_text()
            )
            year = int(''.join(filter(str.isdigit, year_text)))
            
            # 走行距離
            mileage_text = self._clean_text(
                item.select_one('.item-mileage, .mileage').get_text()
            )
            mileage = self._parse_mileage(mileage_text)
            
            # 画像URL
            img = item.select_one('.item-img img, img')
            image_url = img['src'] if img else None
            
            # 詳細ページURL
            link = item.select_one('a')
            url = self.BASE_URL + link['href'] if link else None
            
            # その他の情報
            color = self._clean_text(
                item.select_one('.item-color, .color').get_text()
            ) if item.select_one('.item-color, .color') else None
            
            return {
                'source': 'carsensor',
                'make': make,
                'model': model,
                'year': year,
                'price': price,
                'mileage': mileage,
                'color': color,
                'url': url,
                'image_url': image_url,
                'fuel_type': None,  # 要実装
                'transmission': None,  # 要実装
                'location': None,  # 要実装
                'description': None  # 要実装
            }
            
        except Exception as e:
            print(f"Error parsing car item: {e}")
            return None
```

---

## 🧪 テスト方法

### 1. 単体テスト

```python
# backend/tests/test_carsensor_scraper.py
import pytest
from app.scrapers.carsensor import CarSensorScraper

@pytest.mark.asyncio
async def test_carsensor_scraper():
    scraper = CarSensorScraper()
    results = await scraper.scrape(make="トヨタ", price_max=3000000)
    
    assert len(results) > 0
    assert all('make' in car for car in results)
    assert all('price' in car for car in results)

@pytest.mark.asyncio
async def test_carsensor_parse_item():
    scraper = CarSensorScraper()
    # HTMLサンプルでテスト
    html = '''
    <article class="car-item">
        <h2 class="item-title">トヨタ プリウス</h2>
        <p class="item-price">250万円</p>
        <p class="item-year">2020年</p>
        <p class="item-mileage">3.0万km</p>
        <a href="/detail/123"></a>
    </article>
    '''
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    item = soup.select_one('.car-item')
    
    result = scraper._parse_car_item(item)
    
    assert result is not None
    assert result['make'] == 'Toyota'
    assert result['model'] == 'プリウス'
    assert result['year'] == 2020
    assert result['price'] == 2500000
```

### 2. 実行テスト

```bash
cd backend
pytest tests/test_carsensor_scraper.py -v
```

---

## 🔍 デバッグのヒント

### HTML構造の確認

```python
# 一時的なデバッグコード
async def debug_scrape(self):
    url = "https://example.com/cars"
    html = await self._fetch_html(url)
    soup = BeautifulSoup(html, 'lxml')
    
    # HTMLをファイルに保存
    with open('debug.html', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    
    # 要素の確認
    items = soup.select('.car-item')
    print(f"Found {len(items)} items")
    
    if items:
        first = items[0]
        print(first.prettify())
```

### レスポンスの確認

```python
# ステータスコードとヘッダーの確認
async def _fetch_html_debug(self, url: str) -> Optional[str]:
    response = await self.session.get(url)
    print(f"Status: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Content length: {len(response.text)}")
    return response.text if response.status_code == 200 else None
```

---

## 📊 パフォーマンス最適化

### 並行スクレイピング

```python
import asyncio

async def scrape_multiple_pages(self, base_url: str, num_pages: int = 5):
    """複数ページを並行スクレイピング"""
    tasks = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}&page={page}"
        tasks.append(self._fetch_and_parse(url))
    
    results = await asyncio.gather(*tasks)
    # 結果を平坦化
    all_cars = []
    for page_results in results:
        all_cars.extend(page_results)
    
    return all_cars
```

### キャッシング

```python
from functools import lru_cache
import hashlib
import json

@lru_cache(maxsize=100)
def _get_cached_results(self, cache_key: str) -> Optional[List[Dict]]:
    """結果をキャッシュ"""
    # ファイルベースのキャッシュ
    cache_file = f"cache/{cache_key}.json"
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)
    return None

def _save_to_cache(self, cache_key: str, data: List[Dict]):
    """結果をキャッシュに保存"""
    os.makedirs('cache', exist_ok=True)
    with open(f"cache/{cache_key}.json", 'w') as f:
        json.dump(data, f)
```

---

## 🚀 次のステップ

1. **robots.txtの確認**: 各サイトのスクレイピングポリシーを確認
2. **実装**: `carsensor.py`、`goonet.py`、`gulliver.py` を実装
3. **テスト**: 単体テストと統合テストを実施
4. **エラー処理**: 接続エラー、タイムアウトなどの処理を追加
5. **レート制限**: 適切な間隔を設定
6. **モニタリング**: ログとエラートラッキングを実装

---

## 📚 参考資料

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [aiohttp Documentation](https://docs.aiohttp.org/)
- [robots.txt Specification](https://www.robotstxt.org/)
- [Web Scraping Best Practices](https://www.scrapehero.com/web-scraping-best-practices/)
