# Git Commit ガイド

このプロジェクトでは、一貫性のあるコミットメッセージを使用することを推奨します。

## コミットメッセージのフォーマット

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type（必須）

- `feat`: 新機能
- `fix`: バグ修正
- `docs`: ドキュメントのみの変更
- `style`: コードの意味に影響しない変更（空白、フォーマット、セミコロンなど）
- `refactor`: バグ修正も新機能追加もしないコード変更
- `perf`: パフォーマンス向上のためのコード変更
- `test`: テストの追加や修正
- `chore`: ビルドプロセスやツールの変更

### Scope（オプション）

変更の範囲を示します：

- `backend`: バックエンド関連
- `frontend`: フロントエンド関連
- `docs`: ドキュメント
- `db`: データベース
- `api`: APIエンドポイント
- `ui`: UIコンポーネント

### Subject（必須）

変更内容の簡潔な説明：

- 現在形の動詞で始める
- 最初の文字を小文字にする
- 末尾にピリオドをつけない
- 50文字以内

### Body（オプション）

変更の理由や詳細：

- 72文字で改行
- 何を変更したかではなく、なぜ変更したかを説明

### Footer（オプション）

- `BREAKING CHANGE`: 破壊的変更の説明
- `Closes #123`: Issue番号の参照

---

## コミット例

### 新機能追加

```bash
git commit -m "feat(backend): add car search endpoint"
```

```bash
git commit -m "feat(frontend): add car comparison grid component

Add new component to display multiple cars side-by-side
for easy comparison. Includes responsive layout for mobile."
```

### バグ修正

```bash
git commit -m "fix(api): correct price parsing in scraper"
```

```bash
git commit -m "fix(frontend): resolve CORS error in API calls

Update axios configuration to include proper headers
for cross-origin requests."
```

### ドキュメント更新

```bash
git commit -m "docs: update Supabase setup guide"
```

```bash
git commit -m "docs(readme): add installation instructions

Include detailed setup steps for both backend and frontend
with troubleshooting section."
```

### リファクタリング

```bash
git commit -m "refactor(backend): extract database logic to service layer"
```

### スタイル変更

```bash
git commit -m "style(frontend): format code with prettier"
```

### テスト追加

```bash
git commit -m "test(backend): add unit tests for scrapers"
```

### ビルド/ツール変更

```bash
git commit -m "chore: add development helper scripts"
```

---

## よく使うGitコマンド

### 基本的なワークフロー

```bash
# 変更を確認
git status

# ファイルをステージング
git add .

# コミット
git commit -m "feat: add new feature"

# プッシュ
git push origin main
```

### ブランチ管理

```bash
# 新しいブランチを作成
git checkout -b feature/car-search

# ブランチを切り替え
git checkout main

# ブランチをマージ
git merge feature/car-search

# ブランチを削除
git branch -d feature/car-search
```

### 変更の取り消し

```bash
# ステージングを取り消し
git reset HEAD <file>

# コミットを取り消し（変更は保持）
git reset --soft HEAD^

# コミットを取り消し（変更も破棄）
git reset --hard HEAD^

# 特定のファイルの変更を破棄
git checkout -- <file>
```

### 履歴確認

```bash
# コミット履歴を表示
git log

# 簡潔な履歴表示
git log --oneline

# グラフィカルな履歴表示
git log --graph --oneline --all
```

---

## プロジェクト固有のワークフロー

### 機能追加の場合

```bash
# 1. 新しいブランチを作成
git checkout -b feature/watchlist-notifications

# 2. 変更を加える
# ... コーディング ...

# 3. テストを実行
cd backend && pytest tests/

# 4. コミット
git add .
git commit -m "feat(backend): add email notifications for watchlist

Send email alerts when car prices drop below user-defined threshold.
Includes new endpoint /api/watchlist/notifications"

# 5. プッシュ
git push origin feature/watchlist-notifications

# 6. プルリクエストを作成（GitHub上で）
```

### バグ修正の場合

```bash
# 1. 修正用ブランチを作成
git checkout -b fix/price-parsing-error

# 2. バグを修正
# ... コーディング ...

# 3. テストを追加
# ... テスト追加 ...

# 4. コミット
git add .
git commit -m "fix(backend): correct price parsing for million yen values

fixes #42"

# 5. プッシュ
git push origin fix/price-parsing-error
```

---

## .gitignore の確認

以下のファイルは自動的に無視されます：

```
# Python
__pycache__/
*.py[cod]
venv/
.env

# Node
node_modules/
.env.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## コミット前のチェックリスト

- [ ] コードが正しく動作する
- [ ] テストがパスする（`pytest tests/`）
- [ ] リンターでエラーがない
- [ ] 不要なコメントやデバッグコードを削除
- [ ] `.env` などの機密情報を含まない
- [ ] コミットメッセージが明確
- [ ] 関連するIssueがあれば参照

---

## 参考資料

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
