# ANGULAR - COMPREHENSIVE INTERVIEW Q&A

## Expert Level Q&A | Production Experience

---

## Q1: Explain Angular Architecture and Dependency Injection

**A:**

Angular follows a **component-based architecture** with modular design. The core concept is **Dependency Injection (DI)** which provides loose coupling and better testability.

### Architecture Layers:
```
┌─────────────────────────────────────────┐
│       Components & Templates            │
├─────────────────────────────────────────┤
│   Services & Dependency Injection       │
├─────────────────────────────────────────┤
│   Directives, Pipes & Decorators       │
├─────────────────────────────────────────┤
│   RxJS Observables (Reactive)           │
├─────────────────────────────────────────┤
│   HTTP Client & Interceptors            │
├─────────────────────────────────────────┤
│   Routing & State Management            │
└─────────────────────────────────────────┘
```

### Dependency Injection Example:
```typescript
// Service
@Injectable({ providedIn: 'root' })
export class UserService {
  constructor(private http: HttpClient) {}
  
  getUser(id: number): Observable<User> {
    return this.http.get(`/api/users/${id}`);
  }
}

// Component - Angular automatically injects UserService
@Component({
  selector: 'app-user-detail',
  templateUrl: './user-detail.component.html'
})
export class UserDetailComponent implements OnInit {
  user: User;
  
  constructor(private userService: UserService) {}
  
  ngOnInit() {
    this.userService.getUser(1).subscribe(
      user => this.user = user
    );
  }
}
```

### Why DI matters:
- ✅ **Loose Coupling:** Components don't create dependencies
- ✅ **Testability:** Mock services easily in tests
- ✅ **Reusability:** Same service used by multiple components
- ✅ **Single Responsibility:** Each class has one job

---

## Q2: Explain the Component Lifecycle and ngOnInit

**A:**

Angular components have a well-defined lifecycle with hooks at each stage.

### Lifecycle Hooks Order:
```
1. Constructor() → Component instance created
2. ngOnChanges() → @Input properties initialized/changed
3. ngOnInit() → Component initialized (fetch data here)
4. ngDoCheck() → Custom change detection
5. ngAfterContentInit() → Content projected
6. ngAfterContentChecked() → Content checked
7. ngAfterViewInit() → Child views created (fetch DOM here)
8. ngAfterViewChecked() → Child views checked
9. ngOnDestroy() → Component destroyed (cleanup here)
```

### Practical Example:
```typescript
@Component({
  selector: 'app-user-profile',
  template: `
    <div>
      <h2>{{ user?.name }}</h2>
      <p>{{ user?.email }}</p>
    </div>
  `
})
export class UserProfileComponent implements OnInit, OnDestroy {
  @Input() userId: number;
  user: User;
  private subscription: Subscription;
  
  constructor(private userService: UserService) {
    console.log('1. Constructor');
  }
  
  ngOnInit() {
    console.log('3. ngOnInit - Fetch data here');
    this.subscription = this.userService.getUser(this.userId)
      .subscribe(user => this.user = user);
  }
  
  ngAfterViewInit() {
    console.log('7. ngAfterViewInit - Access DOM here');
    // Access child components or template elements
  }
  
  ngOnDestroy() {
    console.log('9. ngOnDestroy - Cleanup subscriptions');
    this.subscription.unsubscribe();  // Memory leak prevention!
  }
}
```

### Key Points:
- ✅ **ngOnInit:** Best place to fetch data, not constructor
- ✅ **ngOnDestroy:** MUST unsubscribe to prevent memory leaks
- ✅ **ngAfterViewInit:** Access template elements via @ViewChild
- ✅ **Never use lifecycle hooks multiple times:** Initialize once, use wisely

---

## Q3: RxJS Observables and Reactive Programming

**A:**

**Observables** are lazy, composable sequences of values over time. Fundamental to Angular.

