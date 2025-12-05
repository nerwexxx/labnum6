import random
import os

class Puzzle15:
    def __init__(self):
        self.board = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 0]]
        self.empty_pos = (3, 3)
        
    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Головоломка '15'\n")
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    print("   ", end=" ")
                else:
                    print(f"{self.board[i][j]:2d}", end=" ")
            print()
        print("\nУправление: w-вверх, s-вниз, a-влево, d-вправо, q-выход")
    
    def is_solved(self):
        solution = [[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 0]]
        return self.board == solution
    
    def move(self, direction):
        x, y = self.empty_pos
        new_x, new_y = x, y
        
        if direction == 'w' and x < 3:
            new_x = x + 1
        elif direction == 's' and x > 0:
            new_x = x - 1
        elif direction == 'a' and y < 3:
            new_y = y + 1
        elif direction == 'd' and y > 0:
            new_y = y - 1
        else:
            return False
        
        self.board[x][y], self.board[new_x][new_y] = self.board[new_x][new_y], self.board[x][y]
        self.empty_pos = (new_x, new_y)
        return True
    
    def shuffle(self, moves=100):
        directions = ['w', 's', 'a', 'd']
        for _ in range(moves):
            direction = random.choice(directions)
            self.move(direction)
    
    def play(self):
        self.shuffle()
        
        while True:
            self.print_board()
            
            if self.is_solved():
                print("\nПоздравляем! Вы решили головоломку!")
                break
            
            move = input("\nВаш ход: ").lower()
            
            if move == 'q':
                print("Выход из игры")
                break
            
            if move not in ['w', 's', 'a', 'd']:
                print("Некорректный ввод. Используйте w, s, a, d")
                continue
            
            if not self.move(move):
                print("Невозможно сделать такой ход!")

if __name__ == "__main__":
    game = Puzzle15()
    game.play()
