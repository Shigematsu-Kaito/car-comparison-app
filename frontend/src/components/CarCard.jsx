export default function CarCard({ car, onSelect, isSelected, onAddToWatchList }) {
    const formatPrice = (price) => {
        if (price >= 10000) {
            return `${(price / 10000).toFixed(1)}万円`
        }
        return `${price}円`
    }

    const formatMileage = (mileage) => {
        if (mileage >= 10000) {
            return `${(mileage / 10000).toFixed(1)}万km`
        }
        return `${mileage}km`
    }

    return (
        <div className={`bg-card border rounded-lg overflow-hidden shadow hover:shadow-lg transition ${isSelected ? 'ring-2 ring-primary' : ''}`}>
            {/* 画像 */}
            <div className="aspect-video bg-muted flex items-center justify-center">
                {car.image_url ? (
                    <img src={car.image_url} alt={`${car.make} ${car.model}`} className="w-full h-full object-cover" />
                ) : (
                    <span className="text-muted-foreground">画像なし</span>
                )}
            </div>

            {/* 情報 */}
            <div className="p-4">
                <div className="flex items-start justify-between mb-2">
                    <div>
                        <h3 className="font-semibold text-lg">{car.make} {car.model}</h3>
                        <p className="text-sm text-muted-foreground">{car.year}年式</p>
                    </div>
                    <span className="text-xs bg-secondary px-2 py-1 rounded">{car.source}</span>
                </div>

                <div className="space-y-1 text-sm mb-4">
                    <p className="text-xl font-bold text-primary">{formatPrice(car.price)}</p>
                    <p className="text-muted-foreground">走行距離: {formatMileage(car.mileage)}</p>
                    {car.color && <p className="text-muted-foreground">色: {car.color}</p>}
                    {car.fuel_type && <p className="text-muted-foreground">燃料: {car.fuel_type}</p>}
                    {car.transmission && <p className="text-muted-foreground">変速: {car.transmission}</p>}
                    {car.location && <p className="text-muted-foreground">所在地: {car.location}</p>}
                </div>

                {/* アクション */}
                <div className="flex gap-2">
                    <button
                        onClick={onSelect}
                        className={`flex-1 px-3 py-2 rounded text-sm font-medium ${isSelected
                                ? 'bg-primary text-primary-foreground'
                                : 'bg-secondary hover:bg-secondary/80'
                            }`}
                    >
                        {isSelected ? '選択中' : '比較に追加'}
                    </button>
                    <button
                        onClick={onAddToWatchList}
                        className="px-3 py-2 bg-accent text-accent-foreground rounded text-sm font-medium hover:opacity-90"
                    >
                        検討リスト
                    </button>
                </div>

                {/* 詳細リンク */}
                {car.url && (
                    <a
                        href={car.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="block mt-2 text-sm text-primary hover:underline text-center"
                    >
                        詳細を見る →
                    </a>
                )}
            </div>
        </div>
    )
}
