@echo off
REM Development Helper Script for Windows
REM このスクリプトは開発を効率化するための便利なコマンドを提供します

setlocal enabledelayedexpansion

REM Show help
if "%1"=="" goto :help
if "%1"=="help" goto :help
if "%1"=="--help" goto :help
if "%1"=="-h" goto :help

if "%1"=="setup" goto :setup
if "%1"=="start" goto :start
if "%1"=="backend" goto :backend
if "%1"=="frontend" goto :frontend
if "%1"=="test" goto :test
if "%1"=="clean" goto :clean
if "%1"=="db-setup" goto :db_setup

echo [ERROR] 不明なコマンド: %1
goto :help

:help
echo 中古車比較アプリ - 開発ヘルパースクリプト
echo.
echo 使用方法: dev.bat [command]
echo.
echo 利用可能なコマンド:
echo   setup           - 初回セットアップを実行
echo   start           - バックエンドとフロントエンドを起動
echo   backend         - バックエンドのみ起動
echo   frontend        - フロントエンドのみ起動
echo   test            - テストを実行
echo   clean           - キャッシュと一時ファイルを削除
echo   db-setup        - データベースセットアップガイドを表示
echo   help            - このヘルプメッセージを表示
echo.
goto :eof

:setup
echo [INFO] 初回セットアップを開始します...

REM Backend setup
echo [INFO] バックエンドのセットアップ...
cd backend

if not exist "venv" (
    python -m venv venv
    echo [INFO] 仮想環境を作成しました
)

call venv\Scripts\activate.bat
pip install -r requirements.txt

if not exist ".env" (
    copy .env.example .env
    echo [WARNING] .envファイルを作成しました。Supabase接続情報を設定してください！
)

cd ..

REM Frontend setup
echo [INFO] フロントエンドのセットアップ...
cd frontend
call npm install

if not exist ".env" (
    copy .env.example .env
    echo [INFO] .envファイルを作成しました
)

cd ..

echo [INFO] セットアップ完了！
echo [INFO] 次のステップ: dev.bat db-setup でデータベースをセットアップしてください
goto :eof

:start
echo [INFO] バックエンドとフロントエンドを起動します...
echo [INFO] バックエンド: http://localhost:8000
echo [INFO] フロントエンド: http://localhost:5173
echo.
echo 新しいターミナルウィンドウが開きます
echo Ctrl+C で各ウィンドウを停止してください
echo.

REM Start backend in new window
start "Backend Server" cmd /k "cd backend && venv\Scripts\activate && uvicorn main:app --reload"

REM Wait a bit
timeout /t 2 /nobreak >nul

REM Start frontend in new window
start "Frontend Server" cmd /k "cd frontend && npm run dev"

echo [INFO] サーバーを起動しました！
goto :eof

:backend
echo [INFO] バックエンドを起動します...
echo [INFO] URL: http://localhost:8000
echo [INFO] API Docs: http://localhost:8000/docs
cd backend
call venv\Scripts\activate.bat
uvicorn main:app --reload
cd ..
goto :eof

:frontend
echo [INFO] フロントエンドを起動します...
echo [INFO] URL: http://localhost:5173
cd frontend
call npm run dev
cd ..
goto :eof

:test
echo [INFO] テストを実行します...
cd backend
call venv\Scripts\activate.bat
pytest tests/ -v
cd ..
echo [INFO] テスト完了！
goto :eof

:clean
echo [INFO] キャッシュと一時ファイルを削除します...

REM Python cache
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
for /d /r . %%d in (.pytest_cache) do @if exist "%%d" rd /s /q "%%d"
del /s /q *.pyc >nul 2>&1

echo [INFO] クリーンアップ完了！
goto :eof

:db_setup
echo [INFO] データベースセットアップガイド
echo.
echo 1. https://supabase.com でプロジェクトを作成
echo 2. SQL Editorで database/schema.sql を実行
echo 3. (オプション) database/sample_data.sql を実行してテストデータを作成
echo 4. Settings ^> API でプロジェクトURLとAPIキーを取得
echo 5. backend/.env に以下を設定:
echo    SUPABASE_URL=your_project_url
echo    SUPABASE_KEY=your_anon_key
echo.
echo 詳細: docs/supabase_setup.md を参照
goto :eof

:eof
endlocal
