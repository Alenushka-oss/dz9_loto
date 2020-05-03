
from ishodnik import Game, Bag, Card, Computer
if __name__ == '__main__':

    num_compics = int(input('Введите число компьютерных игроков: '))
    num_users = int(input('Введите число живых игроков: '))

    game = Game()
    game.run(num_compics, num_users)

class Bag:
    def stats(self):
        print(f'В мешке {len(self.nums)} бочoнков.')

    def __str__(self):
        str_nums = ''
        for n in sorted(self.nums.copy()):
            str_nums += f'{n}, '
        return f'Всего {len(self.nums)} бочонков: {str_nums}'

    def __eq__(self, other):
        return sorted(self.nums) == sorted(other.nums)

    def __len__(self):
        return len(self.nums)

class Card:
    def show(self):
        print() if i + 1 in (9, 18, 27) else print(' ', end='')
        print('-' * 26, end='\n')

    def __str__(self):
        str_card = f'\n-{self.player_name}{"-" * (26 - len(self.player_name) - 1)}\n'
        for i in range(len(self.card)):
            if self.card[i] is None:
                str_card += '--'
            elif self.card[i] == 0:
                str_card += '  '
            elif self.card[i] < 10:
                str_card += f' {self.card[i]}'
            else:
                str_card += f'{self.card[i]}'
            str_card += '\n' if i + 1 in (9, 18, 27) else ' '
        str_card += '-' * 26 + '\n'
        return str_card

    def __eq__(self, other):
        return sorted(self.card_nums) == sorted(other.card_nums)

    def __len__(self):
        return len(self.card_nums)

class Computer:
    def step(self, num):
      def stats(self):
        print(f'{self.name}. Осталось {len(self.nums)} чисел : {self.nums}')

    def __str__(self):
        str_card = str(self.card)
        return str_card + f'Имя игрока: {self.name}\nОсталось {len(self.nums)} чисел : {sorted(self.nums)}'

    def __eq__(self, other):
        return (sorted(self.nums) == sorted(other.nums)) and (self.is_winner == other.is_winner)

    def __contains__(self, item):
        return True if self.name == item else False

    def __getitem__(self, item):
        return self.nums[item]

    def __len__(self):
        return len(self.nums)


class User(Computer):

    def step(self, num):
            if num in self.card.card_nums:
                self.is_looser = True

    def __str__(self):
        str_card = str(self.card)
        return str_card + f'Имя игрока: {self.name}\nОсталось {len(self.nums)} чисел : {sorted(self.nums)}'

    def __eq__(self, other):
        return (sorted(self.nums) == sorted(other.nums)) and (self.is_winner == other.is_winner)

    def __contains__(self, item):
        return True if self.name == item else False


class Game:

    def __init__(self):
     def step(self, num):
        # удаляем лузеров
        for loser in self.losers:
            self.players.pop(loser.name)
        # удаляем список лузеров, т.к. мы их только что удалили
        self.losers = []

    def cards_show(self):
     def check_winner(self):

        return False

    def __str__(self):
        str_resume = f'\nПАРАМЕТРЫ ИГРЫ:\nЧисло игроков: {self.num_users + self.num_compics}\n' \
                    f'- людей: {self.num_users}\n- компьютеров: {self.num_compics}\n' \
                    f'Число боченков: {len(self.bag.nums)}\nНомеров в каждой карточке: {15}\n' \
                    f'Чило победителей: {len(self.winners)}\nИмена победителей: {self.winners}\n' \
                    f'Чило проигравших: {len(self.losers)}\nИмена проигравших: {self.losers}\n'

        return str_resume

    def __eq__(self, other):
        return (self.num_users == other.num_users) \
               and (self.num_compics == other.num_compics) \
               and (self.winners == other.winners) \
               and (self.losers == other.losers) \
               and (self.bag == other.bag) \
               and (self.players == other.players)

    def __len__(self):
        return len(self.players)


if __name__ == '__main__':
    pass
    import copy