### Observable vs Promise:
```
Observable               Promise
├─ Lazy (waits for      ├─ Eager (starts immediately)
│  subscription)        │
├─ Multiple values      ├─ Single value
├─ Cancellable          ├─ Not cancellable
├─ Use operators        ├─ Only .then()
└─ Transforms data      └─ Limited transform
```

### Common RxJS Operators:

```typescript
import { Observable } from 'rxjs';
import { map, filter, switchMap, mergeMap, catchError, tap, shareReplay } from 'rxjs/operators';

// 1. MAP - Transform each value
users$.pipe(
  map(user => user.name)  // Extract just the name
).subscribe(name => console.log(name));

// 2. FILTER - Keep only matching values
users$.pipe(
  filter(user => user.status === 'ACTIVE')
).subscribe(user => console.log(user));

// 3. SWITCHMAP - Cancel previous request, start new one
// Perfect for search with auto-complete
this.searchTerm$.pipe(
  switchMap(term => this.userService.search(term))
).subscribe(results => this.results = results);

// 4. MERGEMAP - Keep all requests, merge results
this.userIds$.pipe(
  mergeMap(id => this.userService.getUser(id))
).subscribe(user => console.log(user));

// 5. TAKEUPTO - Backpressure - handle slow consumers
this.dataStream$.pipe(
  bufferCount(100)  // Buffer 100 items
).subscribe(batch => this.processBatch(batch));

// 6. CATCHERROR - Error handling
this.userService.getUser(id).pipe(
  catchError(error => {
    console.error('Error loading user:', error);
    return of(defaultUser);  // Fallback value
  })
).subscribe(user => this.user = user);

// 7. TAP - Side effects (logging, impact check)
this.userService.getUser(id).pipe(
  tap(user => console.log('User loaded:', user)),
  tap(user => this.auditLog.record('USER_LOADED')),
  map(user => user.name)
).subscribe(name => this.displayName(name));

// 8. SHAREREPLAY - Cache and share result
usersCache$ = this.userService.getAllUsers().pipe(
  shareReplay(1)  // Cache 1 emission, reuse for new subscribers
);
```

### Real-world Example - Auto-complete with Debounce:
```typescript
@Component({
  selector: 'app-user-search',
  template: `
    <input [formControl]="searchControl" placeholder="Search users">
    <ul>
      <li *ngFor="let user of filteredUsers$ | async">{{ user.name }}</li>
    </ul>
  `
})
export class UserSearchComponent implements OnInit {
  searchControl = new FormControl();
  filteredUsers$: Observable<User[]>;
  
  constructor(private userService: UserService) {}
  
  ngOnInit() {
    this.filteredUsers$ = this.searchControl.valueChanges.pipe(
      debounceTime(300),           // Wait 300ms after user stops typing
      distinctUntilChanged(),       // Only if value actually changed
      filter(term => term.length > 0),
      switchMap(term => 
        this.userService.search(term).pipe(
          catchError(error => {
            console.error('Search failed:', error);
            return of([]);
          })
        )
      ),
      shareReplay(1)               // Cache results
    );
  }
}
```

---

## Q4: Change Detection Strategy in Angular

**A:**

**Change Detection** is how Angular knows when to update the view. This is a critical performance topic.

### Two Strategies:

```typescript
// 1. DEFAULT - Checks entire component tree on ANY event
@Component({
  selector: 'app-expensive-component',
  template: `{{ computeExpensiveValue() }}`,
  changeDetection: ChangeDetectionStrategy.Default
})
export class ExpensiveComponent {}

// 2. ONPUSH - Only checks if @Input changed or event fired here
@Component({
  selector: 'app-optimized-component',
  template: `{{ data }}`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class OptimizedComponent {
  @Input() data: any;  // Only recheck if this changes
}
```

### Performance Impact:
```
Without OnPush:
- User clicks anywhere in app
- Angular checks ALL components
- Expensive calculations run everywhere
- Performance degrades with component count

With OnPush:
- Only components with changed @Input properties rebuild
- Manual change detection trigger when needed
- 50-80% faster for large applications
```

