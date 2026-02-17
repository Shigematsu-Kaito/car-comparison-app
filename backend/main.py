from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import search, watchlist

app = FastAPI(
    title=settings.APP_NAME,
    description="Used Car Comparison Application API",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(search.router, prefix="/api", tags=["search"])
app.include_router(watchlist.router, prefix="/api", tags=["watchlist"])


@app.get("/")
async def root():
    """Health check"""
    return {"status": "ok", "message": "Used Car Comparison API is running"}


@app.get("/health")
async def health():
    """Health check"""
    return {"status": "healthy"}
