# API仕様書

## ベースURL

```
http://localhost:8000
```

## エンドポイント一覧

### ヘルスチェック

#### GET /
アプリケーションの稼働状態を確認

**レスポンス**
```json
{
  "status": "ok",
  "message": "中古車比較API稼働中"
}
```

#### GET /health
ヘルスチェック

**レスポンス**
```json
{
  "status": "healthy"
}
```

---

### 車検索

#### POST /api/search
中古車を検索（スクレイピング実行）

**リクエストボディ**
```json
{
  "make": "トヨタ",
  "model": "プリウス",
  "year_min": 2015,
  "year_max": 2023,
  "price_min": 1000000,
  "price_max": 3000000,
  "mileage_max": 50000,
  "fuel_type": "ハイブリッド",
  "transmission": "CVT",
  "sources": ["carsensor", "goonet", "gulliver"]
}
```

**レスポンス**
```json
[
  {
    "id": "uuid",
    "source": "carsensor",
    "make": "トヨタ",
    "model": "プリウス",
    "year": 2020,
    "price": 2500000,
    "mileage": 30000,
    "color": "白",
    "fuel_type": "ハイブリッド",
    "transmission": "CVT",
    "location": "東京都",
    "url": "https://...",
    "image_url": "https://...",
    "description": "...",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
]
```

---

### 車情報取得

#### GET /api/cars
保存済みの車情報を取得

**クエリパラメータ**
- `skip`: スキップする件数（デフォルト: 0）
- `limit`: 取得する最大件数（デフォルト: 100）

**レスポンス**
```json
[
  {
    "id": "uuid",
    "source": "carsensor",
    "make": "トヨタ",
    "model": "プリウス",
    ...
  }
]
```

#### GET /api/cars/{car_id}
特定の車情報を取得

**パスパラメータ**
- `car_id`: 車のUUID

**レスポンス**
```json
{
  "id": "uuid",
  "source": "carsensor",
  "make": "トヨタ",
  "model": "プリウス",
  ...
}
```

---

### 検討リスト

#### GET /api/watchlist/{user_id}
ユーザーの検討リストを取得

**パスパラメータ**
- `user_id`: ユーザーID

**レスポンス**
```json
[
  {
    "id": "uuid",
    "user_id": "user123",
    "car_id": "car-uuid",
    "notes": "検討中",
    "created_at": "2024-01-01T00:00:00Z"
  }
]
```

#### POST /api/watchlist/{user_id}
検討リストに追加

**パスパラメータ**
- `user_id`: ユーザーID

**リクエストボディ**
```json
{
  "car_id": "car-uuid",
  "notes": "検討中"
}
```

**レスポンス**
```json
{
  "id": "uuid",
  "user_id": "user123",
  "car_id": "car-uuid",
  "notes": "検討中",
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### PUT /api/watchlist/{item_id}
検討リストアイテムを更新

**パスパラメータ**
- `item_id`: アイテムのUUID

**リクエストボディ**
```json
{
  "notes": "更新されたメモ"
}
```

**レスポンス**
```json
{
  "id": "uuid",
  "user_id": "user123",
  "car_id": "car-uuid",
  "notes": "更新されたメモ",
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### DELETE /api/watchlist/{item_id}
検討リストから削除

**パスパラメータ**
- `item_id`: アイテムのUUID

**レスポンス**
```json
{
  "message": "削除しました"
}
```

---

## エラーレスポンス

すべてのエンドポイントで、エラー発生時は以下の形式で返されます：

```json
{
  "detail": "エラーメッセージ"
}
```

HTTPステータスコード：
- `400`: リクエストが不正
- `404`: リソースが見つからない
- `500`: サーバーエラー

---

## Swagger UI

APIの詳細仕様とインタラクティブなテストは、以下のURLで確認できます：

```
http://localhost:8000/docs
```
