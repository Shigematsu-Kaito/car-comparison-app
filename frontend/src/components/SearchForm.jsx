import { useState } from 'react'

export default function SearchForm({ onSearch, loading }) {
    const [formData, setFormData] = useState({
        make: '',
        model: '',
        year_min: '',
        year_max: '',
        price_min: '',
        price_max: '',
        mileage_max: '',
        fuel_type: '',
        transmission: '',
    })

    const handleSubmit = (e) => {
        e.preventDefault()

        // 空の値を除外
        const searchParams = Object.fromEntries(
            Object.entries(formData).filter(([_, value]) => value !== '')
        )

        onSearch(searchParams)
    }

    const handleChange = (e) => {
        const { name, value } = e.target
        setFormData(prev => ({ ...prev, [name]: value }))
    }

    return (
        <form onSubmit={handleSubmit} className="bg-card p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold mb-4">検索条件</h2>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {/* メーカー */}
                <div>
                    <label className="block text-sm font-medium mb-1">メーカー</label>
                    <input
                        type="text"
                        name="make"
                        value={formData.make}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                        placeholder="例: トヨタ"
                    />
                </div>

                {/* 車種 */}
                <div>
                    <label className="block text-sm font-medium mb-1">車種</label>
                    <input
                        type="text"
                        name="model"
                        value={formData.model}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                        placeholder="例: プリウス"
                    />
                </div>

                {/* 年式（最小） */}
                <div>
                    <label className="block text-sm font-medium mb-1">年式（最小）</label>
                    <input
                        type="number"
                        name="year_min"
                        value={formData.year_min}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                        placeholder="2015"
                    />
                </div>

                {/* 年式（最大） */}
                <div>
                    <label className="block text-sm font-medium mb-1">年式（最大）</label>
                    <input
                        type="number"
                        name="year_max"
                        value={formData.year_max}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                        placeholder="2023"
                    />
                </div>

                {/* 価格（最小） */}
                <div>
                    <label className="block text-sm font-medium mb-1">価格（最小・円）</label>
                    <input
                        type="number"
                        name="price_min"
                        value={formData.price_min}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                        placeholder="1000000"
                    />
                </div>

                {/* 価格（最大） */}
                <div>
                    <label className="block text-sm font-medium mb-1">価格（最大・円）</label>
                    <input
                        type="number"
                        name="price_max"
                        value={formData.price_max}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                        placeholder="3000000"
                    />
                </div>

                {/* 走行距離（最大） */}
                <div>
                    <label className="block text-sm font-medium mb-1">走行距離（最大・km）</label>
                    <input
                        type="number"
                        name="mileage_max"
                        value={formData.mileage_max}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                        placeholder="50000"
                    />
                </div>

                {/* 燃料タイプ */}
                <div>
                    <label className="block text-sm font-medium mb-1">燃料タイプ</label>
                    <select
                        name="fuel_type"
                        value={formData.fuel_type}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                    >
                        <option value="">指定なし</option>
                        <option value="ガソリン">ガソリン</option>
                        <option value="ハイブリッド">ハイブリッド</option>
                        <option value="ディーゼル">ディーゼル</option>
                        <option value="電気">電気</option>
                    </select>
                </div>

                {/* トランスミッション */}
                <div>
                    <label className="block text-sm font-medium mb-1">トランスミッション</label>
                    <select
                        name="transmission"
                        value={formData.transmission}
                        onChange={handleChange}
                        className="w-full px-3 py-2 border rounded"
                    >
                        <option value="">指定なし</option>
                        <option value="AT">AT</option>
                        <option value="MT">MT</option>
                        <option value="CVT">CVT</option>
                    </select>
                </div>
            </div>

            <div className="mt-6">
                <button
                    type="submit"
                    disabled={loading}
                    className="w-full px-6 py-3 bg-primary text-primary-foreground rounded font-semibold hover:opacity-90 disabled:opacity-50"
                >
                    {loading ? '検索中...' : '検索する'}
                </button>
            </div>
        </form>
    )
}
