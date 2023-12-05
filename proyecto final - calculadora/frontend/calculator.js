let currentInput = '';
let operator = '';
let firstOperand = '';

function appendNumber(number) {
    currentInput += number;
    updateDisplay();
}

function setOperator(op) {
    operator = op;
    firstOperand = currentInput;
    currentInput = '';
}

function clearDisplay() {
    currentInput = '';
    operator = '';
    firstOperand = '';
    updateDisplay();
}

function calculateResult() {
    let result;
    const secondOperand = currentInput;
    switch (operator) {
        case '+':
            result = parseFloat(firstOperand) + parseFloat(secondOperand);
            break;
        case '-':
            result = parseFloat(firstOperand) - parseFloat(secondOperand);
            break;
        case '*':
            result = parseFloat(firstOperand) * parseFloat(secondOperand);
            break;
        case '/':
            result = parseFloat(firstOperand) / parseFloat(secondOperand);
            break;
        default:
            return;
    }
    currentInput = result.toString();
    operator = '';
    firstOperand = '';
    updateDisplay();
}

function updateDisplay() {
    document.getElementById('display').value = currentInput;
}

// Manejador de eventos para las teclas
document.addEventListener('keydown', function (event) {
    const key = event.key;

    if (!isNaN(key) || key === '.') {
        // Números y punto decimal
        appendNumber(key);
    } else if (key === '+' || key === '-' || key === '*' || key === '/') {
        // Operadores
        setOperator(key);
    } else if (key === 'Enter') {
        // Tecla Enter para calcular el resultado
        calculateResult();
    } else if (key === 'Escape') {
        // Tecla Escape para borrar
        clearDisplay();
    }
});
