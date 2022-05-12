import random
dice_rolls = 2
dice_sum = 0
for i in range(0,dice_rolls):
  roll = random.randint(1,12)
  dice_sum += roll
  if roll == 1:
    print(f'You rolled a {roll}! Sucks')
  elif roll == 12:
    print(f'You rolled a {roll}! Fire!')
  else:
    print(f'You rolled a {roll}')
print(f'You have rolled a total of {dice_sum}')