with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.write('halo'))

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('halo')

with open('text.txt', 'a') as f:
    f.write('lol')
