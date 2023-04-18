import random

class Material:
    data = {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h", "8": "i", "9": "j"}

    barrel = [     "   \o/  < Help!",
                   " ------",
                   "|      |",
                   "|      |",
                   "|      |",
                   " ------ "]
    barrel = "\n".join(barrel)

    def __init__(self):
        self.temp = list(self.data.values())
        random.shuffle(self.temp)
        self.value_shuffled = dict(zip(self.data, self.temp))


class List:
    def __init__(self):
        self.material = Material()
        self.shuffled_dict = self.material.value_shuffled

    def choose(self, a_key):
        return self.shuffled_dict.pop(a_key)


class Game:
    def __init__(self):
        self.list = List()

    def play_game(self):
        self.shuffled_dict = self.list.shuffled_dict
        self.key_list = []
        for res_key in self.shuffled_dict.keys():
            self.key_list.append(res_key)

        while len(self.shuffled_dict) > 0:
            n = input("qで終了、それ以外でPlay:")
            if n == "q":
                break
            print(self.list.material.barrel)
            response = input("{}の中から選んで入力:".format(self.key_list))
            if response in self.key_list:
                p = self.list.choose(response)
                if p == "a":
                    print("ハズレを引きました！")
                    break
                else:
                    self.key_list.remove(response)
            else:
                print("{}の中から正しく入力してください.".format(self.key_list))
        drawing = self.pop_out()

    def pop_out(self):
        self.pop = [
                            "    \ o/    ",
                            "      |     ",
                            "  \  / \   / ",
                            "    ------  ",
                            "   |      | ",
                            "   |      | ",
                            "   |      | ",
                            "    ------  "]
        pop = "\n".join(self.pop)
        print(pop)

game = Game()
game.play_game()