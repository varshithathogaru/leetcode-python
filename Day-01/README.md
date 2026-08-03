# 🚀 Daily Coding Log | Day 1

## Problem no 2347

**Total Distance Traveled**

## Difficulty

Easy

## Language

Python

## Solution

```python
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        extra = min((mainTank - 1) // 4, additionalTank)
        return (mainTank + extra) * 10
```

## Approach

Instead of simulating fuel transfer step by step, I identified a mathematical pattern.

The number of extra liters that can be transferred depends on:

- Fuel consumed from the main tank
- Fuel available in the additional tank

Using:

extra = min((mainTank - 1) // 4, additionalTank)

The total distance becomes:

(mainTank + extra) × 10

## Complexity

Time: O(1)

Space: O(1)

## Key Learning

Sometimes recognizing a mathematical pattern leads to a much cleaner solution than simulating every operation.
