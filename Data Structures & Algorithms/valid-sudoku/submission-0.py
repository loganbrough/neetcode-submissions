from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)
        for c in range(9):
            for r in range(9):
                v = board[c][r]
                if v == ".":
                    continue
                box = (r // 3, c // 3)
                if v in rows[r] or v in col[c] or v in boxes[box]:
                    return False
                rows[r].add(v)
                col[c].add(v)
                boxes[box].add(v)
        return True

