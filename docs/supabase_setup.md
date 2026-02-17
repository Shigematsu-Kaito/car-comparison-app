# Supabase セットアップガイド

このガイドでは、Supabase（無料プラン）のセットアップ手順を詳しく説明します。

---

## 📋 前提条件

- Googleアカウント、GitHubアカウント、またはメールアドレス
- ブラウザ（Chrome、Firefox、Edge など）

---

## 🚀 ステップ1: Supabaseアカウント作成

### 1.1 Supabaseにアクセス
https://supabase.com にアクセス

### 1.2 サインアップ
1. 右上の「Start your project」をクリック
2. GitHubアカウントでサインイン（推奨）
   - または、メールアドレスでサインアップ
3. 認証を完了

---

## 🏗️ ステップ2: プロジェクト作成

### 2.1 新規プロジェクト作成
1. ダッシュボードで「New Project」をクリック
2. 以下を入力：
   - **Name**: `used-car-comparison` （任意の名前）
   - **Database Password**: 強力なパスワードを設定（メモしておく）
   - **Region**: `Northeast Asia (Tokyo)` を選択（日本の場合）
   - **Pricing Plan**: `Free` を選択

3. 「Create new project」をクリック
4. プロジェクトの初期化を待つ（1-2分）

---

## 🗄️ ステップ3: データベーススキーマの作成

### 3.1 SQL Editorを開く
1. 左サイドバーから「SQL Editor」をクリック
2. 「New query」をクリック

### 3.2 スキーマSQLを実行
1. プロジェクトの `database/schema.sql` ファイルを開く
2. 内容を**すべてコピー**
3. SQL Editorにペースト
4. 右下の「Run」ボタンをクリック
5. 成功メッセージを確認

### 3.3 サンプルデータを投入（オプション）
1. 「New query」をクリック
2. `database/sample_data.sql` の内容をコピー
3. SQL Editorにペースト
4. 「Run」をクリック
5. 6件のサンプル車データが作成される

---

## 🔑 ステップ4: API認証情報の取得

### 4.1 Project Settings を開く
1. 左下の「Settings」（歯車アイコン）をクリック
2. 「API」をクリック

### 4.2 必要な情報をコピー

#### Project URL
```
URL: https://xxxxxxxxxxxxx.supabase.co
```
↑ この URL をコピー

#### Project API keys
```
anon public: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
↑ `anon` `public` キーをコピー

> [!CAUTION]
> `service_role` キーは**絶対に**公開しないでください！
> バックエンドでも `anon` キーを使用します。

---

## ⚙️ ステップ5: 環境変数の設定

### 5.1 バックエンド設定
`backend/.env` ファイルを編集：

```env
# Supabase connection info
SUPABASE_URL=https://xxxxxxxxxxxxx.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Application settings
APP_NAME=Used Car Comparison API
DEBUG=True
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# Scraping settings
REQUEST_TIMEOUT=30
MAX_RETRY=3
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
```

> [!IMPORTANT]
> `SUPABASE_URL` と `SUPABASE_KEY` を**実際の値**に置き換えてください！

### 5.2 フロントエンド設定
`frontend/.env` ファイルはそのままでOK：
```env
VITE_API_URL=http://localhost:8000
```

---

## 🧪 ステップ6: 動作確認

### 6.1 バックエンドを再起動
```bash
# 現在のuvicornサーバーを停止（Ctrl+C）
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```

### 6.2 接続テスト
ブラウザで以下にアクセス：
```
http://localhost:8000/docs
```

### 6.3 APIをテスト
Swagger UIで以下を試す：

#### 1. ヘルスチェック
- `GET /health` → Execute
- レスポンス: `{"status":"healthy"}`

#### 2. 車データ取得（サンプルデータを投入した場合）
- `GET /api/cars` → Execute
- レスポンス: 6件の車データが返ってくる

### 6.4 フロントエンドで確認
ブラウザで以下にアクセス：
```
http://localhost:5173
```

サンプルデータを投入していれば、`GET /api/cars` で取得したデータが表示されます。

---

## 🔍 データベースの確認

### Table Editorで確認
1. Supabaseダッシュボードで「Table Editor」をクリック
2. `cars` テーブルを選択
3. サンプルデータが表示される

### SQL Editorでクエリ実行
```sql
-- 全データ確認
SELECT * FROM cars ORDER BY created_at DESC;

-- メーカー別集計
SELECT make, COUNT(*) as count, AVG(price) as avg_price
FROM cars
GROUP BY make
ORDER BY count DESC;

-- 価格帯別集計
SELECT 
    CASE 
        WHEN price < 2000000 THEN 'Under 2M JPY'
        WHEN price < 3000000 THEN '2M-3M JPY'
        ELSE 'Over 3M JPY'
    END as price_range,
    COUNT(*) as count
FROM cars
GROUP BY price_range;
```

---

## 🛡️ ステップ7: セキュリティ設定（オプション）

### Row Level Security (RLS)
現在は無効になっていますが、本番環境では有効化を推奨：

```sql
-- RLSを有効化
ALTER TABLE cars ENABLE ROW LEVEL SECURITY;
ALTER TABLE watchlist ENABLE ROW LEVEL SECURITY;

-- 読み取り許可（全員）
CREATE POLICY "Allow public read access" ON cars
    FOR SELECT USING (true);

-- 書き込み許可（認証済みユーザーのみ）
CREATE POLICY "Allow authenticated write access" ON cars
    FOR ALL USING (auth.role() = 'authenticated');
```

---

## 🎯 よくある問題

### Q1. 接続できない
**確認事項:**
- `.env` ファイルが存在するか
- `SUPABASE_URL` と `SUPABASE_KEY` が正しいか
- バックエンドを再起動したか

### Q2. データが表示されない
**確認事項:**
- `schema.sql` を実行したか
- `sample_data.sql` を実行したか（オプション）
- Table Editorでデータが存在するか確認

### Q3. CORS エラー
**確認事項:**
- `backend/.env` の `CORS_ORIGINS` にフロントエンドのURLが含まれているか
- バックエンドを再起動したか

---

## 📊 モニタリング

### Supabase Dashboard
- **Database**: データベース使用状況
- **API**: API呼び出し統計
- **Logs**: エラーログ確認

### 無料プランの制限
- データベース: 500MB
- ストレージ: 1GB
- 帯域幅: 5GB/月
- API リクエスト: 無制限（レート制限あり）

---

## ✅ セットアップ完了チェックリスト

- [ ] Supabaseプロジェクトを作成
- [ ] `schema.sql` を実行してテーブルを作成
- [ ] `sample_data.sql` を実行してサンプルデータを投入
- [ ] API認証情報（URL、Key）を取得
- [ ] `backend/.env` に認証情報を設定
- [ ] バックエンドを再起動
- [ ] `http://localhost:8000/docs` でAPI動作確認
- [ ] `http://localhost:5173` でフロントエンド動作確認

---

## 🚀 次のステップ

セットアップが完了したら：

1. **スクレイパーの実装**: 実際のサイトからデータを取得
2. **認証機能の追加**: Supabase Authを使用
3. **検索機能の強化**: より詳細なフィルター
4. **デプロイ**: 本番環境への展開

詳細は `docs/deployment.md` を参照してください。
