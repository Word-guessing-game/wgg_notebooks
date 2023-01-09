import React, { useEffect, useState } from "react";
import Api from '../utils/api'

export default function Home() {
  const [messages, setMessages] = useState([]);

  const handleClick = async () => {
    console.log('handleClick#5')
    const api = new Api()
    const response = await api.getJson({ path: '/hello-world' })
    setMessages([...messages, response.msg])
  }

  return (
    <div>
      <h2>Home</h2>
      <div>
        {
          messages.map((message, index) => <div key={`msg-${index}`} className="message">{message}</div>)
        }
      </div>
      <button type="button" onClick={handleClick}>
        ClickMe
      </button>
    </div>
  );
}
