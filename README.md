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

## 🚀 クイックスタート

初めての方は [QUICKSTART.md](QUICKSTART.md) を参照してください（5分でスタート！）

**便利なコマンド:**
- Windows: `dev.bat help`
- Mac/Linux: `./dev.sh help` または `make help`

## セットアップ

### 前提条件
- Python 3.9+
- Node.js 18+
- Supabaseアカウント（無料プランで可）

### 1. Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env file with your Supabase credentials
```

### 2. Supabase Database
Follow the detailed guide: [docs/supabase_setup.md](docs/supabase_setup.md)

Quick steps:
1. Create a Supabase project
2. Run `database/schema.sql` in SQL Editor
3. (Optional) Run `database/sample_data.sql` for test data
4. Copy URL and API key to `backend/.env`

### 3. Frontend
```bash
cd frontend
npm install
cp .env.example .env
# Edit .env file if needed (default is http://localhost:8000)
```

## Development

### Start Backend
```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Start Frontend
```bash
cd frontend
npm run dev
# App: http://localhost:5173
```

## Documentation

- [API Specification](docs/api_spec.md) - REST API endpoints
- [Supabase Setup Guide](docs/supabase_setup.md) - Database setup with screenshots
- [User Guide](docs/user_guide.md) - How to use the application
- [Deployment Guide](docs/deployment.md) - Production deployment

## プロジェクト構成

```
.
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── models/      # Pydantic models
│   │   ├── services/    # Business logic
│   │   ├── scrapers/    # Web scrapers
│   │   └── core/        # Config & DB
│   ├── tests/           # Unit tests
│   └── main.py          # Entry point
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── hooks/       # Custom hooks
│   │   ├── services/    # API client
│   │   └── styles/      # Global styles
│   └── index.html       # HTML entry
├── database/            # Database schemas
│   ├── schema.sql       # Table definitions
│   └── sample_data.sql  # Test data
└── docs/                # Documentation
```
