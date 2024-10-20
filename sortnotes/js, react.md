<!-- Declaration With let Keyword -->
{
    // block of code

    // declare variable with let
    let name = "Peter";

    // can be accessed here
    console.log(name); // Peter
}

// can't be accessed here
console.log(name);

<!-- Declaration With const Keyword -->
// declare variable with const
const fruit = "Apple";

console.log(fruit);

// reassign fruit
// this code causes an error
fruit = "Banana";

console.log(fruit);

<!-- JavaScript Template Literals -->
const firstName = "Jack";
const lastName = "Sparrow";

console.log("Hello " + firstName + " " + lastName);

// Output: Hello Jack Sparrow

const firstName = "Jack";
const lastName = "Sparrow";

console.log(`Hello ${firstName} ${lastName}`);

// Output: Hello Jack Sparrow

<!-- Default Parameter Values -->

// function to find sum of two numbers
function sum(numA, numB = 5) {

    // default value of numB is 5
    console.log(numA + numB);
};

// pass 10 to numA but
// don't pass value to numB
// numB takes default value 5
sum(10);  // 15

// pass 5 to numA and 15 to numB 
sum(5, 15);  // 20

<!-- JavaScript Arrow Function -->
// function expression
let product = function(x, y) {
   return x * y;
};

result = product(5, 10);

console.log(result);  // 50

// function expression using arrow function
let product = (x, y) => x * y;

result = product(5, 10);

console.log(result);  // 50

<!-- JavaScript Classes -->
// constructor function
function Person(name) {
    this.name = name;
};

// create objects
var p1 = new Person("John");
var p2 = new Person("Rachel");

// print object properties
console.log(p1.name);  // John
console.log(p2.name);  // Rachel


// declare a class
class Person {

    // constructor function
    constructor(name) {
        this.name = name;
    };
};

// create objects
let p1 = new Person("John");
let p2 = new Person("Rachel");

// print object properties
console.log(p1.name);  // John
console.log(p2.name);  // Rachel

<!-- JavaScript Destructuring -->
// object of hospital
const hospital = {
    doctors: 23,
    patients: 44,
};

// assign individual values
let doctors = hospital.doctors;
let patients = hospital.patients;

console.log(doctors);  // 23
console.log(patients);  // 44

const hospital = {
    doctors: 23,
    patients: 44,
};


<!-- JavaScript import and export -->
// use ES6 destructuring syntax
let { doctors, patients } = hospital;

console.log(doctors);  // 23
console.log(patients);  // 44


// export
export default function greet(name) {
    console.log(`Hi ${name}!`);
};

import greet from './action.js';

greet("Sara");

// Output: Hi Sara!


<!-- JavaScript Promise -->
// define a promise
let countValue = new Promise(function (resolve, reject) {
    setTimeout(function () {
        resolve("Promise resolved!");
    }, 5000);
});

// executes when promise resolves
countValue.then(function successValue(result) {
    console.log(result);
});

// Output: Promise resolved!

<!-- JavaScript Rest Parameter -->
// function with ...args rest parameter
function show(a, b, ...args) {
    console.log("a:", a);
    console.log("b:", b);
    console.log("args:", args);
}

// call function with extra parameters
show(1, 2, 3, 4, 5);


let numArr = [1, 2, 3];

<!-- Spread Operator -->
// without spread operator
console.log([numArr, 4, 5]);  // [[1, 2, 3], 4, 5]

// with spread operator
console.log([...numArr, 4, 5]);  // [1, 2, 3, 4, 5]


<!-- Declaration With let Keyword -->
<!-- Declaration With const Keyword -->
<!-- JavaScript Template Literals -->
<!-- Default Parameter Values -->
<!-- JavaScript Arrow Function -->
<!-- JavaScript Classes -->
<!-- JavaScript Destructuring -->
<!-- JavaScript import and export -->
<!-- JavaScript Promise -->
<!-- JavaScript Rest Parameter -->
<!-- Spread Operator -->




























JSX: HTML-like syntax inside JavaScript.
Components: Reusable building blocks of React.
Props: Used to pass data between components.
State and Hooks: Manage component data and lifecycle with useState and useEffect.
Event Handling: Handling events using functions.
Conditional Rendering: Display elements conditionally based on state/props.
Forms and Controlled Components: Managing form data with React state.
API Interaction: Fetching and manipulating data from an API.

24. Explain the lifecycle methods of components
A React Component can go through four stages of its life as follows. 

