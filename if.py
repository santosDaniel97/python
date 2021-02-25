n1 = float(input('Digite a nota da P1: '))
n2 = float(input('Digite a nota da P2: '))

media = (n1 + n2) / 2

if media >= 0 and media <= 4:
  print(f'Reprovado com média {media}')
elif media >= 5 and media <= 8:
  print(f'Aprovado com média {media}')
elif media >= 9 or media == 10:
  print(f'PARABÉNS, APROVADO COM MÉDIA {media}')