# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0 for j in range(3)] for i in range(3)]
        count = 0
        for move in moves:
            if count%2:
                grid[move[0]][move[1]] = -1
            else:
                grid[move[0]][move[1]] = 1
            count+=1
        
        for i in range(len(grid)):
            sum_i = sum(grid[i])
            if sum_i == 3:
                return "A"
            if sum_i == -3:
                return "B"
        
        for j in range(3):
            sum_j = 0
            for i in range(3):
                sum_j += grid[i][j]
            if sum_j == 3:
                return "A"
            if sum_j == -3:
                return "B"
        
        sum_d1 = 0
        sum_d2 = 0
        for j in range(3):
            sum_d1 += grid[j][j]
            sum_d2 += grid[j][2-j]
        if sum_d1 == 3 or sum_d2 == 3:
            return "A"
        if sum_d1 == -3 or sum_d2 == -3:
            return "B"

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

        """brute solution with exact representation"""
        # grid = [['-' for j in range(3)] for i in range(3)]
        # count = 0
        # for move in moves:
        #     if count%2:
        #         grid[move[0]][move[1]] = '0'
        #     else:
        #         grid[move[0]][move[1]] = 'X'
        # def checkPattern():
        #     # check rows
        #     for i in range(3):
        #         count = 1
        #         pattern = grid[i][0]
        #         for j in range(1, 3):
        #             if grid[i][j]==pattern:
        #                 count+=1
        #         if count == 3:
        #             return pattern
        #     # check cols
        #     for j in range(3):
        #         count = 1
        #         pattern = grid[0][j]
        #         for i in range(1, 3):
        #             if grid[i][j]==pattern:
        #                 count+=1
        #         if count == 3:
        #             return pattern
        #     # check diagonal1
        #     pattern = grid[0][0]
        #     count = 0
        #     for i in range(3):
        #         if grid[i][i]==pattern:
        #             count+=1
        #     if count == 3:
        #         return pattern
        #     # check diagonal2
        #     pattern = grid[0][2]
        #     count = 0
        #     for i in range(3):
        #         if grid[i][2-i]==pattern:
        #             count+=1
        #     if count == 3:
        #         return pattern
            
