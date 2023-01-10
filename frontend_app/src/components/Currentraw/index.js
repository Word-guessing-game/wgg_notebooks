import styles from './Currentraw.module.scss';

function Currentraw(props) {
  var bar_color;
  if (props.lastElem.position<=1000){
    bar_color="#AFEEEE"
  } else if (props.lastElem.position > 1000 && props.lastElem.position <= 5000){
    bar_color="#F0E68C"
  }else{
    bar_color="#FFC0CB"
  };
  return (
    <div className={styles.row_wrapper_current}>
      <div className={styles.outer_bar}>
        <div className={styles.inner_bar}style={{ width: `${100-props.lastElem.position * 100/5000}%`, background: `${bar_color}` }}></div>
      </div>
      <div className={styles.raw}>
        <span>{props.lastElem.word}</span>
        <span>{props.lastElem.position}</span>
      </div>
    </div>
  );
}

export default Currentraw;
