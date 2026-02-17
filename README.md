# 中古車比較Webアプリケーション

複数の中古車サイト（カーセンサー、Goo-net、ガリバー）から情報を収集し、比較・検討できるWebアプリケーションです。

## 技術スタック

### バックエンド
- **FastAPI** - 高速なPython Webフレームワーク
- **Supabase** - PostgreSQLベースのBaaS
- **BeautifulSoup4** - スクレイピングライブラリ
- **Requests** - HTTPライブラリ

### フロントエンド
- **React** - UIライブラリ
- **Vite** - ビルドツール
- **TailwindCSS** - CSSフレームワーク
- **Shadcn UI** - UIコンポーネントライブラリ

## プロジェクト構成

```
used-car-comparison/
├── backend/          # FastAPI バックエンド
├── frontend/         # React フロントエンド
├── database/         # DB関連
└── docs/            # ドキュメント
```

## セットアップ

### 前提条件
- Python 3.9+
- Node.js 18+
- Supabaseアカウント（無料プランで可）

### バックエンドのセットアップ

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
cp .env.example .env
# .env ファイルに Supabase の接続情報を設定
uvicorn main:app --reload
```

### フロントエンドのセットアップ

```bash
cd frontend
npm install
cp .env.example .env
# .env ファイルにバックエンドAPIのURLを設定
npm run dev
```

### データベースのセットアップ

1. Supabaseプロジェクトを作成
2. `database/schema.sql` のSQLを実行してテーブルを作成

## 開発

### バックエンド開発サーバー起動
```bash
cd backend
uvicorn main:app --reload
```
http://localhost:8000 でAPIが起動します。
API仕様: http://localhost:8000/docs

### フロントエンド開発サーバー起動
```bash
cd frontend
npm run dev
```
http://localhost:5173 でアプリが起動します。

## デプロイ

詳細は [docs/deployment.md](docs/deployment.md) を参照してください。

## ライセンス

MIT License
