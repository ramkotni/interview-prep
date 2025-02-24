React Props
Props are arguments passed into React components.

Props are passed to components via HTML attributes.

props stands for properties.

React Props
React Props are like function arguments in JavaScript and attributes in HTML.

To send props into a component, use the same syntax as HTML attributes:

ExampleGet your own React.js Server
Add a "brand" attribute to the Car element:

const myElement = <Car brand="Ford" />;

The component receives the argument as a props object:

Example
Use the brand attribute in the component:

function Car(props) {
  return <h2>I am a { props.brand }!</h2>;
}

Pass Data
Props are also how you pass data from one component to another, as parameters.

Example
Send the "brand" property from the Garage component to the Car component:

function Car(props) {
  return <h2>I am a { props.brand }!</h2>;
}

function Garage() {
  return (
    <>
      <h1>Who lives in my garage?</h1>
      <Car brand="Ford" />
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Garage />);

If you have a variable to send, and not a string as in the example above, you just put the variable name inside curly brackets:

Example
Create a variable named carName and send it to the Car component:

function Car(props) {
  return <h2>I am a { props.brand }!</h2>;
}

function Garage() {
  const carName = "Ford";
  return (
    <>
      <h1>Who lives in my garage?</h1>
      <Car brand={ carName } />
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Garage />);

Or if it was an object:

Example
Create an object named carInfo and send it to the Car component:

function Car(props) {
  return <h2>I am a { props.brand.model }!</h2>;
}

function Garage() {
  const carInfo = { name: "Ford", model: "Mustang" };
  return (
    <>
      <h1>Who lives in my garage?</h1>
      <Car brand={ carInfo } />
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Garage />);
==========================

React Events
Just like HTML DOM events, React can perform actions based on user events.

React has the same events as HTML: click, change, mouseover etc.

Adding Events
React events are written in camelCase syntax:

onClick instead of onclick.

React event handlers are written inside curly braces:

onClick={shoot}  instead of onclick="shoot()".

React:Get your own React.js Server
<button onClick={shoot}>Take the Shot!</button>
HTML:
<button onclick="shoot()">Take the Shot!</button>

Example:
Put the shoot function inside the Football component:

function Football() {
  const shoot = () => {
    alert("Great Shot!");
  }

  return (
    <button onClick={shoot}>Take the shot!</button>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Football />);

=========================

React Forms
Just like in HTML, React uses forms to allow users to interact with the web page.

Adding Forms in React
You add a form with React like any other element:

Example:Get your own React.js Server
Add a form that allows users to enter their name:

function MyForm() {
  return (
    <form>
      <label>Enter your name:
        <input type="text" />
      </label>
    </form>
  )
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyForm />);

This will work as normal, the form will submit and the page will refresh.

But this is generally not what we want to happen in React.

We want to prevent this default behavior and let React control the form.

Handling Forms
Handling forms is about how you handle the data when it changes value or gets submitted.

In HTML, form data is usually handled by the DOM.

In React, form data is usually handled by the components.

When the data is handled by the components, all the data is stored in the component state.

You can control changes by adding event handlers in the onChange attribute.

We can use the useState Hook to keep track of each inputs value and provide a "single source of truth" for the entire application.

See the React Hooks section for more information on Hooks.

Example:
Use the useState Hook to manage the input:

import { useState } from 'react';
import ReactDOM from 'react-dom/client';

function MyForm() {
  const [name, setName] = useState("");

  return (
    <form>
      <label>Enter your name:
        <input
          type="text" 
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
    </form>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyForm />);

===============

React Router
Create React App doesn't include page routing.

React Router is the most popular solution.

Add React Router
To add React Router in your application, run this in the terminal from the root directory of the application:

npm i -D react-router-dom
Note: This tutorial uses React Router v6.

If you are upgrading from v5, you will need to use the @latest flag:

npm i -D react-router-dom@latest
Folder Structure
To create an application with multiple page routes, let's first start with the file structure.

Within the src folder, we'll create a folder named pages with several files:

src\pages\:

Layout.js
Home.js
Blogs.js
Contact.js
NoPage.js
Each file will contain a very basic React component.

Basic Usage
Now we will use our Router in our index.js file.

ExampleGet your own React.js Server
Use React Router to route to pages based on URL:

index.js:

import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Blogs from "./pages/Blogs";
import Contact from "./pages/Contact";
import NoPage from "./pages/NoPage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="blogs" element={<Blogs />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

Example Explained
We wrap our content first with <BrowserRouter>.

Then we define our <Routes>. An application can have multiple <Routes>. Our basic example only uses one.

<Route>s can be nested. The first <Route> has a path of / and renders the Layout component.

The nested <Route>s inherit and add to the parent route. So the blogs path is combined with the parent and becomes /blogs.

The Home component route does not have a path but has an index attribute. That specifies this route as the default route for the parent route, which is /.

Setting the path to * will act as a catch-all for any undefined URLs. This is great for a 404 error page.

================

React Hooks
Hooks were added to React in version 16.8.

Hooks allow function components to have access to state and other React features. Because of this, class components are generally no longer needed.

Although Hooks generally replace class components, there are no plans to remove classes from React.

What is a Hook?
Hooks allow us to "hook" into React features such as state and lifecycle methods.

Example:Get your own React.js Server
Here is an example of a Hook. Don't worry if it doesn't make sense. We will go into more detail in the next section.

import React, { useState } from "react";
import ReactDOM from "react-dom/client";

function FavoriteColor() {
  const [color, setColor] = useState("red");

  return (
    <>
      <h1>My favorite color is {color}!</h1>
      <button
        type="button"
        onClick={() => setColor("blue")}
      >Blue</button>
      <button
        type="button"
        onClick={() => setColor("red")}
      >Red</button>
      <button
        type="button"
        onClick={() => setColor("pink")}
      >Pink</button>
      <button
        type="button"
        onClick={() => setColor("green")}
      >Green</button>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<FavoriteColor />);

You must import Hooks from react.

Here we are using the useState Hook to keep track of the application state.

State generally refers to application data or properties that need to be tracked.

Hook Rules
There are 3 rules for hooks:

Hooks can only be called inside React function components.
Hooks can only be called at the top level of a component.
Hooks cannot be conditional
Note: Hooks will not work in React class components.

Custom Hooks
If you have stateful logic that needs to be reused in several components, you can build your own custom Hooks.

We'll go into more detail in the Custom Hooks section.

====
React useEffect Hooks
The useEffect Hook allows you to perform side effects in your components.

Some examples of side effects are: fetching data, directly updating the DOM, and timers.

useEffect accepts two arguments. The second argument is optional.

useEffect(<function>, <dependency>)

Let's use a timer as an example.

Example:Get your own React.js Server
Use setTimeout() to count 1 second after initial render:

import { useState, useEffect } from "react";
import ReactDOM from "react-dom/client";

function Timer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    setTimeout(() => {
      setCount((count) => count + 1);
    }, 1000);
  });

  return <h1>I've rendered {count} times!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Timer />);

But wait!! It keeps counting even though it should only count once!

useEffect runs on every render. That means that when the count changes, a render happens, which then triggers another effect.

This is not what we want. There are several ways to control when side effects run.

We should always include the second parameter which accepts an array. We can optionally pass dependencies to useEffect in this array.

Example
1. No dependency passed:

useEffect(() => {
  //Runs on every render
});
Example
2. An empty array:

useEffect(() => {
  //Runs only on the first render
}, []);
Example
3. Props or state values:

useEffect(() => {
  //Runs on the first render
  //And any time any dependency value changes
}, [prop, state]);
So, to fix this issue, let's only run this effect on the initial render.

===============

React Custom Hooks
Hooks are reusable functions.

When you have component logic that needs to be used by multiple components, we can extract that logic to a custom Hook.

Custom Hooks start with "use". Example: useFetch.

Build a Hook
In the following code, we are fetching data in our Home component and displaying it.

We will use the JSONPlaceholder service to fetch fake data. This service is great for testing applications when there is no existing data.

To learn more, check out the JavaScript Fetch API section.

Use the JSONPlaceholder service to fetch fake "todo" items and display the titles on the page:

Example:Get your own React.js Server
index.js:

import { useState, useEffect } from "react";
import ReactDOM from "react-dom/client";

const Home = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/todos")
      .then((res) => res.json())
      .then((data) => setData(data));
 }, []);

  return (
    <>
      {data &&
        data.map((item) => {
          return <p key={item.id}>{item.title}</p>;
        })}
    </>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Home />);

The fetch logic may be needed in other components as well, so we will extract that into a custom Hook.

Move the fetch logic to a new file to be used as a custom Hook:

Example:
useFetch.js:

import { useState, useEffect } from "react";

const useFetch = (url) => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => setData(data));
  }, [url]);

  return [data];
};

export default useFetch;
index.js:

import ReactDOM from "react-dom/client";
import useFetch from "./useFetch";

const Home = () => {
  const [data] = useFetch("https://jsonplaceholder.typicode.com/todos");

  return (
    <>
      {data &&
        data.map((item) => {
          return <p key={item.id}>{item.title}</p>;
        })}
    </>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Home />);

Example Explained
We have created a new file called useFetch.js containing a function called useFetch which contains all of the logic needed to fetch our data.

We removed the hard-coded URL and replaced it with a url variable that can be passed to the custom Hook.

Lastly, we are returning our data from our Hook.

In index.js, we are importing our useFetch Hook and utilizing it like any other Hook. This is where we pass in the URL to fetch data from.

Now we can reuse this custom Hook in any component to fetch data from any URL.

===================
