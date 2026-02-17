export default function WatchList({ items, onRemove }) {
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

    if (items.length === 0) {
        return (
            <div className="text-center py-12">
                <p className="text-muted-foreground">検討リストは空です</p>
            </div>
        )
    }

    return (
        <div className="space-y-4">
            <h2 className="text-2xl font-bold">検討リスト</h2>

            {items.map((item) => {
                const car = item.car || item
                return (
                    <div key={item.id} className="bg-card border rounded-lg p-4 flex gap-4">
                        {/* 画像 */}
                        <div className="w-48 h-32 bg-muted rounded flex-shrink-0 flex items-center justify-center">
                            {car.image_url ? (
                                <img src={car.image_url} alt={`${car.make} ${car.model}`} className="w-full h-full object-cover rounded" />
                            ) : (
                                <span className="text-muted-foreground text-sm">画像なし</span>
                            )}
                        </div>

                        {/* 情報 */}
                        <div className="flex-1">
                            <div className="flex items-start justify-between">
                                <div>
                                    <h3 className="font-semibold text-lg">{car.make} {car.model}</h3>
                                    <p className="text-sm text-muted-foreground">{car.year}年式</p>
                                </div>
                                <span className="text-xs bg-secondary px-2 py-1 rounded">{car.source}</span>
                            </div>

                            <div className="mt-2 grid grid-cols-2 md:grid-cols-3 gap-2 text-sm">
                                <div>
                                    <span className="text-muted-foreground">価格: </span>
                                    <span className="font-semibold text-primary">{formatPrice(car.price)}</span>
                                </div>
                                <div>
                                    <span className="text-muted-foreground">走行距離: </span>
                                    <span>{formatMileage(car.mileage)}</span>
                                </div>
                                {car.color && (
                                    <div>
                                        <span className="text-muted-foreground">色: </span>
                                        <span>{car.color}</span>
                                    </div>
                                )}
                                {car.fuel_type && (
                                    <div>
                                        <span className="text-muted-foreground">燃料: </span>
                                        <span>{car.fuel_type}</span>
                                    </div>
                                )}
                                {car.transmission && (
                                    <div>
                                        <span className="text-muted-foreground">変速: </span>
                                        <span>{car.transmission}</span>
                                    </div>
                                )}
                                {car.location && (
                                    <div>
                                        <span className="text-muted-foreground">所在地: </span>
                                        <span>{car.location}</span>
                                    </div>
                                )}
                            </div>

                            {item.notes && (
                                <div className="mt-2 p-2 bg-muted rounded">
                                    <p className="text-sm"><strong>メモ:</strong> {item.notes}</p>
                                </div>
                            )}

                            <div className="mt-3 flex gap-2">
                                {car.url && (
                                    <a
                                        href={car.url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="px-4 py-2 bg-primary text-primary-foreground rounded text-sm font-medium hover:opacity-90"
                                    >
                                        詳細を見る
                                    </a>
                                )}
                                <button
                                    onClick={() => onRemove(item.id)}
                                    className="px-4 py-2 bg-destructive text-destructive-foreground rounded text-sm font-medium hover:opacity-90"
                                >
                                    削除
                                </button>
                            </div>
                        </div>
                    </div>
                )
            })}
        </div>
    )
}
