# DSA Algorithm Template Bank (Python)

Use these templates for coding rounds. Each problem in syntax files maps to one template id.

## T01 HashMap Complement (Two Sum)
```python
def solve(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        y = target - x
        if y in seen:
            return [seen[y], i]
        seen[x] = i
```

## T02 Running Min + Best Answer (Stock)
```python
def solve(nums):
    best, mn = 0, float('inf')
    for x in nums:
        mn = min(mn, x)
        best = max(best, x - mn)
    return best
```

## T03 Prefix + Suffix Products
```python
def solve(nums):
    n, out, p = len(nums), [1] * len(nums), 1
    for i in range(n):
        out[i], p = p, p * nums[i]
    s = 1
    for i in range(n - 1, -1, -1):
        out[i], s = out[i] * s, s * nums[i]
    return out
```

## T04 Kadane
```python
def solve(nums):
    cur = ans = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        ans = max(ans, cur)
    return ans
```

## T05 Two Pointers (Sorted/Ends)
```python
def solve(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        # update answer
        if condition_to_move_left(arr[l], arr[r]):
            l += 1
        else:
            r -= 1
```

## T06 Sliding Window (Variable)
```python
def solve(s):
    l = 0
    state = {}
    ans = 0
    for r, ch in enumerate(s):
        add(state, ch)
        while invalid(state):
            remove(state, s[l]); l += 1
        ans = max(ans, r - l + 1)
    return ans
```

## T07 Monotonic Stack (Next Greater)
```python
def solve(nums):
    st = []
    out = [-1] * len(nums)
    for i, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            out[st.pop()] = i
        st.append(i)
    return out
```

## T08 Parentheses Stack
```python
def solve(s):
    mp, st = {')':'(', ']':'[', '}':'{'}, []
    for ch in s:
        if ch in '([{':
            st.append(ch)
        elif not st or st.pop() != mp[ch]:
            return False
    return not st
```

## T09 Binary Search (Array)
```python
def solve(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return m
        if nums[m] < target: l = m + 1
        else: r = m - 1
    return -1
```

## T10 Binary Search on Answer
```python
def solve(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## T11 Fast/Slow Linked List
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast: return True
    return False
```

## T12 Reverse Linked List
```python
def reverse(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

## T13 Merge Linked Lists
```python
def merge(a, b):
    d = t = ListNode(0)
    while a and b:
        if a.val < b.val: t.next, a = a, a.next
        else: t.next, b = b, b.next
        t = t.next
    t.next = a or b
    return d.next
```

## T14 Tree DFS (Postorder Height)
```python
def dfs(node):
    if not node: return 0
    l = dfs(node.left)
    r = dfs(node.right)
    # update global answer using l, r
    return 1 + max(l, r)
```

## T15 Tree BFS Level Order
```python
from collections import deque

def level_order(root):
    if not root: return []
    q, ans = deque([root]), []
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft(); level.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        ans.append(level)
    return ans
```

## T16 Trie Node
```python
class Trie:
    def __init__(self):
        self.c, self.end = {}, False
```

## T17 Heap (Top K)
```python
import heapq

def top_k(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k: heapq.heappop(h)
    return h[0]
```

## T18 Backtracking (Subsets/Permutations)
```python
def dfs(i, path):
    if base_case(i, path):
        ans.append(path[:]); return
    for choice in choices(i, path):
        apply(choice, path)
        dfs(next_i(i, choice), path)
        undo(choice, path)
```

## T19 Graph DFS/BFS Components
```python
def dfs(u):
    vis.add(u)
    for v in g[u]:
        if v not in vis: dfs(v)
```

## T20 Topological Sort (Kahn)
```python
from collections import deque

def topo(n, edges):
    g = [[] for _ in range(n)]; indeg = [0] * n
    for a, b in edges: g[b].append(a); indeg[a] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    out = []
    while q:
        u = q.popleft(); out.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0: q.append(v)
    return out
```

## T21 Dijkstra
```python
import heapq

def dijkstra(src, g):
    dist = {src: 0}; pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float('inf')): continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

## T22 DP 1D
```python
def solve(n):
    dp = [0] * (n + 1)
    dp[0] = base0
    for i in range(1, n + 1):
        dp[i] = transition(dp, i)
    return dp[n]
```

## T23 DP 2D
```python
def solve(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = transition(dp, i, j)
    return dp[m][n]
```

## T24 Greedy Reachability (Jump Game)
```python
def can_jump(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach: return False
        reach = max(reach, i + x)
    return True
```

## T25 Interval Merge
```python
def merge(intervals):
    intervals.sort()
    out = []
    for s, e in intervals:
        if not out or out[-1][1] < s:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out
```

## T26 Prefix Sum / HashMap Count
```python
def subarray_count(nums, k):
    cnt, pref, mp = 0, 0, {0: 1}
    for x in nums:
        pref += x
        cnt += mp.get(pref - k, 0)
        mp[pref] = mp.get(pref, 0) + 1
    return cnt
```

## T27 Union-Find
```python
parent = {}

def find(x):
    parent.setdefault(x, x)
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb: return False
    parent[pa] = pb
    return True
```

## T28 Bit Tricks
```python
def single_number(nums):
    x = 0
    for n in nums: x ^= n
    return x
```

## T29 Matrix Traversal
```python
def dirs_dfs(r, c):
    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            pass
```

## T30 Math Fast Power
```python
def my_pow(x, n):
    if n < 0: x, n = 1 / x, -n
    ans = 1
    while n:
        if n & 1: ans *= x
        x *= x; n >>= 1
    return ans
```
