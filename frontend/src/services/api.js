import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
})

// 車検索
export async function searchCars(searchParams) {
    try {
        const response = await api.post('/api/search', searchParams)
        return response.data
    } catch (error) {
        throw new Error(error.response?.data?.detail || '検索に失敗しました')
    }
}

// 車情報取得
export async function getCars(skip = 0, limit = 100) {
    try {
        const response = await api.get('/api/cars', { params: { skip, limit } })
        return response.data
    } catch (error) {
        throw new Error(error.response?.data?.detail || '取得に失敗しました')
    }
}

// 特定の車情報取得
export async function getCar(carId) {
    try {
        const response = await api.get(`/api/cars/${carId}`)
        return response.data
    } catch (error) {
        throw new Error(error.response?.data?.detail || '取得に失敗しました')
    }
}

// 検討リスト取得
export async function getWatchList(userId) {
    try {
        const response = await api.get(`/api/watchlist/${userId}`)
        return response.data
    } catch (error) {
        throw new Error(error.response?.data?.detail || '検討リスト取得に失敗しました')
    }
}

// 検討リストに追加
export async function addToWatchListApi(userId, item) {
    try {
        const response = await api.post(`/api/watchlist/${userId}`, item)
        return response.data
    } catch (error) {
        throw new Error(error.response?.data?.detail || '検討リスト追加に失敗しました')
    }
}

// 検討リストアイテム更新
export async function updateWatchListItem(itemId, item) {
    try {
        const response = await api.put(`/api/watchlist/${itemId}`, item)
        return response.data
    } catch (error) {
        throw new Error(error.response?.data?.detail || '検討リスト更新に失敗しました')
    }
}

// 検討リストから削除
export async function deleteFromWatchList(itemId) {
    try {
        const response = await api.delete(`/api/watchlist/${itemId}`)
        return response.data
    } catch (error) {
        throw new Error(error.response?.data?.detail || '検討リスト削除に失敗しました')
    }
}

export default api
