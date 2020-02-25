/*
 * AUTHOR: Timothy Lickteig
 * DATE: 2020-02-24
 *  Javascript code to run the calculator
 */
var operandOne = "";
var operandTwo = "";
var operator = "";
var answer = "";
$(document).ready(function() {

    $(".calcNumber").click(function() {
        numberButtonClick(this);
    });
    $(".calcOperator").click(function() {
        operatorButtonClick(this);
    });
    $(".calcEval").click(function() {
        evalButtonClick(this);
    });
    $(".calcConst").click(function() {
        constantButtonClick(this);
    });
    $(".calcNumMod").click(function() {
        numberModButtonClick(this);
    });
    $(".calcOther").click(function() {
        otherButtonClick(this);
    });
});
/*
 * Event handler functions
 */
function otherButtonClick(button) {

    option = $(button).attr("value");
    switch (option) {

        case "C":
            if (operator === "") {
                operandOne = "";
            } else {
                operandTwo = "";
            }
            printToDisplay("0");
            break;
        case "CE":
            operandOne = "";
            operandTwo = "";
            operator = "";
            printToDisplay("0");
            break;
        case "<-":
            if (operator === "" && operandOne.length > 0) {
                operandOne = operandOne.substring(0, operandOne.length - 1);
                printToDisplay(operandOne);
            } else if (operandTwo.length > 0) {
                operandTwo = operandTwo.substring(0, operandTwo.length - 1);
                printToDisplay(operandTwo);
            }
            break;
        case "=":
            if ((operandOne !== "") && (operandTwo !== "") && (operator !== "")) {
                
                var first = operandOne * 1;
                var second = operandTwo * 1;                
                switch (operator) {
                                        
                    case "+":                        
                        answer = first + second; 
                        break;
                    case "-":
                        answer = first - second;
                        break;
                    case "x":
                        answer = first * second;
                        break;
                    case "/":
                        answer = first / second;
                        break;
                    case "%":
                        answer = first % second;
                        break;
                    case "^":
                        answer = Math.pow(first, second);
                        break;
                }
                printToDisplay(answer);
                operandOne = answer;
                operandTwo = "";
                operator = "";
            }
            break;
    }
}

function constantButtonClick(button) {
    
    var target = Math.PI;
    if($(button).attr("value") === "e")
    {
        target = Math.E;
    }
    
    printToDisplay(target);
    if(operator === "") {
        operandOne = target;
    } else {
        operandTwo = target;
    }
}

function operatorButtonClick(button) {
    operator = $(button).attr("value");
}

function numberButtonClick(button) {

    if (operator === "") {
        operandOne = operandOne + $(button).attr("value");
        printToDisplay(operandOne);        
    } else {
        operandTwo = operandTwo + $(button).attr("value");
        printToDisplay(operandTwo);
    }
}

function numberModButtonClick(button) {
    
    var target;
    if(operator === "") {
        target = operandOne;
    } else {
        target = operandTwo;
    }
        
    if($(button).attr("value") === ".") {
        target = target + ".";
        /*
        if(target.indexOf(".") === -1) {
            target = target + ".";
        }
        */
    } else {
        if(target.indexOf("-") > -1) {
            target = target.substring(1, target.length);
        } else {
            target = "-" + target;
        }
    }
    
    if(operator === "") {
        firstOperand = target;
        printToDisplay(firstOperand);
    } else {
        secondOperand = target;
        printToDisplay(secondOperand);
    }
}

function evalButtonClick(button) {
    
    func = $(button).attr("value");
    target = 0;
    
    if(operator === "") {
        target = operandOne * 1;
    } else {
        target = operandTwo * 1;
    }
    
    switch(func) {
        
        case "√":
            target = Math.sqrt(target);
            break;
        case "sin":
            target = Math.sin(target);
            break;
        case "cos":
            target = Math.cos(target);
            break;
        case "tan":
            target = Math.tan(target);
            break;
        case "x²":
            target = Math.pow(target, 2);
            break;
        case "x³":
            target = Math.pow(target, 3);
            break;
        case "!":
            target = factorial(target);            
            break;
        case "abs":
            target = Math.abs(target);
            break;
        case "round":
            target = Math.round(target);
            break;
        case "ln":
            target = Math.log(target) / Math.log(Math.E);
            break;
        case "log":
            target = Math.log10(target);
            break;
    }
    
    printToDisplay(target);
    if(operator === "") {
        operandOne = target;
    } else {
        operandTwo = target;
    }
}

/**
 * Utility functions
 */
function printToDisplay(text) {
    $("#calcOutput").val(text);
}

function factorial(number) {
    
    if(number == 0) {
        return 1;
    }
    return number * factorial(number - 1);
}