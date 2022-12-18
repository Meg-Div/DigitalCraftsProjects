const numbers = [
  "0",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "x",
  "/",
  "-",
  "+",
  "=",
];

const operators = ["x", "/", "-", "+", "="];

let nums = [];

//create container
const megsContainer = document.getElementsByClassName("mainContainer")[0];

//if button is 0-9
function number(evt) {
  console.log(evt.target.value);
  nums.push(Number(evt.target.value));
}

//if button is an operator
function operator(evt) {
  console.log(evt.target.value);
  nums.push(evt.target.value);
}

//randomly changes the background on click
const rgb = () => {
  document.body.style.backgroundColor =
    "#" + Math.floor(Math.random() * 16777215).toString(16);
};

//calculates on equal click
const equal = function () {
  //prints out equation line
  console.log(Object.values(nums).join("") + "=");

  //if user input operator first
  if (operators.includes(Object.values(nums)[0])) {
    window.alert("Please enter a number first.");
  }

  //if user inputs in double digits
  if (!operators.includes(Object.values(nums)[1])) {
    str = "";
    n = [];
    for (let i = 0; i < Object.values(nums).length; i++) {
      if (!operators.includes(Object.values(nums)[i])) {
        str = str + Object.values(nums)[i];
      } else {
        n.push(str);
        n.push(Object.values(nums)[i]);
        str = "";
      }
    }
    n.push(str);
    nums = n;
  }

  //calculate

  if (Object.values(nums)[1] == "/") {
    total = Object.values(nums)[0] / Object.values(nums)[2];
  } else if (Object.values(nums)[1] == "x") {
    total = Object.values(nums)[0] * Object.values(nums)[2];
  } else if (Object.values(nums)[1] == "-") {
    total = Object.values(nums)[0] - Object.values(nums)[2];
  }
  //use parsefloat to make sure no concat occurs
  else if (Object.values(nums)[1] == "+") {
    total =
      parseFloat(Object.values(nums)[0]) + parseFloat(Object.values(nums)[2]);
  }

  //if more than one calculation is being performed
  if (Object.values(nums).length > 3) {
    for (let i = 4; i < Object.values(nums).length; i++) {
      if (Object.values(nums)[i - 1] == "/") {
        total = total / Object.values(nums)[i];
      } else if (Object.values(nums)[i - 1] == "x") {
        total = total * Object.values(nums)[i];
      } else if (Object.values(nums)[i - 1] == "-") {
        total = total - Object.values(nums)[i];
      } else if (Object.values(nums)[i - 1] == "+") {
        total = parseFloat(total) + parseFloat(Object.values(nums)[i]);
      }
    }
  }

  h1.innerText = total + " \uD83C\uDF89";
  nums = [];
};

//creates buttons in JS and appends to container
for (let i = 0; i < numbers.length; i++) {
  const button = document.createElement("button");
  button.className = "num";
  button.innerText = numbers[i];
  button.addEventListener("click", rgb);
  if (i == numbers.length - 1) {
    button.addEventListener("click", equal);
  } else if (i < 9) {
    button.addEventListener("click", number);
    button.setAttribute("value", numbers[i]);
    button.innerText = numbers[i];
  } else {
    button.addEventListener("click", operator);
    button.setAttribute("value", numbers[i]);
  }
  megsContainer.append(button);
}

//header
const h1 = document.createElement("h1");
h1.className = "header";
h1.innerText = "Welcome to calculator!";
megsContainer.append(h1);
