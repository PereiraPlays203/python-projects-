print('Digite o código e peso do produto. Digite 0 para encerrar o programa.')

mp = 0
xcod = 0

while True:
    p = int(input('Digite o peso do produto: '))
    if p == 0:
        break
    
    c = int(input('Digite o código do produto: '))
    
    if p > mp:
        mp = p
        xcod = c

print(f'O maior peso é {mp} e o código do produto é {xcod}')