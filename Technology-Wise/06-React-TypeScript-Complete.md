# REACT & TYPESCRIPT - COMPREHENSIVE INTERVIEW Q&A

## Expert Level Q&A | Production Experience

---

## Q1: React Hooks and Functional Components

**A:**

Hooks revolutionized React by allowing stateful logic in functional components instead of requiring class components.

### Hooks vs Class Components:

**Before (Class Component):**
```typescript
class UserComponent extends React.Component {
  state = { user: null, loading: true };
  
  componentDidMount() {
    fetch('/api/users/1')
      .then(res => res.json())
      .then(user => this.setState({ user, loading: false }));
  }
  
  render() {
    const { user, loading } = this.state;
    if (loading) return <div>Loading...</div>;
    return <div>{user.name}</div>;
  }
}
```

**After (Functional Component with Hooks):**
```typescript
function UserComponent() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch('/api/users/1')
      .then(res => res.json())
      .then(user => {
        setUser(user);
        setLoading(false);
      });
  }, []);  // Empty dependency array = run once on mount
  
  if (loading) return <div>Loading...</div>;
  return <div>{user?.name}</div>;
}
```

### Main Hooks:

**1. useState - State Management**
```typescript
const [count, setCount] = useState(0);

// Lazy initialization
const [expensiveValue, setExpensiveValue] = useState(() => {
  return complexCalculation();  // Runs only on first render
});

// Multiple states
const [user, setUser] = useState({ name: '', email: '' });
const updateUserName = (name) => {
  setUser(prev => ({ ...prev, name }));  // Functional update
};
```

**2. useEffect - Side Effects (Mounting, Updating, Cleanup)**
```typescript
// Run on every render (BAD - performance issue)
useEffect(() => {
  console.log('Renders on every update');
});

// Run on mount only
useEffect(() => {
  console.log('Runs once on mount');
}, []);

// Run when dependencies change
useEffect(() => {
  console.log('Runs when userId changes');
}, [userId, userName]);

// Cleanup function (unmount or before re-run)
useEffect(() => {
  const subscription = eventBus.subscribe(handleEvent);
  
  return () => {
    subscription.unsubscribe();  // Cleanup to avoid memory leaks
  };
}, []);

// Multiple effects for different concerns
useEffect(() => {
  document.title = `User: ${user.name}`;
}, [user.name]);

useEffect(() => {
  const timerHandle = setTimeout(() => {
    logUserActivity();
  }, 5000);
  
  return () => clearTimeout(timerHandle);
}, []);
```

**3. useContext - Avoid Prop Drilling**
```typescript
// Create context
const UserContext = React.createContext();

// Provider component
function App() {
  const [user, setUser] = useState(null);
  
  return (
    <UserContext.Provider value={{ user, setUser }}>
      <UserProfile />
      <UserSettings />
    </UserContext.Provider>
  );
}

// Consumer components - no prop drilling!
function UserProfile() {
  const { user } = useContext(UserContext);
  return <div>Welcome, {user?.name}</div>;
}

function UserSettings() {
  const { user, setUser } = useContext(UserContext);
  return (
    <button onClick={() => setUser({ name: 'Updated' })}>
      Update Name
    </button>
  );
}
```

**4. useReducer - Complex State Logic**
```typescript
const initialState = { user: null, loading: true, error: null };

function reducer(state, action) {
  switch (action.type) {
    case 'LOADING':
      return { ...state, loading: true, error: null };
    case 'SUCCESS':
      return { ...state, user: action.payload, loading: false };
    case 'ERROR':
      return { ...state, loading: false, error: action.payload };
    default:
      return state;
  }
}

function UserComponent() {
  const [state, dispatch] = useReducer(reducer, initialState);
  
  useEffect(() => {
    dispatch({ type: 'LOADING' });
    fetch('/api/users/1')
      .then(res => res.json())
      .then(user => dispatch({ type: 'SUCCESS', payload: user }))
      .catch(error => dispatch({ type: 'ERROR', payload: error.message }));
  }, []);
  
  if (state.loading) return <div>Loading...</div>;
  if (state.error) return <div>Error: {state.error}</div>;
  return <div>{state.user?.name}</div>;
}
```

