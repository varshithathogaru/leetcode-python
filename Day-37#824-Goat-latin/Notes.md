# Day 38 Notes — Goat Latin

## LeetCode
#824 - Goat Latin

## Pattern
String Manipulation + Simulation

## Rules

### Vowel
Keep the word unchanged and add `ma`.

Example:

apple → applema

### Consonant
Move first character to the end and add `ma`.

Example:

goat → oatgma

### Position
Add `a` based on the word position.

1st word → a
2nd word → aa
3rd word → aaa

## Important Python

```python
word[0]

First character.

word[1:]

Everything except first character.

"a" * i

Creates i number of as.

enumerate(words, start=1)

Gives positions starting from 1.
