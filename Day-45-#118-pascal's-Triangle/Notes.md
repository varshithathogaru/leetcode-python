
# Day 45 Notes — Pascal's Triangle

## Core Idea

Build every row from the previous row.

## Row Structure

Every row:

- Starts with 1
- Ends with 1
- Middle values come from the previous row

## Formula

```text
current[j] =
previous[j-1] + previous[j]