Initialization: This is the stage where the component is constructed with the given Props and default state. This is done in the constructor of a Component Class.
Mounting: Mounting is the stage of rendering the JSX returned by the render method itself.
Updating: Updating is the stage when the state of a component is updated and the application is repainted.
Unmounting: As the name suggests Unmounting is the final step of the component lifecycle where the component is removed from the page.

16. What is state in React?
The state is an instance of React Component Class that can be defined as an object of a set of observable properties that control the behaviour of the component. In other words, the State of a component is an object that holds some information that may change over the lifetime of the component.

16. Explain React Hooks.
What are Hooks? Hooks are functions that let us “hook into” React state and lifecycle features from a functional component.

  useState: Manages state in a functional component.
  useEffect: Handles side effects (e.g., fetching data, setting up subscriptions).
  useContext: Consumes context values directly in a component.
  useReducer: Manages complex state logic similar to useState but with a reducer function.
  useRef: Provides a mutable reference to access DOM elements or store a value that persists across renders.
  useMemo: Memoizes a computed value to optimize performance.
  useCallback: Memoizes a function reference to prevent unnecessary re-renders.
  useLayoutEffect: Fires synchronously after DOM mutations, suitable for layout reads/writes.

22. What is react router?
React Router is a standard library for routing in React. It enables the navigation among views of various components in a React Application, allows changing the browser URL, and keeps the UI in sync with the URL.


To install react router type the following command.

npm i react-router-dom


39. What is react-redux?
React-redux is a state management tool which makes it easier to pass these states from one component to another irrespective of their position in the component tree and hence prevents the complexity of the application. As the number of components in our application increases it becomes difficult to pass state as props to multiple components. To overcome this situation we use react-redux


PROPS

STATE

The Data is passed from one component to another.	The Data is passed within the component only.
It is Immutable (cannot be modified).	It is Mutable ( can be modified).
Props can be used with state and functional components.	The state can be used only with the state components/class component (Before 16.0).
Props are read-only.	The state is both read and write.


Here are some React interview questions covering React Hooks and Redux:

### React Hooks Questions

1. **What are React Hooks? Why were they introduced?**
   - Hooks are functions that let you use state and lifecycle features in functional components. They were introduced to avoid the complexity of class components and provide a simpler, more reusable way to handle state and side effects.

2. **What is the difference between `useState` and `useReducer`?**
   - `useState` is for managing simple state, while `useReducer` is used for more complex state logic and when multiple state updates depend on each other.

3. **Explain `useEffect` and its use cases.**
   - `useEffect` is for performing side effects like fetching data, subscribing to events, or manipulating the DOM after a component renders. It can be used for componentDidMount, componentDidUpdate, and componentWillUnmount lifecycle events.

4. **How can you optimize performance with `useMemo` and `useCallback`?**
   - `useMemo` memorizes expensive calculations, preventing recalculation on every render unless dependencies change. `useCallback` memoizes functions, ensuring they don’t get recreated on every render when passed as props.

5. **What is the difference between `useEffect` and `useLayoutEffect`?**
   - `useEffect` runs after the render and paint, while `useLayoutEffect` runs synchronously after render but before painting. This makes `useLayoutEffect` suitable for manipulating DOM measurements before the browser repaints.

6. **Can you explain `useContext` and how it’s used?**
   - `useContext` allows a component to consume context values. It's a way to share state and logic globally or within a subtree without prop drilling.

7. **What are custom hooks, and when would you create one?**
   - Custom hooks are functions that start with `use` and allow you to extract and reuse logic across components. You create one when you notice repeating logic or want to separate concerns.

### Redux Questions

1. **What is Redux, and why is it used in React?**
   - Redux is a state management library that provides a centralized store for the state of your application. It helps manage state consistency across components and makes debugging easier.

2. **What are the core principles of Redux?**
   - **Single source of truth** (a single state tree), **State is read-only** (only changes through actions), and **Changes are made with pure functions** (reducers).

3. **Explain how actions, reducers, and the store work together in Redux.**
   - Actions are plain objects that describe changes. Reducers are pure functions that determine how the state changes based on actions. The store holds the state and provides methods like `dispatch` to send actions and `subscribe` to listen for changes.

4. **How does `useSelector` and `useDispatch` work in React-Redux?**
   - `useSelector` is used to access Redux state in a component, and `useDispatch` is used to dispatch actions to the store.