### When to use OnPush:
```typescript
// ✅ USE ONPUSH when:
// - Component is presentational (receives data via @Input)
// - No side effects in change detection
// - Large lists (many items)
// - Performance is critical

@Component({
  selector: 'app-user-list-item',
  template: `<div>{{ user.name }} - {{ user.email }}</div>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserListItemComponent {
  @Input() user: User;
}

// ❌ DON'T use OnPush when:
// - Component has complex internal state
// - Requires frequent updates from services
// - Uses *ngIf with complex logic
```

---

## Q5: Angular Routing and Route Guards

**A:**

Angular routing is crucial for single-page applications (SPAs).

### Basic Routing Setup:
```typescript
// app-routing.module.ts
const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'users',
    component: UserListComponent,
    canActivate: [AuthGuard]  // Guard route
  },
  {
    path: 'users/:id',
    component: UserDetailComponent,
    canActivate: [AuthGuard],
    canDeactivate: [UnsavedChangesGuard]  // Warn on unsaved changes
  },
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [RoleGuard]
  },
  {
    path: 'users/:id/edit',
    component: UserEditComponent,
    resolve: {  // Pre-fetch data before showing component
      user: UserResolve
    }
  },
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  },
  {
    path: '**',  // Wildcard - must be last
    component: PageNotFoundComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

### Route Guards:

```typescript
// 1. CanActivate - Prevent unauthorized access
@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  
  constructor(private authService: AuthService, private router: Router) {}
  
  canActivate(route: ActivatedRouteSnapshot): boolean {
    if (this.authService.isLoggedIn()) {
      return true;
    }
    this.router.navigate(['/login']);
    return false;
  }
}

// 2. CanDeactivate - Warn before leaving with unsaved changes
export interface ComponentCanDeactivate {
  canDeactivate: () => Observable<boolean> | Promise<boolean> | boolean;
}

@Injectable({ providedIn: 'root' })
export class UnsavedChangesGuard implements CanDeactivate<ComponentCanDeactivate> {
  canDeactivate(
    component: ComponentCanDeactivate
  ): Observable<boolean> | Promise<boolean> | boolean {
    return component.canDeactivate ? component.canDeactivate() : true;
  }
}

// 3. Resolve - Pre-fetch data
@Injectable({ providedIn: 'root' })
export class UserResolve implements Resolve<User> {
  
  constructor(private userService: UserService, private router: Router) {}
  
  resolve(route: ActivatedRouteSnapshot): Observable<User> {
    const userId = route.paramMap.get('id');
    return this.userService.getUser(+userId).pipe(
      catchError(() => {
        this.router.navigate(['/users']);
        return EMPTY;
      })
    );
  }
}

// 4. RoleGuard - Role-based access
@Injectable({ providedIn: 'root' })
export class RoleGuard implements CanActivate {
  
  constructor(private authService: AuthService) {}
  
  canActivate(route: ActivatedRouteSnapshot): boolean {
    const requiredRole = route.data['requiredRole'];
    return this.authService.hasRole(requiredRole);
  }
}
```

### Using Resolved Data:
```typescript
@Component({
  selector: 'app-user-detail',
  template: `<h2>{{ user.name }}</h2>`
})
export class UserDetailComponent implements OnInit {
  user: User;
  
  constructor(private route: ActivatedRoute) {}
  
  ngOnInit() {
    // Data comes from resolve, not from service call
    this.route.data.subscribe(
      (data: { user: User }) => {
        this.user = data.user;
      }
    );
  }
}
```

---

## Q6: Reactive Forms vs Template-driven Forms

**A:**

Angular provides two approaches to handle forms. **Reactive Forms** are more powerful and testable.

### Comparison:

| Aspect | Template-driven | Reactive |
|--------|-----------------|----------|
| **Setup** | Simple, quick | More code, more control |
| **Validation** | In template | In component |
| **Async Operations** | Limited | Full support |
| **Testability** | Harder | Easy |
| **Dynamic Forms** | Difficult | Easy |
| **Performance** | Good | Better |

### Template-driven Form:
```typescript
@Component({
  template: `
    <form #userForm="ngForm" (ngSubmit)="onSubmit(userForm.value)">
      <input name="name" #name="ngModel" [(ngModel)]="user.name" required>
      <span *ngIf="name.invalid">Name is required</span>
      
      <input name="email" #email="ngModel" [(ngModel)]="user.email" email>
      <span *ngIf="email.invalid">Invalid email</span>
      
      <button type="submit" [disabled]="userForm.invalid">Submit</button>
    </form>
  `
})
export class TemplateFormComponent {
  user = { name: '', email: '' };
  
  onSubmit(formValue) {
    console.log(formValue);
  }
}
```

### Reactive Form (Recommended):
```typescript
@Component({
  template: `
    <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
      <input formControlName="name" placeholder="Name">
      <span *ngIf="userForm.get('name')?.invalid">
        Name is required
      </span>
      
      <input formControlName="email" placeholder="Email">
      <span *ngIf="userForm.get('email')?.hasError('email')">
        Invalid email
      </span>
      
      <fieldset formGroupName="address">
        <input formControlName="street" placeholder="Street">
        <input formControlName="city" placeholder="City">
      </fieldset>
      
      <button type="submit" [disabled]="userForm.invalid">
        Submit
      </button>
    </form>
  `
})
export class ReactiveFormComponent implements OnInit {
  userForm: FormGroup;
  
  constructor(private fb: FormBuilder) {}
  
  ngOnInit() {
    this.userForm = this.fb.group({
      name: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      address: this.fb.group({
        street: ['', Validators.required],
        city: ['', Validators.required]
      })
    });
  }
  
  onSubmit() {
    if (this.userForm.valid) {
      console.log(this.userForm.value);
    }
  }
}
```

### Custom Validators:
```typescript
// Custom async validator - Check if email exists
export class EmailValidator {
  static async validate(control: AbstractControl): Promise<ValidationErrors | null> {
    return new Promise<ValidationErrors | null>(resolve => {
      if (!control.value) {
        resolve(null);
        return;
      }
      
      userService.checkEmailExists(control.value).subscribe(exists => {
        if (exists) {
          resolve({ emailExists: true });
        } else {
          resolve(null);
        }
      });
    });
  }
}

// Use custom validator
this.userForm = this.fb.group({
  email: ['', {
    validators: [Validators.required, Validators.email],
    asyncValidators: [EmailValidator.validate]
  }],
  password: ['', Validators.required]
});
```

---

## Q7: State Management in Angular (NGRX)

**A:**

For complex applications, **NGRX** provides Redux-like state management.

### NGRX Architecture:
```
┌──────────────────┐
│   Component      │ Dispatches action
└────────┬─────────┘
         │
         ▼
    ┌─────────────┐
    │   Actions   │ What happened
    └────┬────────┘
         │
         ▼
    ┌─────────────┐
    │  Reducer    │ New state
    └────┬────────┘
         │
         ▼
    ┌─────────────┐
    │   Store     │ Single source of truth
    └────┬────────┘
         │
         ▼
    ┌──────────────┐
    │ Selectors    │ Query state
    └────┬─────────┘
         │
         ▼
    ┌──────────────┐
    │  Component   │ Subscribe to updates
    └──────────────┘
```

### Example - User State Management:

```typescript
// 1. State interface
export interface UserState {
  users: User[];
  selectedUserId: number | null;
  loading: boolean;
  error: string | null;
}

const initialState: UserState = {
  users: [],
  selectedUserId: null,
  loading: false,
  error: null
};

// 2. Actions
export const loadUsers = createAction('[User Page] Load Users');

export const loadUsersSuccess = createAction(
  '[User API] Load Users Success',
  props<{ users: User[] }>()
);

export const loadUsersFailure = createAction(
  '[User API] Load Users Failure',
  props<{ error: string }>()
);

// 3. Effects (Handle side effects like API calls)
@Injectable()
export class UserEffects {
  loadUsers$ = createEffect(() =>
    this.actions$.pipe(
      ofType(loadUsers),
      switchMap(() =>
        this.userService.getUsers().pipe(
          map(users => loadUsersSuccess({ users })),
          catchError(error => of(loadUsersFailure({ error })))
        )
      )
    )
  );

  constructor(
    private actions$: Actions,
    private userService: UserService
  ) {}
}

// 4. Reducer
export const userReducer = createReducer(
  initialState,
  on(loadUsers, state => ({
    ...state,
    loading: true,
    error: null
  })),
  on(loadUsersSuccess, (state, { users }) => ({
    ...state,
    users,
    loading: false
  })),
  on(loadUsersFailure, (state, { error }) => ({
    ...state,
    loading: false,
    error
  }))
);

// 5. Selectors
export const selectUserState = (state: AppState) => state.users;
export const selectAllUsers = createSelector(
  selectUserState,
  (state: UserState) => state.users
);
export const selectUsersLoading = createSelector(
  selectUserState,
  (state: UserState) => state.loading
);
export const selectUsersError = createSelector(
  selectUserState,
  (state: UserState) => state.error
);

// 6. Component usage
@Component({
  selector: 'app-user-list',
  template: `
    <div *ngIf="loading$ | async">Loading...</div>
    <div *ngIf="error$ | async as error">{{ error }}</div>
    <ul>
      <li *ngFor="let user of users$ | async">{{ user.name }}</li>
    </ul>
  `
})
export class UserListComponent implements OnInit {
  users$: Observable<User[]>;
  loading$: Observable<boolean>;
  error$: Observable<string | null>;

  constructor(private store: Store<AppState>) {}

  ngOnInit() {
    this.users$ = this.store.select(selectAllUsers);
    this.loading$ = this.store.select(selectUsersLoading);
    this.error$ = this.store.select(selectUsersError);
    
    this.store.dispatch(loadUsers());
  }
}
```

---

## Q8: Angular Performance Optimization Techniques

**A:**

Key optimization strategies for large Angular applications:

### 1. **OnPush Change Detection**
```typescript
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class UserListItemComponent {
  @Input() user: User;
}
```

### 2. **Lazy Loading Routes**
```typescript
const routes: Routes = [
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule)
  }
];
```

### 3. **Unsubscribe from Observables**
```typescript
// Use takeUntil pattern
private destroy$ = new Subject<void>();

ngOnInit() {
  this.userService.getUsers()
    .pipe(takeUntil(this.destroy$))
    .subscribe(users => this.users = users);
}

ngOnDestroy() {
  this.destroy$.next();
  this.destroy$.complete();
}
```

### 4. **Virtual Scrolling for Large Lists**
```typescript
// Install @angular/cdk
import { ScrollingModule } from '@angular/cdk/scrolling';

@Component({
  template: `
    <cdk-virtual-scroll-viewport itemSize="50" class="list-viewport">
      <div *cdkVirtualFor="let item of items" class="list-item">
        {{ item }}
      </div>
    </cdk-virtual-scroll-viewport>
  `,
  styles: ['.list-viewport { height: 400px; }']
})
export class VirtualListComponent {
  items = Array.from({ length: 10000 }, (_, i) => i);
}
```

### 5. **Async Pipe**
```typescript
// ✅ GOOD: Automatic unsubscribe
<div>{{ data$ | async }}</div>

// ❌ BAD: Manual subscription
ngOnInit() {
  this.userService.getUser(id).subscribe(user => this.user = user);
}
```

### 6. **TrackBy Function in *ngFor**
```typescript
// ✅ EFFICIENT: Only updates changed items
<div *ngFor="let user of users; trackBy: trackByUserId">
  {{ user.name }}
</div>

trackByUserId(index: number, user: User): number {
  return user.id;  // Returns unique identifier
}

// ❌ INEFFICIENT: Recreates all items
<div *ngFor="let user of users">
  {{ user.name }}
</div>
```

### 7. **Code Splitting & Lazy Loading**
```typescript
const routes: Routes = [
  {
    path: 'dashboard',
    loadChildren: () => import('./modules/dashboard/dashboard.module')
      .then(m => m.DashboardModule)
  },
  {
    path: 'reports',
    loadChildren: () => import('./modules/reports/reports.module')
      .then(m => m.ReportsModule)
  }
];
```

---

## Q9: Interceptors and HTTP Error Handling

**A:**

**HTTP Interceptors** are middleware that intercept HTTP requests/responses globally.

### Complete Interceptor Example:

```typescript
// auth.interceptor.ts - Add JWT token to requests
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  
  constructor(private authService: AuthService) {}
  
  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    
    // Add JWT token
    const token = this.authService.getToken();
    if (token) {
      req = req.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`
        }
      });
    }
    
    return next.handle(req);
  }
}

