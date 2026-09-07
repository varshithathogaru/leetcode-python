# Day 33 - Contains Duplicate II

## LeetCode #219

### Problem

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` such that:


nums[i] == nums[j]
abs(i-j)<=k 
return True
else return False

Approach

Use a hash map to store the most recent index of each number.

For every element:

Check whether the number already exists in the dictionary.
If it exists, calculate the distance between the current index and previous index.
If the distance is less than or equal to k, return True.
Otherwise, update the number's index.
If no nearby duplicate is found, return False.