5. **What is middleware in Redux? Can you give examples?**
   - Middleware intercepts actions before they reach the reducer. Examples include `redux-thunk` (for asynchronous actions) and `redux-saga` (for handling complex side effects).

6. **How would you manage side effects in Redux?**
   - Side effects can be managed using middleware like `redux-thunk` or `redux-saga`, which allows dispatching asynchronous actions and handling API calls or other asynchronous behavior.

7. **What are higher-order components (HOCs) in React? How are they related to Redux?**
   - HOCs are functions that take a component and return a new one, enhancing it with additional props or functionality. In Redux, HOCs like `connect` from `react-redux` are used to connect a component to the Redux store.

8. **How does Redux differ from React’s Context API?**
   - Redux provides more structured state management and middleware for handling side effects, while the Context API is a simpler solution for passing data deep in the component tree. Redux is generally better for larger, more complex applications.

These questions should help prepare for interviews focusing on React Hooks, Redux, and their integration into React applications.


Here's an overview of interview questions with answers for each React topic:

### 1. **JSX: HTML-like syntax inside JavaScript**
   - **Question**: What is JSX, and why do we use it in React?
   - **Answer**: JSX is a syntax extension for JavaScript that looks similar to HTML. It allows us to write HTML-like code in our JavaScript files, making it easier to visualize the UI structure directly in the code. JSX is then compiled into `React.createElement` calls, which create virtual DOM elements.

### 2. **Components: Reusable building blocks of React**
   - **Question**: What are React components, and what are the differences between functional and class components?
   - **Answer**: Components are the building blocks of React applications, allowing us to break the UI into reusable and independent pieces. 
     - **Functional Components**: Simple JavaScript functions that take props as input and return JSX.
     - **Class Components**: ES6 classes that extend `React.Component` and have access to lifecycle methods and state.

### 3. **Props: Used to pass data between components**
   - **Question**: What are props, and how are they different from state?
   - **Answer**: Props (short for properties) are used to pass data from a parent component to a child component. They are read-only and immutable, ensuring that child components do not modify the data they receive. State, on the other hand, is local to the component and can be changed within that component.

### 4. **State and Hooks: Manage component data and lifecycle with `useState` and `useEffect`**
   - **Question**: How do you manage state in functional components using hooks?
   - **Answer**: In functional components, the `useState` hook is used to declare state variables. It returns an array with the current state value and a function to update that value. 
     - Example: `const [count, setCount] = useState(0);`
   - **Question**: What is the `useEffect` hook, and when do you use it?
   - **Answer**: `useEffect` is a hook used to perform side effects (e.g., fetching data, subscribing to events) in a component. It runs after the component renders. You can specify dependencies to control when the effect should run.

### 5. **Event Handling: Handling events using functions**
   - **Question**: How do you handle events in React?
   - **Answer**: Event handling in React is similar to handling events in plain JavaScript, but with a few differences:
     - Events are named using camelCase, e.g., `onClick`.
     - Event handlers are passed as functions, not strings: `<button onClick={handleClick}>Click me</button>`.
     - In functional components, event handlers often use the state to respond dynamically.

### 6. **Conditional Rendering: Display elements conditionally based on state/props**
   - **Question**: How do you implement conditional rendering in React?
   - **Answer**: Conditional rendering in React can be done using:
     - Ternary operators: `{isLoggedIn ? <Logout /> : <Login />}`
     - Logical `&&`: `{isAdmin && <AdminPanel />}`
     - `if-else` statements inside the render method (more common in class components).

### 7. **Forms and Controlled Components: Managing form data with React state**
   - **Question**: What are controlled components, and how do you manage form inputs in React?
   - **Answer**: Controlled components are input elements where the form data is handled by the React component's state. The value of the input is tied to the state, and changes are handled using an `onChange` event handler. This ensures a single source of truth for the input's value.

### 8. **API Interaction: Fetching and manipulating data from an API**
   - **Question**: How do you fetch data from an API in React?
   - **Answer**: You can fetch data using the `fetch` API or libraries like Axios inside the `useEffect` hook. The `useEffect` hook ensures the data fetch occurs after the component renders.
     - Example:
       ```javascript
       useEffect(() => {
           fetch('https://api.example.com/data')
               .then(response => response.json())
               .then(data => setData(data));
       }, []);
       ```
   - **Question**: How do you handle API errors and loading states?
   - **Answer**: You manage loading and error states using additional state variables (e.g., `isLoading` and `error`). You can conditionally render UI based on these states, such as showing a loading spinner or error message.