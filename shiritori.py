class Shiritori:
    def __init__(self, words=[], game_over=False):
        self.words = words
        self.game_over = game_over

    def play(self, word):
        if word in self.words:
            self.game_over = True
            return 'game over'

        if len(self.words) == 0:
            self.words.append(word)
        else:
            last_word = self.words[-1]
            last_letter = last_word[-1]
            if last_letter == word[0]:
                self.words.append(word)
            else:
                self.game_over = True
                return 'game over'

        return self.words

    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'


def main():
    my_shiritori = Shiritori()
    a = my_shiritori.play("apple")
    b = my_shiritori.play("ear")
    c = my_shiritori.play("rhino")
    d = my_shiritori.play("corn")
    print(my_shiritori.game_over)


if __name__ == '__main__':
    main()
