import random

class CardTransformer:
    """Класс для преобразования карточек"""

    def __init__(self, card, player_type):
        self._card = [str(x) for x in card]
        self._player_type = player_type

    # Создание новой карточки
    def create_card(self):
        self._new_card = ['' for i in range(27)]
        self.__card_pos = []
        self.__card_row_pos = []
        self.__card_numbers = []
        self.__random_int = 0
        # Определяем заполненные позиции в строках
        for i in range(1, 4):
            self.__card_row_pos = []
            for j in range(1, 6):
                if j == 1:
                    self.__card_row_pos.append(random.randint(0, 8))
                else:
                    self.__random_int = random.randint(0, 8)
                    while self.__random_int in self.__card_row_pos:
                        self.__random_int = random.randint(0, 8)
                    self.__card_row_pos.append(self.__random_int)
            self.__card_pos += [x + (i - 1) * 9 for x in sorted(self.__card_row_pos)]
        # Определяем 15 чисел в карточке
        for i in range(1, 16):
            self.__random_int = random.randint(1, 90)
            while self.__random_int in self.__card_numbers:
                self.__random_int = random.randint(1, 90)
            self.__card_numbers.append(self.__random_int)
        self.__card_numbers = sorted(self.__card_numbers[0:5]) + sorted(self.__card_numbers[5:10]) + sorted(self.__card_numbers[10:15])
        # Сборка новой карточки
        for i, x in zip(self.__card_pos, self.__card_numbers):
            self._new_card[i] = x
        # print(self.__card_pos)
        # print(self.__card_numbers)
        # print(self._new_card)
        return self._new_card

    # Печать карточки
    def print_card(self):
        if self._player_type == 'Игрок':
            self._card_view = '-----------Ваша карточка-----------\n'
        elif self._player_type == 'Компьютер':
            self._card_view = '--------Карточка компьютера--------\n'
        else:
            self._card_view = '-----------------------------------\n'
        for i, x in enumerate(self._card):
            if len(x) == 2:
                if i not in [8, 17, 26]:
                    self._card_view += (str(x) + '  ')
                else:
                    self._card_view += (str(x) + '\n')
            elif len(x) == 1:
                if i not in [8, 17, 26]:
                    self._card_view += (' ' + str(x) + '  ')
                else:
                    self._card_view += (' ' + str(x) + '\n')
            else:
                if i not in [8, 17, 26]:
                    self._card_view += ('  ' + '  ')
                else:
                    self._card_view += ('  ' + '\n')
        self._card_view += '-----------------------------------'
        print(self._card_view)

    # Проверка есть ли число в карточке
    def check_card(self, card_value):
        self._card_value = card_value
        if str(card_value) in self._card:
            return 1
        else:
            return 0

    # Вычеркивание числа из карточки
    def change_card(self, card_value):
        if (str(card_value) in self._card):
            self.__value_ind = self._card.index(str(card_value))
            self._card.pop(self.__value_ind)
            self._card.insert(self.__value_ind, '-')
        return self._card

    # Сколько чисел осталось в карточке
    def card_free_value(self):
        self.__free_value = self._card.count('-')
        return 15 - self.__free_value


class KegTransformer:
    """Класс для бочонков"""

    def __init__(self, kegs):
        self._kegs = kegs

    # Выбор бочонка
    def keg_select(self):
        self.__random_int = random.randint(0, len(self._kegs) - 1)
        self._keg_value = self._kegs[self.__random_int]
        self._kegs.pop(self.__random_int)
        return self._keg_value, self._kegs


class LotoGame:
    """Игра в лото"""

    def __init__(self, human_player, computer_player):
        self._human_player = human_player
        self._computer_player = computer_player

    def start(self):
        self.__game_over = 0
        self.__kegs = [x for x in range(1, 91)]
        self._human_player_list = self._human_player.create_card()
        self._computer_player_list = self._computer_player.create_card()

        while self.__game_over != 1:
            for i in range(0, 90):
                self.__kegs_class = KegTransformer(self.__kegs)
                self.__kegs_tuple = self.__kegs_class.keg_select()
                if self.__kegs_tuple[0] == 11:
                    print(f'Новый бочонок: {self.__kegs_tuple[0]} !!!БАРАБАННЫЕ ПАЛОЧКИ!!! (осталось {len(self.__kegs_tuple[1])})')
                elif self.__kegs_tuple[0] == 22:
                    print(f'Новый бочонок: {self.__kegs_tuple[0]} !!!ГУСИ-ЛЕБЕДИ!!! (осталось {len(self.__kegs_tuple[1])})')
                elif self.__kegs_tuple[0] == 44:
                    print(f'Новый бочонок: {self.__kegs_tuple[0]} !!!СТУЛЬЧИКИ!!! (осталось {len(self.__kegs_tuple[1])})')
                elif self.__kegs_tuple[0] == 77:
                    print(f'Новый бочонок: {self.__kegs_tuple[0]} !!!ТОПОРИКИ!!! (осталось {len(self.__kegs_tuple[1])})')
                else:
                    print(f'Новый бочонок: {self.__kegs_tuple[0]} (осталось {len(self.__kegs_tuple[1])})')
                CardTransformer(self._human_player_list, 'Игрок').print_card()
                CardTransformer(self._computer_player_list, 'Компьютер').print_card()
                self.__kegs_class = KegTransformer(self.__kegs_tuple[1])
                self.__human_answer = input('Зачеркнуть цифру? (y/n) ').upper()
                if self.__human_answer not in ['Y', 'N']:
                    self.__game_over = 1
                    self.__game_over_txt = 'Game over...'
                    break
                else:
                    self.__human_check = CardTransformer(self._human_player_list, 'Игрок').check_card(self.__kegs_tuple[0])
                    self.__computer_check = CardTransformer(self._computer_player_list, 'Компьютер').check_card(self.__kegs_tuple[0])
                    if (self.__human_answer == 'Y' and self.__human_check == 0) or (self.__human_answer == 'N' and self.__human_check == 1):
                        self.__game_over = 1
                        self.__game_over_txt = 'Вы проиграли...'
                        break
                    else:
                        self._human_player_list = CardTransformer(self._human_player_list, 'Игрок').change_card(self.__kegs_tuple[0])
                        self._computer_player_list = CardTransformer(self._computer_player_list, 'Компьютер').change_card(self.__kegs_tuple[0])
                        self.__human_free_value = CardTransformer(self._human_player_list, 'Игрок').card_free_value()
                        self.__computer_free_value = CardTransformer(self._computer_player_list, 'Компьютер').card_free_value()
                        if (self.__computer_free_value == 0 and self.__human_free_value > 0):
                            self.__game_over = 1
                            self.__game_over_txt = 'Вы проиграли...'
                            break
                        elif (self.__computer_free_value > 0 and self.__human_free_value == 0):
                            self.__game_over = 1
                            self.__game_over_txt = 'Вы выиграли!!!'
                            break
                        elif (self.__computer_free_value == 0 and self.__human_free_value == 0):
                            self.__game_over = 1
                            self.__game_over_txt = 'Ничья!!!'
                            break

        print(self.__game_over_txt)



human_player = CardTransformer([], 'Игрок')
computer_player = CardTransformer([], 'Компьютер')
game = LotoGame(human_player, computer_player)
game.start()
