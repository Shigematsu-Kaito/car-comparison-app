-- サンプルデータ投入用SQL
-- Supabaseのセットアップ後、このファイルを実行してテストデータを作成します

-- サンプル中古車データ
INSERT INTO cars (source, make, model, year, price, mileage, color, fuel_type, transmission, location, url, image_url, description)
VALUES
    (
        'carsensor',
        'Toyota',
        'Prius',
        2020,
        2500000,
        30000,
        'White',
        'Hybrid',
        'CVT',
        'Tokyo',
        'https://example.com/car/1',
        'https://via.placeholder.com/400x300?text=Toyota+Prius',
        'Clean and well-maintained hybrid vehicle. Perfect for city driving.'
    ),
    (
        'goonet',
        'Honda',
        'Fit',
        2019,
        1800000,
        45000,
        'Blue',
        'Gasoline',
        'CVT',
        'Osaka',
        'https://example.com/car/2',
        'https://via.placeholder.com/400x300?text=Honda+Fit',
        'Compact car with excellent fuel efficiency. One owner, no accidents.'
    ),
    (
        'gulliver',
        'Nissan',
        'Note',
        2021,
        2200000,
        15000,
        'Red',
        'Electric',
        'AT',
        'Yokohama',
        'https://example.com/car/3',
        'https://via.placeholder.com/400x300?text=Nissan+Note',
        'Electric vehicle with low mileage. Includes charging cable.'
    ),
    (
        'carsensor',
        'Toyota',
        'Corolla',
        2018,
        1500000,
        60000,
        'Black',
        'Gasoline',
        'CVT',
        'Nagoya',
        'https://example.com/car/4',
        'https://via.placeholder.com/400x300?text=Toyota+Corolla',
        'Reliable sedan, great for families. Regular maintenance records available.'
    ),
    (
        'goonet',
        'Mazda',
        'CX-5',
        2020,
        3200000,
        25000,
        'Silver',
        'Diesel',
        'AT',
        'Fukuoka',
        'https://example.com/car/5',
        'https://via.placeholder.com/400x300?text=Mazda+CX-5',
        'Popular SUV with diesel engine. Spacious interior and modern features.'
    ),
    (
        'gulliver',
        'Honda',
        'Civic',
        2019,
        2000000,
        40000,
        'White',
        'Gasoline',
        'MT',
        'Sapporo',
        'https://example.com/car/6',
        'https://via.placeholder.com/400x300?text=Honda+Civic',
        'Sport sedan with manual transmission. Great handling and performance.'
    );

-- データ確認用クエリ
-- SELECT * FROM cars ORDER BY created_at DESC;

-- メーカー別集計
-- SELECT make, COUNT(*) as count, AVG(price) as avg_price
-- FROM cars
-- GROUP BY make
-- ORDER BY count DESC;

-- 価格帯別集計
-- SELECT 
--     CASE 
--         WHEN price < 2000000 THEN 'Under 2M'
--         WHEN price < 3000000 THEN '2M-3M'
--         ELSE 'Over 3M'
--     END as price_range,
--     COUNT(*) as count
-- FROM cars
-- GROUP BY price_range
-- ORDER BY price_range;
