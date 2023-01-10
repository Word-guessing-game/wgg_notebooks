import "macro-css";
import styles from "./Games.module.scss"


function Games({number, name, onGame}) {
  const onCurrentGame = () => {
    onGame(name);
  }
  return (
      <div className="pt-5 pb-5">
        <button type="button" className={styles.button_full} onClick={(obj) => onCurrentGame(obj)}>
          <div className={styles.game_selection_button}>
            <div>
              #{number} - {name}
            </div>
          </div>
        </button>
      </div>
    
  );
}

export default Games;
