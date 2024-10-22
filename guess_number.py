from random import randint



while True:
    computer_num = randint(1,100)
    print ('Угадайте число от 1 до 100')
    persons_num = int(input('Введите число:'))
    if persons_num < computer_num:
        print('Ваше число меньше того, что загадано.')

    if persons_num > computer_num:
        print('Ваше число больше того, что загадано.')

    if computer_num == persons_num:
        print('Отличная интуиция! Вы угадали число :)')
        break
