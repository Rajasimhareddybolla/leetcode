class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board_r = {}
        board_c = {}
        quad = {}
        for i in range(0 , 9):
            for j in range(0 , 9):
                if board[i][j] != '.':
                    ele= board[i][j]
                    if i in board_r:
                        if ele in board_r[i]:
                            return False
                    else:
                        board_r[i] = set()
                    board_r[i].add(ele)
                    if j in board_c:
                        if ele in board_c[j]:
                            return False
                    else:
                        board_c[j] = set()
                    board_c[j].add(ele)
                    q_r = i // 3 
                    q_c = j // 3
                    if (q_r , q_c) in quad:
                        if ele in quad[(q_r , q_c)]:
                            return False
                    else:
                        quad[(q_r , q_c)] = set()
                    quad[(q_r , q_c)].add(ele)
        return True