**5. useCallback - Memoize Functions**
```typescript
// Without useCallback: Function recreated on every render
function UserList() {
  const [users, setUsers] = useState([]);
  
  const handleDelete = (id) => {
    setUsers(users.filter(u => u.id !== id));
  };
  
  // NEW function reference every render!
  return <UserListItems users={users} onDelete={handleDelete} />;
}

// With useCallback: Function reused unless dependencies change
function UserList() {
  const [users, setUsers] = useState([]);
  
  const handleDelete = useCallback((id) => {
    setUsers(prev => prev.filter(u => u.id !== id));
  }, []);  // Empty dependencies = function never changes
  
  return <UserListItems users={users} onDelete={handleDelete} />;
}
```

**6. useMemo - Memoize Expensive Calculations**
```typescript
function ExpensiveComponent({ items, filter }) {
  // Without useMemo: Recalculates on every render
  const filteredAndSorted = items
    .filter(item => item.name.includes(filter))
    .sort((a, b) => a.name.localeCompare(b.name));
  
  // With useMemo: Only recalculates when items or filter change
  const filteredAndSorted = useMemo(
    () => items
      .filter(item => item.name.includes(filter))
      .sort((a, b) => a.name.localeCompare(b.name)),
    [items, filter]
  );
  
  return (
    <div>
      {filteredAndSorted.map(item => <div key={item.id}>{item.name}</div>)}
    </div>
  );
}
```

**7. Custom Hooks - Reusable Logic**
```typescript
// Custom hook for fetching data
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, [url]);
  
  return { data, loading, error };
}

// Usage
function UserProfile() {
  const { data: user, loading, error } = useFetch('/api/users/1');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  return <div>{user?.name}</div>;
}

// Another custom hook
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });
  
  const setValue = (value) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(error);
    }
  };
  
  return [storedValue, setValue];
}

// Usage
function App() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle Theme: {theme}
    </button>
  );
}
```

---

## Q2: React Component Optimization

**A:**

Performance optimization is crucial for large applications.

### 1. React.memo - Prevent Unnecessary Re-renders
```typescript
// Without memo: Re-renders on every parent update
function UserCard({ user, onSelect }) {
  return (
    <div onClick={() => onSelect(user.id)}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
}

// With memo: Only re-renders if props change
const UserCard = React.memo(function UserCard({ user, onSelect }) {
  return (
    <div onClick={() => onSelect(user.id)}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
});

// Custom comparison function
const UserCard = React.memo(
  function UserCard({ user, onSelect }) { /* ... */ },
  (prevProps, nextProps) => {
    // Return true if props are equal (skip render)
    return prevProps.user.id === nextProps.user.id &&
           prevProps.onSelect === nextProps.onSelect;
  }
);
```

### 2. Virtual Scrolling for Large Lists
```typescript
// Install react-window
import { FixedSizeList } from 'react-window';

function UserList({ users }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      {users[index].name} - {users[index].email}
    </div>
  );
  
  return (
    <FixedSizeList
      height={600}
      itemCount={users.length}
      itemSize={35}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
}
```

### 3. Code Splitting with React.lazy
```typescript
// Lazy load component only when needed
const HeavyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}

// With route-based code splitting
const AdminPanel = React.lazy(() => import('./AdminPanel'));
const UserProfile = React.lazy(() => import('./UserProfile'));

function Router() {
  const [page, setPage] = useState('home');
  
  return (
    <Suspense fallback={<div>Loading page...</div>}>
      {page === 'admin' && <AdminPanel />}
      {page === 'profile' && <UserProfile />}
    </Suspense>
  );
}
```

### 4. Reduce Bundle Size
```bash
# Analyze bundle
npm install --save-dev webpack-bundle-analyzer

# Check unused code
npm install --save-dev purify-css
```

---

## Q3: State Management in React

**A:**

Multiple approaches depending on complexity:

### 1. Local State (useState) - Simple Cases
```typescript
function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### 2. useContext + useReducer - Medium Complexity
```typescript
const AppContext = React.createContext();

function AppProvider({ children }) {
  const [state, dispatch] = useReducer(appReducer, initialState);
  
  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
}

// Usage
function Component() {
  const { state, dispatch } = useContext(AppContext);
  
  return (
    <button onClick={() => dispatch({ type: 'INCREMENT' })}>
      Count: {state.count}
    </button>
  );
}
```

### 3. Redux - Large Applications
```typescript
// Actions
const INCREMENT = 'INCREMENT';
const DECREMENT = 'DECREMENT';

