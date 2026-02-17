from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """アプリケーション設定"""
    
    # Supabase設定
    SUPABASE_URL: str
    SUPABASE_KEY: str
    
    # アプリケーション設定
    APP_NAME: str = "中古車比較アプリ"
    DEBUG: bool = False
    CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    # スクレイピング設定
    REQUEST_TIMEOUT: int = 30
    MAX_RETRY: int = 3
    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
