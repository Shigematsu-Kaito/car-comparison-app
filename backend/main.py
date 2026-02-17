from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import search, watchlist

app = FastAPI(
    title=settings.APP_NAME,
    description="中古車比較アプリケーションAPI",
    version="1.0.0"
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(search.router, prefix="/api", tags=["search"])
app.include_router(watchlist.router, prefix="/api", tags=["watchlist"])


@app.get("/")
async def root():
    """ヘルスチェック"""
    return {"status": "ok", "message": "中古車比較API稼働中"}


@app.get("/health")
async def health():
    """ヘルスチェック"""
    return {"status": "healthy"}