// error.interceptor.ts - Global error handling
@Injectable()
export class ErrorInterceptor implements HttpInterceptor {
  
  constructor(
    private errorService: ErrorService,
    private router: Router,
    private authService: AuthService
  ) {}
  
  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    
    return next.handle(req).pipe(
      catchError((error: HttpErrorResponse) => {
        
        // Handle 401 Unauthorized
        if (error.status === 401) {
          this.authService.logout();
          this.router.navigate(['/login']);
        }
        
        // Handle 403 Forbidden
        if (error.status === 403) {
          this.errorService.showError('Access Denied');
        }
        
        // Handle server errors (5xx)
        if (error.status >= 500) {
          this.errorService.showError('Server Error. Please try again later.');
        }
        
        // Log error
        console.error('HTTP Error:', error);
        
        return throwError(() => error);
      })
    );
  }
}

// logging.interceptor.ts - Log all requests
@Injectable()
export class LoggingInterceptor implements HttpInterceptor {
  
  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    
    const startTime = Date.now();
    console.log(`[HTTP] ${req.method} ${req.url}`);
    
    return next.handle(req).pipe(
      tap(
        event => {
          if (event instanceof HttpResponse) {
            const elapsed = Date.now() - startTime;
            console.log(`[HTTP] ${req.method} ${req.url} - ${event.status} (${elapsed}ms)`);
          }
        },
        error => {
          const elapsed = Date.now() - startTime;
          console.error(`[HTTP] ${req.method} ${req.url} - ERROR (${elapsed}ms)`);
        }
      )
    );
  }
}

