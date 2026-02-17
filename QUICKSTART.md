# クイックスタートガイド

このガイドでは、最速でアプリケーションを起動する手順を説明します。

## 🚀 5分でスタート

### Windows ユーザー

```cmd
REM 1. セットアップ（初回のみ）
dev.bat setup

REM 2. Supabase設定（詳細は後述）
REM backend\.env を編集してSupabase接続情報を追加

REM 3. 起動
dev.bat start
```

### Mac/Linux ユーザー

```bash
# 1. セットアップ（初回のみ）
chmod +x dev.sh
./dev.sh setup

# 2. Supabase設定（詳細は後述）
# backend/.env を編集してSupabase接続情報を追加

# 3. 起動
./dev.sh start
```

---

## 📝 詳細手順

### ステップ1: 初回セットアップ

#### Windows
```cmd
dev.bat setup
```

#### Mac/Linux
```bash
chmod +x dev.sh
./dev.sh setup
```

これで以下が自動的に実行されます：
- ✅ Python仮想環境の作成
- ✅ バックエンド依存関係のインストール
- ✅ フロントエンド依存関係のインストール
- ✅ .envファイルの作成

### ステップ2: Supabaseセットアップ

#### 2.1 アカウント作成（無料）
1. https://supabase.com にアクセス
2. GitHubアカウントでサインイン
3. 新しいプロジェクトを作成
   - Name: `used-car-comparison`
   - Region: `Northeast Asia (Tokyo)`
   - Password: 強力なパスワードを設定

#### 2.2 データベーススキーマの作成
1. Supabaseダッシュボードで「SQL Editor」を開く
2. 「New query」をクリック
3. `database/schema.sql` の内容を全てコピー&ペースト
4. 「Run」をクリック

#### 2.3 サンプルデータの投入（オプション）
1. 「New query」をクリック
2. `database/sample_data.sql` の内容をコピー&ペースト
3. 「Run」をクリック
4. 6件の車データが作成されます

#### 2.4 API認証情報の取得
1. Supabaseダッシュボードで「Settings」→「API」を開く
2. 以下をコピー：
   - **Project URL**: `https://xxxxx.supabase.co`
   - **anon public key**: `eyJhbG...`

#### 2.5 .envファイルの編集
`backend/.env` を開いて以下を入力：

```env
SUPABASE_URL=ここにProject URLをペースト
SUPABASE_KEY=ここにanon public keyをペースト

APP_NAME=Used Car Comparison API
DEBUG=True
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

REQUEST_TIMEOUT=30
MAX_RETRY=3
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
```

> [!IMPORTANT]
> `SUPABASE_URL` と `SUPABASE_KEY` を**実際の値に置き換えてください**！

詳細: [docs/supabase_setup.md](file:///c:/Users/81802/test/docs/supabase_setup.md)

### ステップ3: アプリケーションの起動

#### Windows
```cmd
dev.bat start
```

#### Mac/Linux
```bash
./dev.sh start
```

2つの新しいウィンドウが開きます：
- 🔧 **Backend Server**: http://localhost:8000
- 🎨 **Frontend Server**: http://localhost:5173

### ステップ4: 動作確認

#### バックエンドの確認
ブラウザで以下にアクセス：
```
http://localhost:8000/docs
```
→ Swagger UIが表示されます

#### フロントエンドの確認
ブラウザで以下にアクセス：
```
http://localhost:5173
```
→ アプリのUIが表示されます

#### APIテスト
Swagger UIで以下を試す：
1. `GET /health` → Execute
   - レスポンス: `{"status":"healthy"}`
2. `GET /api/cars` → Execute
   - サンプルデータを投入していれば、車データが返ってきます

---

## 🎯 よくある質問

### Q: Supabase無しで試せますか？
**A**: バックエンドは起動できますが、データベース機能は使えません。まずはSupabaseの無料プランをセットアップすることを強くお勧めします（5分で完了）。

### Q: エラーが出ました
**A**: 以下を確認してください：
1. `.env` ファイルが存在し、正しい値が設定されているか
2. Python 3.9以上がインストールされているか
3. Node.js 18以上がインストールされているか
4. インターネット接続があるか

詳細: [docs/user_guide.md](file:///c:/Users/81802/test/docs/user_guide.md) のトラブルシューティングセクション

### Q: どこから開発を始めればいいですか？
**A**: 以下の順番をお勧めします：
1. ✅ クイックスタート（このガイド）
2. 📖 [ユーザーガイド](file:///c:/Users/81802/test/docs/user_guide.md) - アプリの使い方を理解
3. 🔧 [スクレイパー実装ガイド](file:///c:/Users/81802/test/docs/scraper_implementation.md) - 実際のデータ取得
4. 🚀 [デプロイガイド](file:///c:/Users/81802/test/docs/deployment.md) - 本番環境へ

---

## 📚 その他のリソース

### ドキュメント
- [README](file:///c:/Users/81802/test/README.md) - プロジェクト概要
- [API仕様](file:///c:/Users/81802/test/docs/api_spec.md) - 全エンドポイント
- [Gitガイド](file:///c:/Users/81802/test/docs/git_guide.md) - Gitの使い方

### 便利なコマンド

#### Windows
```cmd
dev.bat help          # ヘルプを表示
dev.bat backend       # バックエンドだけ起動
dev.bat frontend      # フロントエンドだけ起動
dev.bat test          # テストを実行
dev.bat clean         # キャッシュを削除
dev.bat db-setup      # データベース設定ガイド
```

#### Mac/Linux
```bash
./dev.sh help         # ヘルプを表示
./dev.sh backend      # バックエンドだけ起動
./dev.sh frontend     # フロントエンドだけ起動
./dev.sh test         # テストを実行
./dev.sh clean        # キャッシュを削除
./dev.sh db-setup     # データベース設定ガイド
```

---

## ✨ 次のステップ

セットアップが完了したら：

1. **アプリを触ってみる**
   - 検索機能を試す
   - 比較機能を使う
   - 検討リストに追加

2. **スクレイパーを実装**
   - [実装ガイド](file:///c:/Users/81802/test/docs/scraper_implementation.md)を参照
   - 実際のサイトからデータを取得

3. **機能を追加**
   - 認証機能
   - 通知機能
   - フィルター機能の強化

4. **デプロイ**
   - [デプロイガイド](file:///c:/Users/81802/test/docs/deployment.md)を参照
   - Render + Vercelで公開

---

開発を楽しんでください！ 🚗✨
