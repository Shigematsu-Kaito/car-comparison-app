.PHONY: help setup start backend frontend test lint clean db-setup

# Default target
help:
	@echo "中古車比較アプリ - Makefile"
	@echo ""
	@echo "使用方法: make [target]"
	@echo ""
	@echo "利用可能なターゲット:"
	@echo "  setup           - 初回セットアップを実行"
	@echo "  start           - バックエンドとフロントエンドを起動"
	@echo "  backend         - バックエンドのみ起動"
	@echo "  frontend        - フロントエンドのみ起動"
	@echo "  test            - テストを実行"
	@echo "  lint            - コード品質チェック"
	@echo "  clean           - キャッシュと一時ファイルを削除"
	@echo "  db-setup        - データベースセットアップガイドを表示"
	@echo ""

# Initial setup
setup:
	@echo "[INFO] 初回セットアップを開始します..."
	@echo "[INFO] バックエンドのセットアップ..."
	cd backend && \
	python -m venv venv && \
	. venv/bin/activate && \
	pip install -r requirements.txt
	@if [ ! -f backend/.env ]; then \
		cp backend/.env.example backend/.env; \
		echo "[WARNING] .envファイルを作成しました。Supabase接続情報を設定してください！"; \
	fi
	@echo "[INFO] フロントエンドのセットアップ..."
	cd frontend && npm install
	@if [ ! -f frontend/.env ]; then \
		cp frontend/.env.example frontend/.env; \
		echo "[INFO] .envファイルを作成しました"; \
	fi
	@echo "[INFO] セットアップ完了！"
	@echo "[INFO] 次のステップ: make db-setup でデータベースをセットアップしてください"

# Start both servers (requires two terminals)
start:
	@echo "[INFO] バックエンドとフロントエンドを起動します..."
	@echo "[INFO] 注意: このコマンドはフォアグラウンドで実行されます"
	@echo "[INFO] 別々のターミナルで 'make backend' と 'make frontend' を実行することをお勧めします"
	@echo ""
	@echo "バックエンド: http://localhost:8000"
	@echo "フロントエンド: http://localhost:5173"
	@echo ""
	@echo "続行しますか? (Ctrl+C でキャンセル)"
	@read -p "Press Enter to continue..."
	@make backend &
	@make frontend

# Start backend only
backend:
	@echo "[INFO] バックエンドを起動します..."
	@echo "[INFO] URL: http://localhost:8000"
	@echo "[INFO] API Docs: http://localhost:8000/docs"
	cd backend && \
	. venv/bin/activate && \
	uvicorn main:app --reload

# Start frontend only
frontend:
	@echo "[INFO] フロントエンドを起動します..."
	@echo "[INFO] URL: http://localhost:5173"
	cd frontend && npm run dev

# Run tests
test:
	@echo "[INFO] テストを実行します..."
	cd backend && \
	. venv/bin/activate && \
	pytest tests/ -v
	@echo "[INFO] テスト完了！"

# Lint code
lint:
	@echo "[INFO] コード品質チェックを実行します..."
	@echo "[INFO] バックエンドをチェック中..."
	cd backend && \
	. venv/bin/activate && \
	flake8 app/ --max-line-length=100 || echo "[WARNING] flake8がインストールされていません"
	@echo "[INFO] フロントエンドをチェック中..."
	cd frontend && npm run lint || echo "[INFO] lint scriptが見つかりません"
	@echo "[INFO] チェック完了！"

# Clean cache and temp files
clean:
	@echo "[INFO] キャッシュと一時ファイルを削除します..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "[INFO] クリーンアップ完了！"

# Show database setup guide
db-setup:
	@echo "[INFO] データベースセットアップガイド"
	@echo ""
	@echo "1. https://supabase.com でプロジェクトを作成"
	@echo "2. SQL Editorで database/schema.sql を実行"
	@echo "3. (オプション) database/sample_data.sql を実行してテストデータを作成"
	@echo "4. Settings > API でプロジェクトURLとAPIキーを取得"
	@echo "5. backend/.env に以下を設定:"
	@echo "   SUPABASE_URL=your_project_url"
	@echo "   SUPABASE_KEY=your_anon_key"
	@echo ""
	@echo "詳細: docs/supabase_setup.md を参照"

# Install dependencies
install:
	@echo "[INFO] 依存関係をインストールします..."
	cd backend && . venv/bin/activate && pip install -r requirements.txt
	cd frontend && npm install
	@echo "[INFO] インストール完了！"

# Run backend tests with coverage
test-coverage:
	@echo "[INFO] カバレッジ付きでテストを実行します..."
	cd backend && \
	. venv/bin/activate && \
	pytest tests/ --cov=app --cov-report=html
	@echo "[INFO] カバレッジレポート: backend/htmlcov/index.html"

# Format code
format:
	@echo "[INFO] コードをフォーマットします..."
	cd backend && \
	. venv/bin/activate && \
	black app/ tests/ || echo "[WARNING] blackがインストールされていません"
	cd frontend && \
	npx prettier --write src/ || echo "[INFO] prettierが見つかりません"
	@echo "[INFO] フォーマット完了！"
