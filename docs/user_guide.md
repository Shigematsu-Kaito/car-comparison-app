# 中古車比較アプリケーション 使用ガイド

## 🚀 クイックスタート

### 1. サーバーの起動

#### バックエンド（FastAPI）
```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```
→ http://localhost:8000 でAPIが起動します

#### フロントエンド（React）
```bash
cd frontend
npm run dev
```
→ http://localhost:5173 でアプリが起動します

---

## 📱 アプリケーションの使い方

### 検索機能
1. ブラウザで http://localhost:5173 を開く
2. 検索フォームに条件を入力：
   - メーカー（例: トヨタ）
   - 車種（例: プリウス）
   - 年式範囲
   - 価格範囲
   - 走行距離
   - 燃料タイプ
   - トランスミッション
3. 「検索する」ボタンをクリック

### 比較機能
1. 検索結果から「比較に追加」ボタンをクリック
2. 複数の車を選択
3. 「比較」タブをクリック
4. 並べて比較表示

### 検討リスト
1. 気になる車の「検討リスト」ボタンをクリック
2. 「検討リスト」タブで確認
3. メモを追加可能
4. 不要な車は削除可能

---

## 🔧 API エンドポイント

### ヘルスチェック
```bash
curl http://localhost:8000/
# レスポンス: {"status":"ok","message":"Used Car Comparison API is running"}

curl http://localhost:8000/health
# レスポンス: {"status":"healthy"}
```

### API ドキュメント
ブラウザで http://localhost:8000/docs を開くとSwagger UIが表示されます。

### 車検索
```bash
curl -X POST http://localhost:8000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "make": "トヨタ",
    "model": "プリウス",
    "price_max": 3000000
  }'
```

### 検討リスト取得
```bash
curl http://localhost:8000/api/watchlist/default-user
```

---

## 🗄️ Supabaseセットアップ

### 1. プロジェクト作成
1. https://supabase.com にアクセス
2. 新規プロジェクトを作成
3. プロジェクト名とパスワードを設定

### 2. データベース設定
1. Supabaseダッシュボードの「SQL Editor」を開く
2. `database/schema.sql` の内容をコピー
3. SQL Editorにペーストして実行

### 3. 接続情報の取得
1. Settings → API を開く
2. 以下をコピー：
   - Project URL
   - anon public key

### 4. 環境変数の設定
`backend/.env` を編集：
```env
SUPABASE_URL=https://あなたのプロジェクト.supabase.co
SUPABASE_KEY=あなたのanonキー
```

### 5. サーバー再起動
バックエンドサーバーを再起動して設定を反映

---

## 🔍 トラブルシューティング

### Q1. バックエンドが起動しない
**原因**: 仮想環境が有効化されていない
```bash
cd backend
venv\Scripts\activate
```

### Q2. フロントエンドが起動しない  
**原因**: 依存関係がインストールされていない
```bash
cd frontend
npm install
```

### Q3. CORSエラーが出る
**原因**: バックエンドの CORS 設定
**解決**: `backend/.env` を確認：
```env
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Q4. Supabaseに接続できない
**確認事項**:
- ✅ `.env` ファイルが存在するか
- ✅ SUPABASE_URL と SUPABASE_KEY が正しいか
- ✅ Supabaseプロジェクトが稼働中か
- ✅ データベーススキーマが適用済みか

### Q5. 検索結果が表示されない
**原因**: スクレイパーが未実装
**現状**: スクレイパーはスケルトンのみ
**対応**: 各サイトのHTML構造に合わせて実装が必要

---

## 📂 主要ファイルの場所

### 設定ファイル
- バックエンド環境変数: `backend/.env`
- フロントエンド環境変数: `frontend/.env`
- Python依存関係: `backend/requirements.txt`
- Node依存関係: `frontend/package.json`

### コア機能
- APIルーティング: `backend/main.py`
- 検索エンドポイント: `backend/app/api/routes/search.py`
- 検討リストAPI: `backend/app/api/routes/watchlist.py`
- メインアプリ: `frontend/src/App.jsx`

### スクレイパー
- カーセンサー: `backend/app/scrapers/carsensor.py`
- Goo-net: `backend/app/scrapers/goonet.py`
- ガリバー: `backend/app/scrapers/gulliver.py`

---

## 🎯 次のステップ

### 必須タスク
1. ✅ Supabaseのセットアップ
2. ⏳ スクレイパーの実装
3. ⏳ 実データでのテスト

### オプション機能
- 認証機能（Supabase Auth）
- 画像管理（Supabase Storage）
- 通知機能
- より高度な検索フィルター

---

## 📞 サポート

- API仕様: `docs/api_spec.md`
- デプロイガイド: `docs/deployment.md`
- プロジェクト概要: `README.md`
