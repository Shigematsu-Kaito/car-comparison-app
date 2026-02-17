from supabase import create_client, Client
from app.core.config import settings


class Database:
    """Supabaseデータベース接続管理"""
    
    _client: Client = None
    
    @classmethod
    def get_client(cls) -> Client:
        """Supabaseクライアントを取得"""
        if cls._client is None:
            cls._client = create_client(
                settings.SUPABASE_URL,
                settings.SUPABASE_KEY
            )
        return cls._client
    
    @classmethod
    def close(cls):
        """接続をクローズ"""
        cls._client = None


def get_db() -> Client:
    """依存性注入用のデータベース接続取得関数"""
    return Database.get_client()
