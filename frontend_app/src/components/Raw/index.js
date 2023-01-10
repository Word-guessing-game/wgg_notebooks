import styles from "./Raw.module.scss"

function Raw(props) {
  var bar_color;
  if (props.position<=1000){
    bar_color="#AFEEEE"
  } else if (props.position > 1000 && props.position <= 5000){
    bar_color="#F0E68C"
  }else{
    bar_color="#FFC0CB"
  };
  return (
    <div className={styles.row_wrapper}>
      <div className={styles.outer_bar}>
        <div className={styles.inner_bar} style={{ width: `${100-props.position * 100/5000}%`, background: `${bar_color}` }}></div>
      </div>
      <div className={styles.raw}>
        <span>{props.word}</span>
        <span>{props.position}</span>
      </div>
    </div>
  );
}

export default Raw;
