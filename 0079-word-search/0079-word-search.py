class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordCounter = Counter(word)
        boardCounter = Counter()
        for row in range(len(board)):
            for col in range(len(board[0])):
                boardCounter[board[row][col]] += 1
            
        for char in wordCounter:
            if wordCounter[char] > boardCounter[char]:
                return False   
                
        if wordCounter[word[0]] > wordCounter[word[-1]]:
            word = word[::-1]
            
        def match(row, col, i):
            if i == len(word):
                return True
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return False
            returnVal = False
            if board[row][col] == word[i]:
                board[row][col] = "_"
                if (
                    match(row + 1, col, i + 1) or
                    match(row - 1, col, i + 1) or
                    match(row, col + 1, i + 1) or
                    match(row, col - 1, i + 1)
                ):
                    returnVal = True
                board[row][col] = word[i]
            return returnVal
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if match(row, col, 0):
                    return True
        return False