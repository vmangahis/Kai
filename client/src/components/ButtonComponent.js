function ButtonComponent(props) {
    return (
        <button className={props.class}  onClick={() => {console.log('helol')}}>{props.label}</button>
    );
}

export default ButtonComponent;