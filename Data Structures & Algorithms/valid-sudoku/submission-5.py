from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                target = board[r][c]
                if target == ".":
                    continue
                if target in rows[r] or target in cols[c] or target in boxes[r // 3, c // 3]:
                   return False

                rows[r].add(target)
                cols[c].add(target)
                boxes[r//3,c//3].add(target)
        
        return True

