nota1 = float(input('Digite a NP1: '))
nota2 = float(input('Digite a NP2: '))

media = (nota1 + nota2) / 2

if(media > 0 and media < 4):
    print('REPROVADO!')
    print(f'Media = {media}')
elif(media > 5 and media < 8):
    print('APROVADO')
    print(f'Media = {media}')
elif(media > 8):
    print('APROVADO COM FOLGA')
    print(f'Media = {media}')

