//import { URL } from 'url'
import fetch from 'node-fetch'

let urlBase = 'http://localhost:5000'

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
