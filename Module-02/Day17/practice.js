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