import { useState } from 'react'
import SearchForm from './components/SearchForm'
import CarCard from './components/CarCard'
import ComparisonGrid from './components/ComparisonGrid'
import WatchList from './components/WatchList'
import { useCarSearch } from './hooks/useCarSearch'
import { useWatchList } from './hooks/useWatchList'

function App() {
    const [view, setView] = useState('search') // 'search' | 'comparison' | 'watchlist'
    const { cars, loading, error, searchCars } = useCarSearch()
    const { watchList, addToWatchList, removeFromWatchList } = useWatchList()
    const [selectedCars, setSelectedCars] = useState([])

    const handleSearch = async (searchParams) => {
        await searchCars(searchParams)
    }

    const handleCarSelect = (car) => {
        if (selectedCars.find(c => c.id === car.id)) {
            setSelectedCars(selectedCars.filter(c => c.id !== car.id))
        } else {
            setSelectedCars([...selectedCars, car])
        }
    }

    return (
        <div className="min-h-screen bg-background">
            {/* Header */}
            <header className="border-b">
                <div className="container mx-auto px-4 py-4">
                    <h1 className="text-2xl font-bold">中古車比較アプリ</h1>
                    <nav className="flex gap-4 mt-4">
                        <button
                            onClick={() => setView('search')}
                            className={`px-4 py-2 rounded ${view === 'search' ? 'bg-primary text-primary-foreground' : 'bg-secondary'}`}
                        >
                            検索
                        </button>
                        <button
                            onClick={() => setView('comparison')}
                            className={`px-4 py-2 rounded ${view === 'comparison' ? 'bg-primary text-primary-foreground' : 'bg-secondary'}`}
                            disabled={selectedCars.length === 0}
                        >
                            比較 ({selectedCars.length})
                        </button>
                        <button
                            onClick={() => setView('watchlist')}
                            className={`px-4 py-2 rounded ${view === 'watchlist' ? 'bg-primary text-primary-foreground' : 'bg-secondary'}`}
                        >
                            検討リスト ({watchList.length})
                        </button>
                    </nav>
                </div>
            </header>

            {/* Main Content */}
            <main className="container mx-auto px-4 py-8">
                {view === 'search' && (
                    <div>
                        <SearchForm onSearch={handleSearch} loading={loading} />

                        {error && (
                            <div className="mt-4 p-4 bg-destructive/10 text-destructive rounded">
                                エラー: {error}
                            </div>
                        )}

                        <div className="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            {cars.map((car) => (
                                <CarCard
                                    key={car.id}
                                    car={car}
                                    onSelect={() => handleCarSelect(car)}
                                    isSelected={selectedCars.some(c => c.id === car.id)}
                                    onAddToWatchList={() => addToWatchList(car)}
                                />
                            ))}
                        </div>
                    </div>
                )}

                {view === 'comparison' && (
                    <ComparisonGrid cars={selectedCars} />
                )}

                {view === 'watchlist' && (
                    <WatchList
                        items={watchList}
                        onRemove={removeFromWatchList}
                    />
                )}
            </main>
        </div>
    )
}

export default App
