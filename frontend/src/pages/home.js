import React, { useEffect, useState } from "react";
import Api from '../utils/api'

export default function Home() {
  const [messages, setMessages] = useState([])
  const [gameStarted, startGame] = useState(false)
  const [wordToGuess, setWordToGuess] = useState('')
  const api = new Api()

  const handleStartGameButtonClick = async () => {
    startGame(true)
    const response = await api.postJson({ path: '/start-game' })
    setMessages([...messages, response.msg])
  }

  const handleResetGameButtonClick = async () => {
    startGame(false)
    const response = await api.postJson({ path: '/reset-game' })
    setMessages([])
    setWordToGuess('')
  }

  const handleGuessWordButtonClick = async () => {
    console.log({ wordToGuess })
    const response = await api.postJson({ path: '/guess-word', body: { word: wordToGuess } })
    setMessages([...messages, response.msg])
  }

  const handleGuessWordInputChange = (event) => {
    const word = event.target.value
    console.log({ word })
    setWordToGuess(word)
  }

  return (
    <div>
      <h2>Home</h2>
      <div>
        {
          messages.map((message, index) => <div key={`msg-${index}`} className="message">{message}</div>)
        }
      </div>
      {
        !gameStarted ? (
          <button
            type="button"
            onClick={handleStartGameButtonClick}>
            Start game
          </button>
        ) : (
          <>
            <label>
              Введите слово:
              <input
                type="text"
                name="word"
                value={wordToGuess}
                onChange={handleGuessWordInputChange}
              />
            </label>

            <button
              type="button"
              onClick={handleResetGameButtonClick}>
              Reset game
            </button>
            <button
              type="button"
              onClick={handleGuessWordButtonClick}>
              Try
            </button>
          </>
      )
      }
    </div>
  );
}
