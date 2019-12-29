try:
    usr = input().lower()
except EOFError:
    print('Конец файла')
except KeyboardInterrupt:
    print('\nВыход')
else:
    res = list(usr)
    count = 0
    for i in res:
        count += 1
        if count % 2 == 0:
            print(i.capitalize(), end='')
        else:
            print(i, end='')