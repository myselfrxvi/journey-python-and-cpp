from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        empty_cells = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3, c // 3)].add(val)

        def backtrack(idx: int) -> bool:
            if idx == len(empty_cells):
                return True

            r, c = empty_cells[idx]
            box = (r // 3, c // 3)

            for digit in "123456789":
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box]:
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box].add(digit)

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box].remove(digit)

            return False

        backtrack(0)
