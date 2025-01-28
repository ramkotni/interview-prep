https://react.dev/learn

Quick Start
Welcome to the React documentation! This page will give you an introduction to 80% of the React concepts that you will use on a daily basis.

You will learn
How to create and nest components
How to add markup and styles
How to display data
How to render conditions and lists
How to respond to events and update the screen
How to share data between components
Creating and nesting components 
React apps are made out of components. A component is a piece of the UI (user interface) that has its own logic and appearance. A component can be as small as a button, or as large as an entire page.

React components are JavaScript functions that return markup:

function MyButton() {
  return (
    <button>I'm a button</button>
  );
}
Now that you’ve declared MyButton, you can nest it into another component:

export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
Notice that <MyButton /> starts with a capital letter. That’s how you know it’s a React component. React component names must always start with a capital letter, while HTML tags must be lowercase.

Have a look at the result:


App.js
Download
Reset

Fork
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
function MyButton() {
  return (
    <button>
      I'm a button
    </button>
  );
}

export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}



Show more
The export default keywords specify the main component in the file. If you’re not familiar with some piece of JavaScript syntax, MDN and javascript.info have great references.

Writing markup with JSX 
The markup syntax you’ve seen above is called JSX. It is optional, but most React projects use JSX for its convenience. All of the tools we recommend for local development support JSX out of the box.

JSX is stricter than HTML. You have to close tags like <br />. Your component also can’t return multiple JSX tags. You have to wrap them into a shared parent, like a <div>...</div> or an empty <>...</> wrapper:

function AboutPage() {
  return (
    <>
      <h1>About</h1>
      <p>Hello there.<br />How do you do?</p>
    </>
  );
}
If you have a lot of HTML to port to JSX, you can use an online converter.

Adding styles 
In React, you specify a CSS class with className. It works the same way as the HTML class attribute:

<img className="avatar" />
Then you write the CSS rules for it in a separate CSS file:

/* In your CSS */
.avatar {
  border-radius: 50%;
}
React does not prescribe how you add CSS files. In the simplest case, you’ll add a <link> tag to your HTML. If you use a build tool or a framework, consult its documentation to learn how to add a CSS file to your project.

Displaying data 
JSX lets you put markup into JavaScript. Curly braces let you “escape back” into JavaScript so that you can embed some variable from your code and display it to the user. For example, this will display user.name:

return (
  <h1>
    {user.name}
  </h1>
);
You can also “escape into JavaScript” from JSX attributes, but you have to use curly braces instead of quotes. For example, className="avatar" passes the "avatar" string as the CSS class, but src={user.imageUrl} reads the JavaScript user.imageUrl variable value, and then passes that value as the src attribute:

return (
  <img
    className="avatar"
    src={user.imageUrl}
  />
);
You can put more complex expressions inside the JSX curly braces too, for example, string concatenation:


App.js
Download
Reset

Fork
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
const user = {
  name: 'Hedy Lamarr',
  imageUrl: 'https://i.imgur.com/yXOvdOSs.jpg',
  imageSize: 90,
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={'Photo of ' + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}

Updating the screen 
Often, you’ll want your component to “remember” some information and display it. For example, maybe you want to count the number of times a button is clicked. To do this, add state to your component.

First, import useState from React:

import { useState } from 'react';
Now you can declare a state variable inside your component:

function MyButton() {
  const [count, setCount] = useState(0);
  // ...
You’ll get two things from useState: the current state (count), and the function that lets you update it (setCount). You can give them any names, but the convention is to write [something, setSomething].

The first time the button is displayed, count will be 0 because you passed 0 to useState(). When you want to change state, call setCount() and pass the new value to it. Clicking this button will increment the counter:

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}
React will call your component function again. This time, count will be 1. Then it will be 2. And so on.

If you render the same component multiple times, each will get its own state. Click each button separately:


App.js
Download
Reset

Fork
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
import { useState } from 'react';

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}



Show more
Notice how each button “remembers” its own count state and doesn’t affect other buttons.

Using Hooks 
Functions starting with use are called Hooks. useState is a built-in Hook provided by React. You can find other built-in Hooks in the API reference. You can also write your own Hooks by combining the existing ones.

Hooks are more restrictive than other functions. You can only call Hooks at the top of your components (or other Hooks). If you want to use useState in a condition or a loop, extract a new component and put it there.

