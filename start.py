with open(r'spam.txt', 'w') as file:
    file.write('YO!')
    file.flush()
    fd = file.fileno()
    print(fd)
    print('lol')
