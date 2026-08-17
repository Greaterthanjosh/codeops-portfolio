function greet(name) {
  return "Hello, " + name + "!";
}

console.log(greet("Josh"));

function outerFunction() {
  let message = "Welcome to JavaScript!";

  function innerFunction() {
    console.log(message);
  }

  innerFunction();
}

outerFunction();

// Higher-Order Function
function fun(n1, n2, callback) {
  return function () {
    return callback(n1, n2);
  };
}

// Callback function: addition
function add(a, b) {
  return a + b;
}

// Callback function: multiplication
function multiply(a, b) {
  return a * b;
}

// Using the higher-order function
const result1 = fun(10, 5, add);
console.log(result1()); // 15

const result2 = fun(10, 5, multiply);
console.log(result2()); // 50
