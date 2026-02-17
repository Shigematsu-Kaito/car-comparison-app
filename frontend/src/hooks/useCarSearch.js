import { useState } from 'react'
import { searchCars } from '../services/api'

export function useCarSearch() {
    const [cars, setCars] = useState([])
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const search = async (searchParams) => {
        setLoading(true)
        setError(null)

        try {
            const results = await searchCars(searchParams)
            setCars(results)
        } catch (err) {
            setError(err.message || '検索に失敗しました')
            setCars([])
        } finally {
            setLoading(false)
        }
    }

    return {
        cars,
        loading,
        error,
        searchCars: search,
    }
}