Sharing data between components 
In the previous example, each MyButton had its own independent count, and when each button was clicked, only the count for the button clicked changed:

Diagram showing a tree of three components, one parent labeled MyApp and two children labeled MyButton. Both MyButton components contain a count with value zero.
Initially, each MyButton’s count state is 0

The same diagram as the previous, with the count of the first child MyButton component highlighted indicating a click with the count value incremented to one. The second MyButton component still contains value zero.
The first MyButton updates its count to 1

However, often you’ll need components to share data and always update together.

To make both MyButton components display the same count and update together, you need to move the state from the individual buttons “upwards” to the closest component containing all of them.

In this example, it is MyApp:

Diagram showing a tree of three components, one parent labeled MyApp and two children labeled MyButton. MyApp contains a count value of zero which is passed down to both of the MyButton components, which also show value zero.
Initially, MyApp’s count state is 0 and is passed down to both children

The same diagram as the previous, with the count of the parent MyApp component highlighted indicating a click with the value incremented to one. The flow to both of the children MyButton components is also highlighted, and the count value in each child is set to one indicating the value was passed down.
On click, MyApp updates its count state to 1 and passes it down to both children

Now when you click either button, the count in MyApp will change, which will change both of the counts in MyButton. Here’s how you can express this in code.

First, move the state up from MyButton into MyApp:

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  // ... we're moving code from here ...
}
Then, pass the state down from MyApp to each MyButton, together with the shared click handler. You can pass information to MyButton using the JSX curly braces, just like you previously did with built-in tags like <img>:

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}
The information you pass down like this is called props. Now the MyApp component contains the count state and the handleClick event handler, and passes both of them down as props to each of the buttons.

Finally, change MyButton to read the props you have passed from its parent component:

function MyButton({ count, onClick }) {
  return (
    <button onClick={onClick}>
      Clicked {count} times
    </button>
  );
}
When you click the button, the onClick handler fires. Each button’s onClick prop was set to the handleClick function inside MyApp, so the code inside of it runs. That code calls setCount(count + 1), incrementing the count state variable. The new count value is passed as a prop to each button, so they all show the new value. This is called “lifting state up”. By moving state up, you’ve shared it between components.


App.js
Download
Reset

Fork
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
import { useState } from 'react';

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return (
    <button onClick={onClick}>
      Clicked {count} times
    </button>
  );
}



Show more
Next Steps 
By now, you know the basics of how to write React code!

Check out the Tutorial to put them into practice and build your first mini-app with React.

===============

What is React?
React is an open-source JavaScript library used for building user interfaces (UIs) for single-page applications (SPAs). It was developed by Facebook and is now maintained by Facebook and a community of developers. React allows developers to build reusable UI components, manage state and render dynamic content efficiently. Its core concepts revolve around a component-based architecture, where each component is a piece of the UI that manages its state and logic.

Key features of React include:

Declarative: React makes it easy to design interactive UIs by updating the UI automatically when the data changes.
Component-Based: Applications are built using components that can be reused and nested.
Virtual DOM: React uses a Virtual DOM (a lightweight representation of the actual DOM) to efficiently update and render the UI, making it faster.
Unidirectional Data Flow: Data flows in one direction, making it easier to track and manage the state of the application.
JSX: React uses JSX (JavaScript XML), which allows you to write HTML-like syntax directly within JavaScript code.
End-to-End React Project: Task Management App
In this example, we’ll build a simple Task Management App using React. The app will allow users to add, delete, and mark tasks as complete.

Steps to Build the Task Management App
1. Set Up the React Project
To get started, first, create a new React project using create-react-app.

bash
Copy
npx create-react-app task-manager
cd task-manager
npm start
This will set up the boilerplate for the React application and start a development server.

2. Project Structure
Here’s how we can structure our project:

bash
Copy
/task-manager
  /public
    index.html
  /src
    /components
      Task.js
      TaskList.js
      AddTask.js
    App.js
    index.js
    styles.css
3. Create Components
We'll break down the application into three main components:

AddTask: To add new tasks.
TaskList: To display the list of tasks.
Task: To display individual task items.
Task.js (Single Task Component)
jsx
Copy
import React from 'react';

function Task({ task, toggleComplete, deleteTask }) {
  return (
    <div className={`task ${task.completed ? 'completed' : ''}`}>
      <span onClick={() => toggleComplete(task.id)}>{task.text}</span>
      <button onClick={() => deleteTask(task.id)}>Delete</button>
    </div>
  );
}

