import random

def rand_number(lvl):
    if lvl == '1': # легкая сложность - угадать число от 1 до 50
        return random.randint(1, 50), 50, 10
    elif lvl == '2': # нормальная сложность - угадать число от 1 до 100
        return random.randint(1, 100), 100, 5
    elif lvl == '3': # высокая сложность - угадать число от 1 до 500
        return random.randint(1, 500), 500, 3


def game():
    lvl = ''
    user_number = ''

    print('Приветствую тебя в игре "УГАДАЙ ЧИСЛО"!\n'
          'тут будет какая-нибудь предистория ;)')
    print('Настал момент выбрать сложность, готовы ли ты к испытаниям?\n'
          '1) лёгкая            2) нормальная                      3) сложная\n'
          '(пока не совсем      (давай попробуем)        (я и есть сама сложность +=+)\n'
          'готов к испытаниям)')

    while lvl != '1' or lvl != '2' or lvl != '3':
        lvl = input('1, 2, 3?: ')
        if lvl == '1' or lvl == '2' or lvl == '3':
            break

    print('тут какая-нибудь интересная подвязка к началу игры + правила')
    guess_number, max_num, lifes = rand_number(lvl)
    print('ТАК НАЧНЕМ ЖЕ НАШУ ИГРУ!!!\n'
          f'угадай число от 1 до {max_num}')

    while True:
        user_number = int(input('Твоя догадка: '))
        if lifes == 0:
            return print('ты проиграл + история + предложить сыграть еще раз')
        elif user_number != guess_number:
            lifes -= 1
            if user_number > guess_number:
                print('слишком много, попробуй меньше')
            elif user_number < guess_number:
                print('слишком мало, попробуй больше')
            print(f'у тебя осталось: {lifes} ЖИЗНЕЙ')
        elif user_number == guess_number:
            return print('ты победил все дела молодец и нужно как-то закончить историю')


game()
