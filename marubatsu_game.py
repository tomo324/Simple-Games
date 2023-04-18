import random

class Board:

    lattice = [["-", "-", "-"],
               ["-", "-", "-"], 
               ["-", "-", "-"]]

    #3*3の盤面を表示
    def show(self):
        for row in range(3):
            for col in range(3):
                print(self.lattice[row][col], end="")
            print()


class Computer:

    def cpu_choose(self):
        coordinate = [0, 1, 2]
        x = random.choice(coordinate)
        y = random.choice(coordinate)
        return [x, y]


class Game:

    def __init__(self):
        self.board = Board()
        self.computer = Computer()

    def judge(self):
        tile = self.board.lattice
        #終了条件を列記する
        self.exit1 = (tile[0][0] == tile[1][0] == tile[2][0] == "○") or (tile[0][0] == tile[1][0] == tile[2][0] == "×") #縦3列
        self.exit2 = (tile[0][1] == tile[1][1] == tile[2][1] == "○") or (tile[0][1] == tile[1][1] == tile[2][1] == "×")
        self.exit3 = (tile[0][2] == tile[1][2] == tile[2][2] == "○") or (tile[0][2] == tile[1][2] == tile[2][2] == "×")
        self.exit4 = (tile[0][0] == tile[0][1] == tile[0][2] == "○") or (tile[0][0] == tile[0][1] == tile[0][2] == "×") #横3列
        self.exit5 = (tile[1][0] == tile[1][1] == tile[1][2] == "○") or (tile[1][0] == tile[1][1] == tile[1][2] == "×")
        self.exit6 = (tile[2][0] == tile[2][1] == tile[2][2] == "○") or (tile[2][0] == tile[2][1] == tile[2][2] == "×")
        self.exit7 = (tile[0][0] == tile[1][1] == tile[2][2] == "○") or (tile[0][0] == tile[1][1] == tile[2][2] == "×") #斜め2列
        self.exit8 = (tile[2][0] == tile[1][1] == tile[0][2] == "○") or (tile[2][0] == tile[1][1] == tile[0][2] == "×")
        self.exit9 = all([tile[i][j] != "-" for i in range(3) for j in range(3)])  #引き分け
        return self.exit1 or self.exit2 or self.exit3 or self.exit4 or self.exit5 or self.exit6 or self.exit7 or self.exit8 or self.exit9

    def play_game(self):
        print("playerは○, computerは×です。")
        self.board.show()
        while True:
            if self.judge():  #playerとcomputerがボードに記入するたびに終了条件を確認
                break
            else:
                while True:
                    x = input("x座標(0~2)を入力(qで終了):")
                    y = input("y座標(0~2)を入力(qで終了):")
                    if x == y == "q":
                        break
                    elif x not in ["0", "1", "2"] or y not in ["0", "1", "2"]:
                        print("無効な入力です")
                        break
                    else:
                        x = int(x)
                        y = int(y)
                        if self.board.lattice[y][x] != "-":  #重複しないようにする
                            print("重複しています。")
                            continue
                        else:
                            self.board.lattice[y][x] = "○"  #xを横列、yを縦列にできるようにx,yを逆にする
                            break
            if x == y == "q":
                break
            if self.judge():
                break
            else:
                while True:
                    c_list = self.computer.cpu_choose()
                    x = c_list[0]
                    y = c_list[1]
                    if self.board.lattice[y][x] != "-":
                        continue
                    else:
                        self.board.lattice[y][x] = "×"
                        break
            self.board.show()
        print("終了!")
        self.board.show()

game = Game()
game.play_game()