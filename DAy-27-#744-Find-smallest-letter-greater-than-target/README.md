# LeetCode #744 - Find Smallest Letter Greater Than Target

## 🧩 Problem Statement

Given a sorted list of characters and a target character, return the
smallest character in the list that is strictly greater than the target.

If no character is greater than the target, return the first character
in the list.

## 💡 Approach

I solved this problem using **Binary Search**.

The array is already sorted, so binary search allows us to find the
first character that is strictly greater than the target efficiently.

### Pointer Movement

If:

letters[mid] <= target

then the current character cannot be the answer, so:

low = mid + 1

Otherwise:

letters[mid] > target

so it can be a possible answer, and we search the left half:

high = mid - 1

When the loop finishes, `low` represents the first character greater
than the target.

## 🔄 Wrap Around

If no character is greater than the target, `low` becomes equal to
the length of the array.

To handle this, I use:

low % len(letters)

For example:

letters = ["c", "f", "j"]
target = "j"

low = 3

3 % 3 = 0

Therefore, the answer is:

"c"

## 🧠 Python Solution

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1

        while low <= high:
            mid = (low + high) // 2

            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

        return letters[low % len(letters)]
