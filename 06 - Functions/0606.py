#%%
def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

print shout("I'M INTERESTED IN SHOUTING")
#%%
def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

print by_three(6)
print by_three(11)