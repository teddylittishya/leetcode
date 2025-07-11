# -*- coding: utf-8 -*-
"""151. Reverse Words in a String.ipynb

# Built in
"""

class Solution:
    def reverseWords(self, s: str)-> str:
         return ' '.join(s.strip().split()[::-1])

"""# 1. List/Array (split and reverse)"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words, i, n = [], 0, len(s)
        while i < n:
            while i < n and s[i] == ' ': i += 1
            start = i
            while i < n and s[i] != ' ': i += 1
            if start < i: words.append(s[start:i])
        return ' '.join(words[::-1])

"""- Algorithm: Parse words into a list, reverse, and join.
- Time Complexity: O(n)

- Space Complexity: O(n)

Notes: This is the most straightforward and readable approach

#2. stack
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        stack, i, n = [], 0, len(s)
        while i < n:
            while i < n and s[i] == ' ': i += 1
            start = i
            while i < n and s[i] != ' ': i += 1
            if start < i: stack.append(s[start:i])
        return ' '.join(reversed(stack))

"""- Algorithm: Push words onto a stack, pop to reverse order.
- Time Complexity: O(n)

- Space Complexity: O(n)

Notes: Functionally similar to the list approach, but explicitly uses stack logic

# Two-Pointer In-Place (Optimal for Mutable Strings)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        res, i, n = [], len(s) - 1, len(s)
        while i >= 0:
            while i >= 0 and s[i] == ' ': i -= 1
            end = i
            while i >= 0 and s[i] != ' ': i -= 1
            if end > i: res.append(s[i+1:end+1])
        return ' '.join(res)

"""- Algorithm: Traverse from end to start, collect words, and build the result
- Time Complexity: O(n)

- Space Complexity: O(n)

Notes: This approach avoids extra space for splitting, but Python strings are immutable, so a new list is still used

# Reverse Entire String, Then Each Word
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        chars = list(s[::-1])
        n = len(chars)
        i = 0
        while i < n:
            if chars[i] != ' ':
                start = i
                while i < n and chars[i] != ' ': i += 1
                chars[start:i] = chars[start:i][::-1]
            else:
                i += 1
        # Remove extra spaces
        res, i = [], 0
        while i < n:
            if chars[i] != ' ':
                start = i
                while i < n and chars[i] != ' ': i += 1
                res.append(''.join(chars[start:i]))
            else:
                i += 1
        return ' '.join(res)

"""- Algorithm: Reverse the whole string, then reverse each word in place.
- Time Complexity: O(n)

- Space Complexity: O(n)

Notes: Mimics the in-place C++/Java approach, but Python strings are immutable

# Deque (Double-Ended Queue)
"""

from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        dq, i, n = deque(), 0, len(s)
        while i < n:
            while i < n and s[i] == ' ': i += 1
            start = i
            while i < n and s[i] != ' ': i += 1
            if start < i: dq.appendleft(s[start:i])
        return ' '.join(dq)

"""- Time Complexity: O(n)

- Space Complexity: O(n)

Notes: Deque is optimal if you want to prepend efficiently.
"""

!pip install tabulate

from tabulate import tabulate

table = [
    ["Split & Reverse", "List/Array", "O(n)", "O(n)", "Most readable in Python"],
    ["Stack", "Stack (list)", "O(n)", "O(n)", "Explicit LIFO, educational"],
    ["Two-Pointer", "None/List", "O(n)", "O(n)", "Efficient, no built-ins, clear logic"],
    ["Reverse String + Words", "List (mutable chars)", "O(n)", "O(n)", "Mimics in-place, best for C++/Java"],
    ["Deque", "deque", "O(n)", "O(n)", "Efficient prepending"],
    ["Recursion", "Call Stack/List", "O(n)", "O(n)", "Elegant, but not practical for large strings"]
]


headers = ["Approach", "Data Structure", "Time Complexity", "Space Complexity", "Notes"]

print(tabulate(table, headers, tablefmt="github"))

