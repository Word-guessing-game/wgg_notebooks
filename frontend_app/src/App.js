import "macro-css";
import Dropdown from "./components/Dropdown";
import Rules from "./components/Rules";
import Currentraw from "./components/Currentraw";
import Raw from "./components/Raw";
import Games from "./components/Games";
import React, { useCallback } from "react";

function App() {
  const [isOpened, setIsOpened] = React.useState(false);
  const onClickOpen = () => {
    setIsOpened(!isOpened);
  };
  const [isHowPlay, setIsHowPlay] = React.useState(false);
  const [isChoseGame, setIsChoseGame] = React.useState(false);
  const [gameNumbers, setGameNumbers] = React.useState(0);
  const [currentGame, setCurrentGame] = React.useState("");
  const [arrWords, setArrWords] = React.useState([]);
  const [inputValue, setInputValue] = React.useState("");
  const [requestResult, setRequestResult] = React.useState();
  const [isLoaded, setIsLoaded] = React.useState(false);
  const [data, setData] = React.useState("");
  const [errorRequest, setErrorRequest] = React.useState();

  React.useEffect(() => {
    fetch("http://127.0.0.1:8000/get_games_numbers", {
      method: "POST",
      headers: {
        accept: "application/json",
      },
    })
      .then((res) => {
        return res.json();
      })
      .then((json) => {
        setGameNumbers(json);
      });
  }, []);

  React.useEffect(() => {
    if ((currentGame.length > 1) & (data.length > 1)) {
      fetch("http://127.0.0.1:8000/get_word_position", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ n_game: currentGame, game_word: data }),
      })
        .then((res) => {
          return res.json();
        })
        .then(
          (json) => {
            setRequestResult(json);
            setIsLoaded(true);
            setErrorRequest();
          },
          (error) => {
            if (error) {
              setErrorRequest("Извините, я не знаю этого слова");
            }
          }
        );
    }
  }, [data]);

  React.useEffect(() => {
    if (requestResult) {
      {
        setArrWords([...arrWords, requestResult]);
      }
    }
  }, [requestResult]);

  const [win, setWin] = React.useState();
  React.useEffect(() => {
    try {
      arrWords.at(-1).position === 0 ? setWin(1) : setWin(0);
    } catch (err) {
      console.log("неть ничего");
    }
  }, [arrWords]);

  React.useEffect(() => {
    if (win === 1) {
      setArrWords([]);
    }
  }, [win]);

  return (
    <div className="wrapper">
      <div className="top-bar">
        <div className="title">
          <h1>Guess the word!</h1>
        </div>
        <div className="pos-r">
          <button
            className={isOpened ? "btn-active" : "btn"}
            onClick={onClickOpen}
          >
            <svg
              src="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              fill="currentColor"
              viewBox="0 0 16 16"
            >
              <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"></path>
            </svg>
          </button>
          <Dropdown
            state={isOpened}
            onClickHowPlay={() => [
              setIsHowPlay(!isHowPlay),
              setIsOpened(!isOpened),
            ]}
            onClickChoseGame={() => [
              setIsChoseGame(!isChoseGame),
              setIsOpened(!isOpened),
            ]}
          />
        </div>
      </div>
      <div className="info-bar">
        <span className="label"> ИГРА:</span>
        <span>#{currentGame} </span>
        <span className="label"> ПОПЫТОК:</span>
        <span>{arrWords.length}</span>
      </div>
      <div className="form">
        <input
          className="word"
          type="text"
          placeholder="введите слово"
          value={inputValue}
          onChange={(event) => setInputValue(event.target.value)}
        />
        <button className="checkButton" onClick={() => setData(inputValue)}>
          Проверить
        </button>
      </div>
      {errorRequest ? (
        <div className="message-text">Извините, я не знаю этого слова</div>
      ) : (
        <div></div>
      )}
      {console.log(arrWords)}
      {arrWords.length ? (
        <div className="guess-history">
          <div>
            <Currentraw lastElem={arrWords.at(-1)} />
          </div>

          {arrWords.map((obj) => (
            <Raw word={obj.word} position={obj.position} />
          ))}
          <Currentraw lastElem={arrWords.at(-1)} />
        </div>
      ) : (
        <div></div>
      )}
      {win === 1 ? (
        <div><div className="end-msg">
        <p className="bigger">Поздравляем!</p>
        <p>Вы угадали слово игры  <b>{currentGame}</b></p>  
      </div>
      <img src="/74US.gif" alt="salute" /></div>
      ) : (
        <div></div>
      )}
      {isChoseGame ? (
        <div className="modal_bg">
          <div className="modal_wrapper">
            <div
              className="modal_close_button"
              onClick={() => setIsChoseGame(!isChoseGame)}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                viewBox="0 0 16 16"
              >
                <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"></path>
              </svg>
            </div>
            <div className="modal">
              <div>
                <p>Select a previous game to play:</p>
                <div>
                  {gameNumbers.map((obj) => (
                    <Games
                      number={obj.number}
                      name={obj.name}
                      onGame={(obj) => [
                        setCurrentGame(obj),
                        setIsChoseGame(!isChoseGame),
                        setArrWords([]),
                        setWin(0),
                      ]}
                    />
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      ) : null}
      {isHowPlay ? (
        <Rules onClickHowPlay={() => setIsHowPlay(!isHowPlay)} />
      ) : null}
    </div>
  );
}

export default App;
