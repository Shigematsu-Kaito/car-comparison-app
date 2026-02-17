#!/bin/bash
# Development Helper Script
# このスクリプトは開発を効率化するための便利なコマンドを提供します

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Show help
show_help() {
    echo "中古車比較アプリ - 開発ヘルパースクリプト"
    echo ""
    echo "使用方法: ./dev.sh [command]"
    echo ""
    echo "利用可能なコマンド:"
    echo "  setup           - 初回セットアップを実行"
    echo "  start           - バックエンドとフロントエンドを起動"
    echo "  backend         - バックエンドのみ起動"
    echo "  frontend        - フロントエンドのみ起動"
    echo "  test            - テストを実行"
    echo "  lint            - コード品質チェック"
    echo "  clean           - キャッシュと一時ファイルを削除"
    echo "  db-setup        - データベースセットアップガイドを表示"
    echo "  help            - このヘルプメッセージを表示"
    echo ""
}

# Initial setup
setup() {
    print_info "初回セットアップを開始します..."
    
    # Backend setup
    print_info "バックエンドのセットアップ..."
    cd backend
    if [ ! -d "venv" ]; then
        python -m venv venv
        print_info "仮想環境を作成しました"
    fi
    
    source venv/bin/activate || . venv/Scripts/activate
    pip install -r requirements.txt
    
    if [ ! -f ".env" ]; then
        cp .env.example .env
        print_warning ".envファイルを作成しました。Supabase接続情報を設定してください！"
    fi
    
    cd ..
    
    # Frontend setup
    print_info "フロントエンドのセットアップ..."
    cd frontend
    npm install
    
    if [ ! -f ".env" ]; then
        cp .env.example .env
        print_info ".envファイルを作成しました"
    fi
    
    cd ..
    
    print_info "セットアップ完了！"
    print_info "次のステップ: ./dev.sh db-setup でデータベースをセットアップしてください"
}

# Start both servers
start() {
    print_info "バックエンドとフロントエンドを起動します..."
    print_info "バックエンド: http://localhost:8000"
    print_info "フロントエンド: http://localhost:5173"
    print_warning "Ctrl+C で停止します"
    
    # Start backend in background
    cd backend
    source venv/bin/activate || . venv/Scripts/activate
    uvicorn main:app --reload &
    BACKEND_PID=$!
    cd ..
    
    # Start frontend in background
    cd frontend
    npm run dev &
    FRONTEND_PID=$!
    cd ..
    
    # Wait for Ctrl+C
    trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
    wait
}

# Start backend only
backend() {
    print_info "バックエンドを起動します..."
    print_info "URL: http://localhost:8000"
    print_info "API Docs: http://localhost:8000/docs"
    
    cd backend
    source venv/bin/activate || . venv/Scripts/activate
    uvicorn main:app --reload
}

# Start frontend only
frontend() {
    print_info "フロントエンドを起動します..."
    print_info "URL: http://localhost:5173"
    
    cd frontend
    npm run dev
}

# Run tests
test() {
    print_info "テストを実行します..."
    
    cd backend
    source venv/bin/activate || . venv/Scripts/activate
    pytest tests/ -v
    cd ..
    
    print_info "テスト完了！"
}

# Lint code
lint() {
    print_info "コード品質チェックを実行します..."
    
    # Backend
    print_info "バックエンドをチェック中..."
    cd backend
    source venv/bin/activate || . venv/Scripts/activate
    
    if command -v flake8 &> /dev/null; then
        flake8 app/ --max-line-length=100
    else
        print_warning "flake8がインストールされていません。pip install flake8 でインストールしてください"
    fi
    
    cd ..
    
    # Frontend
    print_info "フロントエンドをチェック中..."
    cd frontend
    npm run lint
    cd ..
    
    print_info "チェック完了！"
}

# Clean cache and temp files
clean() {
    print_info "キャッシュと一時ファイルを削除します..."
    
    # Python cache
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    
    # Node modules (optional)
    # rm -rf frontend/node_modules
    
    print_info "クリーンアップ完了！"
}

# Show database setup guide
db_setup() {
    print_info "データベースセットアップガイド"
    echo ""
    echo "1. https://supabase.com でプロジェクトを作成"
    echo "2. SQL Editorで database/schema.sql を実行"
    echo "3. (オプション) database/sample_data.sql を実行してテストデータを作成"
    echo "4. Settings > API でプロジェクトURLとAPIキーを取得"
    echo "5. backend/.env に以下を設定:"
    echo "   SUPABASE_URL=your_project_url"
    echo "   SUPABASE_KEY=your_anon_key"
    echo ""
    echo "詳細: docs/supabase_setup.md を参照"
}

# Main
case "$1" in
    setup)
        setup
        ;;
    start)
        start
        ;;
    backend)
        backend
        ;;
    frontend)
        frontend
        ;;
    test)
        test
        ;;
    lint)
        lint
        ;;
    clean)
        clean
        ;;
    db-setup)
        db_setup
        ;;
    help|--help|-h|"")
        show_help
        ;;
    *)
        print_error "不明なコマンド: $1"
        show_help
        exit 1
        ;;
esac
