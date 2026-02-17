import re
from typing import Optional


def normalize_make(make: str) -> str:
    """
    メーカー名を正規化
    
    例: 「トヨタ」「TOYOTA」「toyota」 -> 「トヨタ」
    """
    make_mapping = {
        'toyota': 'トヨタ',
        'honda': 'ホンダ',
        'nissan': '日産',
        'mazda': 'マツダ',
        'subaru': 'スバル',
        'suzuki': 'スズキ',
        'daihatsu': 'ダイハツ',
        'mitsubishi': '三菱',
        # 必要に応じて追加
    }
    
    normalized = make.lower().strip()
    return make_mapping.get(normalized, make)


def normalize_model(model: str) -> str:
    """
    車種名を正規化
    
    例: 「プリウス」「PRIUS」「prius」 -> 「プリウス」
    """
    return model.strip()


def normalize_fuel_type(fuel_type: str) -> Optional[str]:
    """
    燃料タイプを正規化
    
    例: 「ガソリン」「レギュラー」 -> 「ガソリン」
    """
    fuel_mapping = {
        'ガソリン': 'ガソリン',
        'レギュラー': 'ガソリン',
        'ハイオク': 'ハイオク',
        'ディーゼル': 'ディーゼル',
        '軽油': 'ディーゼル',
        'ハイブリッド': 'ハイブリッド',
        'HV': 'ハイブリッド',
        '電気': '電気',
        'EV': '電気',
        'PHV': 'プラグインハイブリッド',
        'PHEV': 'プラグインハイブリッド',
    }
    
    normalized = fuel_type.strip()
    return fuel_mapping.get(normalized, fuel_type)


def normalize_transmission(transmission: str) -> Optional[str]:
    """
    トランスミッションを正規化
    
    例: 「AT」「オートマ」 -> 「AT」
    """
    trans_mapping = {
        'オートマ': 'AT',
        'オートマチック': 'AT',
        'A/T': 'AT',
        'AT': 'AT',
        'マニュアル': 'MT',
        'M/T': 'MT',
        'MT': 'MT',
        'CVT': 'CVT',
    }
    
    normalized = transmission.strip()
    return trans_mapping.get(normalized, transmission)


def extract_year_from_text(text: str) -> Optional[int]:
    """
    テキストから年式を抽出
    
    例: 「2020年」「平成32年」 -> 2020
    """
    # 西暦の抽出
    match = re.search(r'(\d{4})年', text)
    if match:
        return int(match.group(1))
    
    # 平成の変換（必要に応じて）
    heisei_match = re.search(r'平成(\d+)年', text)
    if heisei_match:
        heisei_year = int(heisei_match.group(1))
        return 1988 + heisei_year
    
    return None


def format_price(price: int) -> str:
    """
    価格をフォーマット
    
    例: 1234567 -> "123.5万円"
    """
    if price >= 10000:
        man = price / 10000
        return f"{man:.1f}万円"
    return f"{price}円"


def format_mileage(mileage: int) -> str:
    """
    走行距離をフォーマット
    
    例: 12345 -> "1.2万km"
    """
    if mileage >= 10000:
        man = mileage / 10000
        return f"{man:.1f}万km"
    return f"{mileage}km"