const increment = () => ({ type: INCREMENT });
const decrement = () => ({ type: DECREMENT });

// Reducer
function counterReducer(state = 0, action) {
  switch (action.type) {
    case INCREMENT:
      return state + 1;
    case DECREMENT:
      return state - 1;
    default:
      return state;
  }
}

// Store
import { createStore } from 'redux';
const store = createStore(counterReducer);

// Component
function Counter() {
  const [count, setCount] = useState(store.getState());
  
  useEffect(() => {
    const unsubscribe = store.subscribe(() => {
      setCount(store.getState());
    });
    return unsubscribe;
  }, []);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => store.dispatch(increment())}>+1</button>
      <button onClick={() => store.dispatch(decrement())}>-1</button>
    </div>
  );
}

// With react-redux library (easier)
import { Provider, useDispatch, useSelector } from 'react-redux';

function Counter() {
  const count = useSelector(state => state.counter);
  const dispatch = useDispatch();
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>+1</button>
    </div>
  );
}

function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
}
```

### 4. RTK Query / SWR - Data Fetching
```typescript
// Better for data fetching than Redux
import { useQuery } from '@tanstack/react-query';

function UserList() {
  const { data: users, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: async () => {
      const res = await fetch('/api/users');
      return res.json();
    },
    staleTime: 1000 * 60 * 5,  // Cache for 5 minutes
  });
  
  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return (
    <ul>
      {users?.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
}
```

---

## Q4: TypeScript in React

**A:**

TypeScript adds type safety to React.

### Functional Component with TypeScript:
```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

interface UserCardProps {
  user: User;
  onSelect: (id: number) => void;
  disabled?: boolean;  // Optional prop
}

const UserCard: React.FC<UserCardProps> = ({ user, onSelect, disabled = false }) => {
  return (
    <div onClick={() => onSelect(user.id)} style={{ opacity: disabled ? 0.5 : 1 }}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
};
```

### Typing Hooks:
```typescript
interface FormData {
  name: string;
  email: string;
}

function UserForm() {
  const [form, setForm] = useState<FormData>({ name: '', email: '' });
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.currentTarget;
    setForm(prev => ({ ...prev, [name]: value }));
  };
  
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Handle form submission
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={form.name} onChange={handleChange} />
      <input name="email" value={form.email} onChange={handleChange} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### Typing Redux with TypeScript:
```typescript
// Types
interface AppState {
  counter: number;
  users: User[];
  loading: boolean;
}

// Typed selector
export const selectCounter = (state: AppState) => state.counter;

// Typed dispatch
type AppDispatch = typeof store.dispatch;

// Typed useSelector/useDispatch
export const useAppSelector: TypedUseSelectorHook<AppState> = useSelector;
export const useAppDispatch: () => AppDispatch = useDispatch;

// Component
function Counter() {
  const count = useAppSelector(selectCounter);  // Type: number
  const dispatch = useAppDispatch();  // Typed dispatch
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>+1</button>
    </div>
  );
}
```

---

## Q5: Testing React Components

**A:**

Testing React with **Jest** and **React Testing Library**.

### Unit Test Example:
```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

describe('UserCard Component', () => {
  
  test('renders user information', () => {
    const user = { id: 1, name: 'John', email: 'john@example.com' };
    const mockSelect = jest.fn();
    
    render(<UserCard user={user} onSelect={mockSelect} />);
    
    expect(screen.getByText('John')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });
  
  test('calls onSelect when clicked', async () => {
    const user = { id: 1, name: 'John', email: 'john@example.com' };
    const mockSelect = jest.fn();
    
    render(<UserCard user={user} onSelect={mockSelect} />);
    
    const card = screen.getByText('John').closest('div');
    fireEvent.click(card);
    
    expect(mockSelect).toHaveBeenCalledWith(1);
  });
  
  test('disables card when disabled prop is true', () => {
    const user = { id: 1, name: 'John', email: 'john@example.com' };
    const mockSelect = jest.fn();
    
    const { container } = render(
      <UserCard user={user} onSelect={mockSelect} disabled={true} />
    );
    
    const card = container.firstChild;
    expect(card).toHaveStyle('opacity: 0.5');
  });
});

describe('UserForm Component', () => {
  
  test('updates form state on input change', async () => {
    render(<UserForm />);
    
    const nameInput = screen.getByPlaceholderText('Name');
    await userEvent.type(nameInput, 'John Doe');
    
    expect(nameInput).toHaveValue('John Doe');
  });
  
  test('submits form with data', async () => {
    const mockSubmit = jest.fn();
    render(<UserForm onSubmit={mockSubmit} />);
    
    await userEvent.type(screen.getByPlaceholderText('Name'), 'John');
    await userEvent.type(screen.getByPlaceholderText('Email'), 'john@example.com');
    
    fireEvent.click(screen.getByText('Submit'));
    
    await waitFor(() => {
      expect(mockSubmit).toHaveBeenCalledWith({
        name: 'John',
        email: 'john@example.com'
      });
    });
  });
  
  test('displays error message on invalid submission', async () => {
    render(<UserForm />);
    
    fireEvent.click(screen.getByText('Submit'));
    
    await waitFor(() => {
      expect(screen.getByText('Name is required')).toBeInTheDocument();
    });
  });
});
```

---

## Q6: Common React Patterns

**A:**

### 1. Controlled Component Pattern
```typescript
function SearchUsers() {
  const [searchTerm, setSearchTerm] = useState('');
  const [results, setResults] = useState<User[]>([]);
  
  useEffect(() => {
    if (searchTerm.trim() === '') {
      setResults([]);
      return;
    }
    
    const timer = setTimeout(() => {
      fetch(`/api/users/search?q=${searchTerm}`)
        .then(res => res.json())
        .then(data => setResults(data));
    }, 300);
    
    return () => clearTimeout(timer);
  }, [searchTerm]);
  
  return (
    <div>
      <input
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search users"
      />
      <ul>
        {results.map(user => <li key={user.id}>{user.name}</li>)}
      </ul>
    </div>
  );
}
```

### 2. Render Props Pattern
```typescript
interface RenderPropsExample {
  render: (props: any) => React.ReactNode;
}

function DataConsumer<T>({ render }: RenderPropsExample) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchData().then(data => {
      setData(data);
      setLoading(false);
    });
  }, []);
  
  return render({ data, loading });
}

// Usage
<DataConsumer
  render={({ data, loading }) => 
    loading ? <div>Loading</div> : <div>{data}</div>
  }
/>
```

### 3. Compound Component Pattern
```typescript
interface AccordionProps {
  children: React.ReactNode;
}

interface AccordionItemProps {
  title: string;
  children: React.ReactNode;
}

function Accordion({ children }: AccordionProps) {
  const [expandedIndex, setExpandedIndex] = useState<number | null>(null);
  
  return (
    <div>
      {React.Children.map(children, (child, index) => {
        if (React.isValidElement(child)) {
          return React.cloneElement(child, {
            isExpanded: expandedIndex === index,
            onToggle: () => setExpandedIndex(expandedIndex === index ? null : index)
          } as any);
        }
        return child;
      })}
    </div>
  );
}

function AccordionItem({ title, children, isExpanded, onToggle }: any) {
  return (
    <div>
      <button onClick={onToggle}>{title}</button>
      {isExpanded && <div>{children}</div>}
    </div>
  );
}

// Usage
<Accordion>
  <AccordionItem title="Section 1">Content 1</AccordionItem>
  <AccordionItem title="Section 2">Content 2</AccordionItem>
</Accordion>
```

---

## Quick Reference

### React Hooks Comparison
| Hook | Purpose | When to Use |
|------|---------|-----------|
| useState | State management | Simple local state |
| useEffect | Side effects | API calls, subscriptions |
| useContext | Avoid prop drilling | Shared state across components |
| useReducer | Complex state logic | Multiple state variables |
| useCallback | Memoize functions | Optimize performance |
| useMemo | Memoize values | Expensive calculations |
| useRef | Direct DOM access | Uncontrolled components |

### Performance Checklist
✅ Use React.memo for expensive components  
✅ Use useCallback/useMemo wisely  
✅ Lazy load components with React.lazy  
✅ Use virtual scrolling for long lists  
✅ Avoid inline functions in render  
✅ Split code by route  
✅ Use proper key prop in lists  

---

**Last Updated:** May 8, 2026

