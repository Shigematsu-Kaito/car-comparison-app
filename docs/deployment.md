# デプロイガイド

## 前提条件

- Supabaseアカウント
- バックエンドデプロイ環境（例: Render、Heroku、Railway）
- フロントエンドデプロイ環境（例: Vercel、Netlify）

---

## データベースのセットアップ

### 1. Supabaseプロジェクトの作成

1. [Supabase](https://supabase.com)にアクセス
2. 新規プロジェクトを作成
3. プロジェクトURLとAPIキーをメモ

### 2. データベーススキーマの適用

1. SupabaseダッシュボードのSQL Editorを開く
2. `database/schema.sql`の内容をコピー
3. SQLエディタにペーストして実行

---

## バックエンドのデプロイ

### Renderを使用する場合

1. [Render](https://render.com)にサインアップ
2. 新規Web Serviceを作成
3. GitHubリポジトリを連携
4. 以下の設定を入力：
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3.11

5. 環境変数を設定：
   - `SUPABASE_URL`: SupabaseプロジェクトURL
   - `SUPABASE_KEY`: Supabase APIキー
   - `CORS_ORIGINS`: フロントエンドのURL（例: https://your-app.vercel.app）

### Dockerを使用する場合

```bash
cd backend
docker build -t car-comparison-backend .
docker run -p 8000:8000 \
  -e SUPABASE_URL=your-url \
  -e SUPABASE_KEY=your-key \
  car-comparison-backend
```

---

## フロントエンドのデプロイ

### Vercelを使用する場合

1. [Vercel](https://vercel.com)にサインアップ
2. 新規プロジェクトを作成
3. GitHubリポジトリを連携
4. 以下の設定を入力：
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

5. 環境変数を設定：
   - `VITE_API_URL`: バックエンドのURL（例: https://your-api.onrender.com）

### Netlifyを使用する場合

1. [Netlify](https://netlify.com)にサインアップ
2. 新規サイトを作成
3. GitHubリポジトリを連携
4. 以下の設定を入力：
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`

5. 環境変数を設定：
   - `VITE_API_URL`: バックエンドのURL

---

## ローカルDocker環境での起動

```bash
# ルートディレクトリで実行
docker-compose up --build
```

アクセス：
- フロントエンド: http://localhost:5173
- バックエンド: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 環境変数の設定

### バックエンド（.env）

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
APP_NAME=中古車比較アプリ
DEBUG=False
CORS_ORIGINS=https://your-frontend-url.com
REQUEST_TIMEOUT=30
MAX_RETRY=3
USER_AGENT=Mozilla/5.0...
```

### フロントエンド（.env）

```env
VITE_API_URL=https://your-backend-url.com
```

---

## トラブルシューティング

### CORSエラーが発生する場合

バックエンドの`.env`ファイルで、`CORS_ORIGINS`にフロントエンドのURLを追加してください。

```env
CORS_ORIGINS=http://localhost:5173,https://your-frontend.vercel.app
```

### データベース接続エラー

1. Supabaseプロジェクトが稼働していることを確認
2. 環境変数`SUPABASE_URL`と`SUPABASE_KEY`が正しいか確認
3. データベーススキーマが適用されているか確認

### スクレイピングが動作しない

1. 各サイトのスクレイパーは実装スケルトンのため、実際のHTML構造に合わせて実装が必要です
2. robots.txtと利用規約を確認し、適切なクローリングマナーを守ってください

---

## セキュリティ considerations

1. **環境変数の管理**
   - `.env`ファイルは`.gitignore`に追加済み
   - 本番環境では必ず環境変数を使用

2. **APIキーの保護**
   - Supabase APIキーは公開しない
   - フロントエンドでは匿名キーのみ使用

3. **CORS設定**
   - 本番環境では特定のドメインのみ許可

4. **レート制限**
   - 必要に応じてAPIレート制限を実装
