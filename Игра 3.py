import os

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Крестики-нолики\n")
        print("  0   1   2")
        for i in range(3):
            print(f"{i} {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:
                print(" ---+---+---")
    
    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play(self):
        while True:
            self.print_board()
            
            winner = self.check_winner()
            if winner:
                print(f"\nИгрок {winner} победил!")
                break
            
            if self.is_board_full():
                print("\nНичья!")
                break
            
            try:
                print(f"\nХод игрока {self.current_player}")
                row = int(input("Введите строку (0-2): "))
                col = int(input("Введите столбец (0-2): "))
                
                if self.make_move(row, col):
                    self.switch_player()
                else:
                    print("Некорректный ход! Попробуйте еще раз.")
                    input("Нажмите Enter...")
            except ValueError:
                print("Введите числа от 0 до 2!")
                input("Нажмите Enter...")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
