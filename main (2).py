#1. Find the second-largest unique element in an array without using sort() or max().
def second_largest(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
# Time: O(n) | Space: O(1)


#2. Find all pairs in an array whose sum equals a given target.

def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        comp = target - num
        if comp in seen:
            pairs.add((min(num, comp), max(num, comp)))
        seen.add(num)
    return list(pairs)
# Time: O(n) | Space: O(n)

#3. Move all zeros to the end of an array without changing the order of other elements.

def move_zeros(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums
# Time: O(n) | Space: O(1)

#4. Find the missing number from an array containing numbers from 1 to N.

def missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)
# Time: O(n) | Space: O(1)

#5. Find all duplicate elements in a list without using nested loops.

def find_duplicates(nums):
    seen = set()
    dups = set()
    for num in nums:
        if num in seen:
            dups.add(num)
        seen.add(num)
    return list(dups)
# Time: O(n) | Space: O(n)

#6. Find the first non-repeating character in a string.

from collections import Counter

def first_unique_char(s):
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return ch
    return None
# Time: O(n) | Space: O(1) (at most 26/256 chars)

#7. Check whether two strings are anagrams without using sorted().

from collections import Counter

def is_anagram(s1, s2):
    return len(s1) == len(s2) and Counter(s1) == Counter(s2)
# Time: O(n) | Space: O(1)

#8. Merge two sorted arrays without using sort().

def merge_sorted(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res
# Time: O(m + n) | Space: O(m + n)

#9. Rotate an array to the right by K positions.

def rotate_right(nums, k):
    n = len(nums)
    k %= n
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums
# Time: O(n) | Space: O(1)

#10. Find the intersection of two arrays, including duplicate occurrences.

from collections import Counter

def intersect(nums1, nums2):
    counts = Counter(nums1)
    res = []
    for num in nums2:
        if counts[num] > 0:
            res.append(num)
            counts[num] -= 1
    return res
# Time: O(m + n) | Space: O(min(m, n))

#11. Find the maximum sum of a contiguous subarray.

def max_subarray_sum(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
# Time: O(n) | Space: O(1)

#12. Find the longest substring without repeating characters.

def length_of_longest_substring(s):
    seen = {}
    left = max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
# Time: O(n) | Space: O(min(n, charset))

#13. Find the longest common prefix among multiple strings.

def longest_common_prefix(strs):
    if not strs:
        return ""
    for i, ch in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != ch:
                return strs[0][:i]
    return strs[0]
# Time: O(S) where S is sum of all characters | Space: O(1)

#14. Group a list of strings into anagram groups.

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
# Time: O(n * k log k) | Space: O(n * k)

#15. Find the Kth largest element in an unsorted array.

import heapq

def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
# Time: O(n log k) | Space: O(k)

#16. Check whether a given string contains balanced parentheses using a stack.

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
# Time: O(n) | Space: O(n)

#17. Find all subarrays whose sum equals a given target.

from collections import defaultdict

def find_subarrays_sum(nums, target):
    prefix_map = defaultdict(list)
    prefix_map[0].append(-1)
    curr_sum = 0
    result = []
    for i, num in enumerate(nums):
        curr_sum += num
        if (curr_sum - target) in prefix_map:
            for start_idx in prefix_map[curr_sum - target]:
                result.append(nums[start_idx + 1 : i + 1])
        prefix_map[curr_sum].append(i)
    return result
# Time: O(n + number of subarrays) | Space: O(n)

#18. Merge overlapping intervals in a list.

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
# Time: O(n log n) | Space: O(n)

#19. Search for an element in a rotated sorted array.

def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
# Time: O(log n) | Space: O(1)

#20. Find the longest consecutive sequence in an unsorted array.

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr = num
            streak = 1
            while curr + 1 in num_set:
                curr += 1
                streak += 1
            longest = max(longest, streak)
    return longest
# Time: O(n) | Space: O(n)

#21. Find the trapped rainwater between elevation bars.

def trap(height):
    l, r = 0, len(height) - 1
    left_max = right_max = water = 0
    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max, height[l])
            water += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            r -= 1
    return water
# Time: O(n) | Space: O(1)

#22. Find the median of two sorted arrays in O(log(m+n)) time. 23. Find the maximum product of a contiguous subarray.

def find_median_sorted_arrays(A, B):
    if len(A) > len(B):
        A, B = B, A
    m, n = len(A), len(B)
    l, r = 0, m
    while l <= r:
        i = (l + r) // 2
        j = (m + n + 1) // 2 - i
        max_left_A = float('-inf') if i == 0 else A[i - 1]
        min_right_A = float('inf') if i == m else A[i]
        max_left_B = float('-inf') if j == 0 else B[j - 1]
        min_right_B = float('inf') if j == n else B[j]

        if max_left_A <= min_right_B and max_left_B <= min_right_A:
            if (m + n) % 2 == 0:
                return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2
            return max(max_left_A, max_left_B)
        elif max_left_A > min_right_B:
            r = i - 1
        else:
            l = i + 1
# Time: O(log(min(m, n))) | Space: O(1)

#24. Find the smallest missing positive integer from an unsorted arra

def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target_idx = nums[i] - 1
            nums[i], nums[target_idx] = nums[target_idx], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
# Time: O(n) | Space: O(1)
#25. Count the number of subarrays whose sum equals K.

from collections import defaultdict

def subarray_sum_count(nums, k):
    count = 0
    curr_sum = 0
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    for num in nums:
        curr_sum += num
        count += prefix_counts[curr_sum - k]
        prefix_counts[curr_sum] += 1
    return count
# Time: O(n) | Space: O(n)

#26. Find the longest increasing subsequence in an array.

import bisect

def length_of_lis(nums):
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)
# Time: O(n log n) | Space: O(n)

#27. Solve the Coin Change problem using dynamic programming.

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != float('inf') else -1
# Time: O(amount * len(coins)) | Space: O(amount)

#28. Solve the Word Break problem using dynamic programming.

def word_break(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]
# Time: O(n^2) | Space: O(n)

#29. Find the minimum number of jumps required to reach the last index.

def jump(nums):
    jumps = farthest = current_end = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
# Time: O(n) | Space: O(1)

#30. Find the maximum profit from buying and selling stocks with multiple transactions.

def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
# Time: O(n) | Space: O(1)

#31. Implement an LRU Cache with O(1) time complexity for get() and put().

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
# Time: O(1) | Space: O(capacity)

#32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
# Time: O(1) | Space: O(n)

#33. Find the number of islands in a 2D matrix using DFS or BFS.

def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
    return islands
# Time: O(R * C) | Space: O(R * C)

#34. Find the shortest path in a weighted graph using Dijkstra's algorithm.

import heapq

def dijkstra(graph, start):
    # graph format: {node: [(neighbor, weight), ...]}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]:
            continue
        for v, weight in graph[u]:
            dist = curr_dist + weight
            if dist < distances[v]:
                distances[v] = dist
                heapq.heappush(pq, (dist, v))
    return distances
# Time: O((V + E) log V) | Space: O(V + E)

#35. Detect a cycle in a directed and undirected graph.

# Directed Graph
def has_cycle_directed(n, adj):
    state = [0] * n
    def dfs(u):
        state[u] = 1
        for v in adj[u]:
            if state[v] == 1 or (state[v] == 0 and dfs(v)):
                return True
        state[u] = 2
        return False
    return any(state[i] == 0 and dfs(i) for i in range(n))

# Undirected Graph
def has_cycle_undirected(n, adj):
    visited = set()
    def dfs(u, parent):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                if dfs(v, u): return True
            elif v != parent:
                return True
        return False
    return any(i not in visited and dfs(i, -1) for i in range(n))
# Time: O(V + E) | Space: O(V)

#36. Implement topological sorting for a directed acyclic graph.

from collections import deque

def topological_sort(num_vertices, edges):
    adj = [[] for _ in range(num_vertices)]
    in_degree = [0] * num_vertices
    for u, v in edges:  # directed edge u -> v
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(num_vertices) if in_degree[i] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return order if len(order) == num_vertices else []
# Time: O(V + E) | Space: O(V + E)

#37. Solve the N-Queens problem using backtracking.

def solve_n_queens(n):
    res = []
    board = [['.'] * n for _ in range(n)]
    cols, pos_diag, neg_diag = set(), set(), set()

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            cols.add(c); pos_diag.add(r + c); neg_diag.add(r - c)
            board[r][c] = 'Q'
            backtrack(r + 1)
            cols.remove(c); pos_diag.remove(r + c); neg_diag.remove(r - c)
            board[r][c] = '.'

    backtrack(0)
    return res
# Time: O(N!) | Space: O(N^2)

#38. Generate all permutations of a given string or array without duplicates.

def permute_unique(items):
    is_str = isinstance(items, str)
    arr = sorted(items)
    res = []
    used = [False] * len(arr)

    def backtrack(path):
        if len(path) == len(arr):
            res.append("".join(path) if is_str else path[:])
            return
        for i in range(len(arr)):
            if used[i] or (i > 0 and arr[i] == arr[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(arr[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return res
# Time: O(N * N!) | Space: O(N)

#39. Serialize and deserialize a binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = iter(data.split(","))
        def dfs():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
# Time: O(N) | Space: O(N)

#40. Find the lowest common ancestor of two nodes in a binary tre
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right
# Time: O(N) | Space: O(H) where H is tree height

