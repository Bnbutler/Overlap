import random

def list_overlap():

  lista = []
  listb = []
  
  lista = random.sample(range(100),10)
  print(f'1 {lista}')
  listb = random.sample(range(100),10)
  print(f'2 {listb}')
  newlist = [num for num in lista if num in listb]
  print(f'3 {newlist}')

  return newlist

result=list_overlap()
print(result)