// app.module.ts - Register interceptors
@NgModule({
  imports: [HttpClientModule],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: LoggingInterceptor,
      multi: true
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: ErrorInterceptor,
      multi: true
    }
  ]
})
export class AppModule { }
```

---

## Q10: Testing Angular Components

**A:**

Angular testing uses **Jasmine** (test framework) and **Karma** (test runner).

### Component Unit Test Example:

```typescript
describe('UserListComponent', () => {
  let component: UserListComponent;
  let fixture: ComponentFixture<UserListComponent>;
  let userService: jasmine.SpyObj<UserService>;

  beforeEach(async () => {
    // Create mock service
    const mockUserService = jasmine.createSpyObj('UserService', ['getUsers']);

    await TestBed.configureTestingModule({
      declarations: [UserListComponent],
      providers: [
        { provide: UserService, useValue: mockUserService }
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(UserListComponent);
    component = fixture.componentInstance;
    userService = TestBed.inject(UserService) as jasmine.SpyObj<UserService>;
  });

  // Test 1: Component creation
  it('should create', () => {
    expect(component).toBeTruthy();
  });

  // Test 2: Load users on init
  it('should load users on init', () => {
    const mockUsers = [
      { id: 1, name: 'John', email: 'john@example.com' },
      { id: 2, name: 'Jane', email: 'jane@example.com' }
    ];

    userService.getUsers.and.returnValue(of(mockUsers));

    fixture.detectChanges();

    expect(userService.getUsers).toHaveBeenCalled();
    expect(component.users).toEqual(mockUsers);
  });

  // Test 3: Display users in template
  it('should display users in list', () => {
    const mockUsers = [
      { id: 1, name: 'John', email: 'john@example.com' }
    ];

    userService.getUsers.and.returnValue(of(mockUsers));
    fixture.detectChanges();

    const items = fixture.debugElement.queryAll(By.css('.user-item'));
    expect(items.length).toBe(1);
    expect(items[0].nativeElement.textContent).toContain('John');
  });

  // Test 4: Handle errors
  it('should display error when load fails', () => {
    userService.getUsers.and.returnValue(
      throwError(() => new Error('Network error'))
    );

    fixture.detectChanges();

    expect(component.errorMessage).toContain('Network error');
    const errorDiv = fixture.debugElement.query(By.css('.error'));
    expect(errorDiv).toBeTruthy();
  });

  // Test 5: Delete user
  it('should delete user when delete button clicked', () => {
    spyOn(userService, 'deleteUser').and.returnValue(of({}));
    component.users = [{ id: 1, name: 'John', email: 'john@example.com' }];
    fixture.detectChanges();

    component.deleteUser(1);

    expect(userService.deleteUser).toHaveBeenCalledWith(1);
    expect(component.users.length).toBe(0);
  });
});
```

### Service Test Example:

```typescript
describe('UserService', () => {
  let service: UserService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [UserService]
    });

    service = TestBed.inject(UserService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();  // Ensure no outstanding requests
  });

  it('should fetch users', () => {
    const mockUsers = [
      { id: 1, name: 'John', email: 'john@example.com' }
    ];

    service.getUsers().subscribe(users => {
      expect(users.length).toBe(1);
      expect(users[0].name).toBe('John');
    });

    const req = httpMock.expectOne('/api/users');
    expect(req.request.method).toBe('GET');
    req.flush(mockUsers);
  });

  it('should create user', () => {
    const newUser = { name: 'Jane', email: 'jane@example.com' };
    const mockResponse = { id: 2, ...newUser };

    service.createUser(newUser).subscribe(user => {
      expect(user.id).toBe(2);
      expect(user.name).toBe('Jane');
    });

    const req = httpMock.expectOne('/api/users');
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual(newUser);
    req.flush(mockResponse);
  });

  it('should handle HTTP errors', () => {
    service.getUsers().subscribe(
      () => fail('should have failed'),
      (error) => {
        expect(error.status).toBe(500);
      }
    );

    const req = httpMock.expectOne('/api/users');
    req.flush('Server error', { status: 500, statusText: 'Server Error' });
  });
});
```

---

## Key Interview Talking Points

✅ **Component Design Patterns**
- Smart (Container) vs. Dumb (Presentational) components
- Isolate business logic in services
- Keep components focused and testable

✅ **State Management**
- Use NGRX for complex state
- Keep form state with Reactive Forms
- Avoid excessive service state

✅ **Performance Optimization**
- OnPush change detection strategy
- Lazy loading modules and routes
- Unsubscribe from observables
- Virtual scrolling for large lists

✅ **Testing Strategy**
- Test components in isolation with mocked services
- Write integration tests for key flows
- Achieve 80%+ code coverage

✅ **Security**
- Always validate input
- Use Reactive Forms
- Implement HTTPInterceptors for auth

---

## Quick Reference Commands

```bash
# Generate component
ng generate component user-list

# Generate service
ng generate service services/user

# Run tests
ng test

# Build for production
ng build --prod

# Serve with proxy (for API development)
ng serve --proxy-config proxy.conf.json
```

---

**Last Updated:** May 8, 2026

