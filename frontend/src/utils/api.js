export default class Api {
  async getJson({ headers = { 'Content-Type': 'application/json' }, path }) {
    const url = `${apiHost()}${path}`
    console.log('getJson#5', { headers, path })

    const response = await fetch(url, {
      method: 'GET',
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
      redirect: 'follow',
      referrerPolicy: 'no-referrer',
    }).catch((error) => {
      console.log("Error: " + error)
    })

    console.log('fetchJson#17', { response })
    return response.json()
  }
}

function apiHost() {
  return 'http://127.0.0.1:8000'
}
