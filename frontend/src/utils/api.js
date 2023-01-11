import { apiHost } from "../config/settings"

export default class Api {
  async makeJsonRequest({ method, headers = {}, body = {}, path }) {
    const url = `${apiHost()}${path}`
    console.log({ body })

    const response = await fetch(url, {
      method,
      mode: 'cors',
      cache: 'no-cache',
      credentials: 'omit',
      headers: {
        ...headers,
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Request-Method': '*',
        'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
      },
      body,
      redirect: 'follow',
      referrerPolicy: 'no-referrer',
    }).catch((error) => {
      console.log("Error: " + error)
    })

    console.log('fetchJson#17', { response })
    return response.json()
  }

  async getJson({ headers = { 'Content-Type': 'application/json' }, path }) {
    return await this.makeJsonRequest({ method: 'GET', headers, path })
  }

  async postJson({ headers = { 'Content-Type': 'application/json' }, body = {}, path }) {
    return await this.makeJsonRequest({ method: 'POST', headers, body: JSON.stringify(body), path })
  }
}
