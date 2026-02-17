from app.core.database import get_db


def get_database():
    """データベース接続を取得（依存性注入用）"""
    return get_db()
