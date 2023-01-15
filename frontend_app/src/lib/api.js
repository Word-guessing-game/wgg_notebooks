import env from "react-dotenv";

export const fetchFromApi = ({ path, method = 'POST', body = {} }) => {
  const url = `${env.API_HOST}${path}`

  return fetch(url, {
    method,
    mode: 'cors',
    headers: {
      accept: "application/json",
      "Content-Type": "application/json",
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Request-Method': '*',
      'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    },
    body: JSON.stringify(body),
  }).then((res) => {
    return res.json();
  })
}
