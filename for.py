words = ['Daniel', 'Felipe', 'Joana']
for w in words:
  print(w, len(w))


# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status


# função Range

for i in range(10 + 1):
  print(i)

# Range com indices

for i in range(-10, 100+1, 21):
  print(i)

for i in range(-10, -100-1, -10):
  print(i)


# Pegar os indices de uma sequencia

a = ['Dan', 'Jonas', 'Pereira']
for i in range(len(a)):
  print(i, a[i])