import { useState, useEffect } from 'react'
import { getWatchList, addToWatchListApi, deleteFromWatchList } from '../services/api'

const USER_ID = 'default-user' // 実際の実装では認証から取得

export function useWatchList() {
    const [watchList, setWatchList] = useState([])
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    // ローカルストレージから読み込み（APIが利用できない場合のフォールバック）
    useEffect(() => {
        const savedList = localStorage.getItem('watchList')
        if (savedList) {
            try {
                setWatchList(JSON.parse(savedList))
            } catch (e) {
                console.error('Failed to parse watchlist from localStorage', e)
            }
        }
    }, [])

    // ローカルストレージに保存
    useEffect(() => {
        localStorage.setItem('watchList', JSON.stringify(watchList))
    }, [watchList])

    const addToWatchList = async (car) => {
        // ローカルに即座に追加
        const newItem = {
            id: `local-${Date.now()}`,
            car,
            notes: '',
            created_at: new Date().toISOString(),
        }
        setWatchList(prev => [...prev, newItem])

        // APIに送信（オプション）
        try {
            // await addToWatchListApi(USER_ID, { car_id: car.id })
        } catch (err) {
            console.error('Failed to sync with API', err)
        }
    }

    const removeFromWatchList = async (itemId) => {
        // ローカルから削除
        setWatchList(prev => prev.filter(item => item.id !== itemId))

        // APIから削除（オプション）
        try {
            // await deleteFromWatchList(itemId)
        } catch (err) {
            console.error('Failed to delete from API', err)
        }
    }

    const fetchWatchList = async () => {
        setLoading(true)
        setError(null)

        try {
            const items = await getWatchList(USER_ID)
            setWatchList(items)
        } catch (err) {
            setError(err.message || '検討リストの取得に失敗しました')
        } finally {
            setLoading(false)
        }
    }

    return {
        watchList,
        loading,
        error,
        addToWatchList,
        removeFromWatchList,
        fetchWatchList,
    }
}
