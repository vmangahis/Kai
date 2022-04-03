function ButtonComponent(props) {
    return (
        <button class={props.class}>{props.label}</button>
    );
}

export default ButtonComponent;