export default Task;
This component displays a task with a button to delete it and the ability to mark it as complete. When the task is clicked, it triggers the toggleComplete function, and when the delete button is clicked, it triggers the deleteTask function.

TaskList.js (List of Tasks)
jsx
Copy
import React from 'react';
import Task from './Task';

function TaskList({ tasks, toggleComplete, deleteTask }) {
  return (
    <div className="task-list">
      {tasks.map(task => (
        <Task
          key={task.id}
          task={task}
          toggleComplete={toggleComplete}
          deleteTask={deleteTask}
        />
      ))}
    </div>
  );
}

export default TaskList;
This component loops through the list of tasks and renders a Task component for each one.

AddTask.js (Add New Task)
jsx
Copy
import React, { useState } from 'react';

function AddTask({ addTask }) {
  const [taskText, setTaskText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (taskText) {
      addTask(taskText);
      setTaskText('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="add-task-form">
      <input
        type="text"
        value={taskText}
        onChange={(e) => setTaskText(e.target.value)}
        placeholder="Enter a new task"
      />
      <button type="submit">Add Task</button>
    </form>
  );
}

export default AddTask;
This component allows the user to input a new task and add it to the list when the form is submitted.

4. Managing State in App.js
Now, let’s put everything together in App.js. This will be the main component where we manage the application state and handle functions like adding, deleting, and toggling tasks.

App.js
jsx
Copy
import React, { useState } from 'react';
import TaskList from './components/TaskList';
import AddTask from './components/AddTask';
import './styles.css';

function App() {
  const [tasks, setTasks] = useState([]);

  const addTask = (taskText) => {
    const newTask = {
      id: Date.now(),
      text: taskText,
      completed: false,
    };
    setTasks([...tasks, newTask]);
  };

  const toggleComplete = (taskId) => {
    const updatedTasks = tasks.map(task => 
      task.id === taskId ? { ...task, completed: !task.completed } : task
    );
    setTasks(updatedTasks);
  };

  const deleteTask = (taskId) => {
    const updatedTasks = tasks.filter(task => task.id !== taskId);
    setTasks(updatedTasks);
  };

  return (
    <div className="App">
      <h1>Task Manager</h1>
      <AddTask addTask={addTask} />
      <TaskList tasks={tasks} toggleComplete={toggleComplete} deleteTask={deleteTask} />
    </div>
  );
}

export default App;
In App.js, we are managing the tasks state using useState hook. The addTask function adds a new task to the list, toggleComplete toggles the task completion status, and deleteTask removes a task from the list. These functions are passed down to the AddTask and TaskList components as props.

5. Styling the App
Finally, we can add some basic CSS to style the application.

styles.css
css
Copy
.App {
  font-family: Arial, sans-serif;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.task-list {
  margin-top: 20px;
}

.task {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
  border-radius: 5px;
}

.completed {
  text-decoration: line-through;
  color: gray;
}

button {
  background-color: red;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}

button:hover {
  background-color: darkred;
}

.add-task-form {
  display: flex;
  gap: 10px;
}

input {
  flex-grow: 1;
  padding: 10px;
  font-size: 16px;
}

button[type="submit"] {
  padding: 10px 15px;
  background-color: green;
  color: white;
  border: none;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: darkgreen;
}
This simple CSS will style the task list and form, providing a user-friendly interface.

6. Run the Application
Once you’ve written the components, styles, and logic, you can run the application by typing:

bash
Copy
npm start
This will start a local development server and open the app in your browser. You should be able to add tasks, mark them as complete, and delete them.

7. Additional Features (Optional Enhancements)
Local Storage: Store tasks in the browser’s local storage so they persist even after a page refresh.
Editing Tasks: Add the ability to edit existing tasks.
Task Priority: Allow users to set priorities for tasks.
Authentication: Implement user authentication with Firebase or a custom back-end for managing tasks across sessions.
Conclusion
In this end-to-end project, we've built a simple Task Management App using React. This application allows users to add tasks, toggle completion, and delete them. We used React’s component-based architecture to create reusable components and managed the state using React’s useState hook. Additionally, we incorporated basic styling to enhance the UI.

This is a foundational example, but you can expand on this project by adding more complex features, such as task editing, persistence with APIs or local storage, or even user authentication for a more robust application.

===============

