export default function ComparisonGrid({ cars }) {
    if (cars.length === 0) {
        return (
            <div className="text-center py-12">
                <p className="text-muted-foreground">比較する車を選択してください</p>
            </div>
        )
    }

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

    const attributes = [
        { label: 'メーカー', key: 'make' },
        { label: '車種', key: 'model' },
        { label: '年式', key: 'year', format: (v) => `${v}年` },
        { label: '価格', key: 'price', format: formatPrice },
        { label: '走行距離', key: 'mileage', format: formatMileage },
        { label: '色', key: 'color' },
        { label: '燃料', key: 'fuel_type' },
        { label: '変速機', key: 'transmission' },
        { label: '所在地', key: 'location' },
        { label: '情報源', key: 'source' },
    ]

    return (
        <div className="bg-card rounded-lg shadow overflow-x-auto">
            <table className="w-full">
                <thead>
                    <tr className="border-b">
                        <th className="p-4 text-left font-semibold bg-muted">項目</th>
                        {cars.map((car, index) => (
                            <th key={index} className="p-4 text-left font-semibold min-w-[200px]">
                                {car.make} {car.model}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {attributes.map((attr, index) => (
                        <tr key={attr.key} className={index % 2 === 0 ? 'bg-muted/50' : ''}>
                            <td className="p-4 font-medium">{attr.label}</td>
                            {cars.map((car, carIndex) => {
                                const value = car[attr.key]
                                const displayValue = value
                                    ? (attr.format ? attr.format(value) : value)
                                    : '-'

                                return (
                                    <td key={carIndex} className="p-4">
                                        {displayValue}
                                    </td>
                                )
                            })}
                        </tr>
                    ))}
                    <tr>
                        <td className="p-4 font-medium">詳細</td>
                        {cars.map((car, index) => (
                            <td key={index} className="p-4">
                                {car.url && (
                                    <a
                                        href={car.url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="text-primary hover:underline text-sm"
                                    >
                                        詳細を見る →
                                    </a>
                                )}
                            </td>
                        ))}
                    </tr>
                </tbody>
            </table>
        </div>
    )
}
