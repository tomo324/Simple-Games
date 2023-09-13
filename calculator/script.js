const displayArea = document.querySelector("#display");
const buttons = document.querySelectorAll("button");

function clickedValue(e) {
    console.log("Button clicked:", e.target.textContent); 
    let buttonValue = e.target.textContent;

    switch (buttonValue) {
        case "C":
            displayArea.value = "";
            break;
        case "=":
            displayArea.value = eval(displayArea.value);
            break;
        default:
            displayArea.value += buttonValue;
            break;
    }
}

buttons.forEach(function(button) {
    button.addEventListener("click", clickedValue);
});
