# Day 34 Notes

## Count Commas in Range

### Main Observation

A comma is inserted after every three digits from the right.

Under the problem constraints:

`text
1 → 999

have no commas.

1000 → n

have one comma.

Formula

If:

n < 1000

return:

0

Otherwise:

n - 1000 + 1

Simplify:

n - 999
