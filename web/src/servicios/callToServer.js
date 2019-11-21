//import { URL } from 'url'
import fetch from 'node-fetch'

let urlBase = 'http://192.168.100.236:5000'
urlBase = 'http://localhost:5000'
urlBase = 'http://10.230.11.153:5000'

export async function callToServer(method, urlCall, params) {
    const url = new URL(urlCall, urlBase).toString()
    
    const response = await fetch(url, {
        method,
        body: JSON.stringify(params),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    return await response.json()
}
