import random
import itertools

Lists = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numList = ['1','2','3','4','5','6','7','8','9','0']

symbolList = ['!','£','$','%','&']

UpperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


Lists1 = int(input('How many characters from List? '))
numList1 = int(input('How many characters from numList? '))
symbolList1 = int(input('How many characters from symbolList? '))
UpperList1 = int(input('How many characters from UpperList? '))
Total = Lists1 + numList1 + symbolList1 + UpperList1


ab1 = []
if Lists1 + numList1 + symbolList1 + UpperList1 < 8:
  print('Not enough characters')

else:

  for i in range(0,Total):
    if Lists and numList and symbolList and UpperList:
      if UpperList1 >= 1 and numList1 >= 1 and symbolList1 >= 1 and Lists1 >= 1:
        ab = itertools.chain(Lists1 * random.choice(Lists),numList1 * random.choice(numList),symbolList1 * random.choice(symbolList),UpperList1 * random.choice(UpperList))
        ab1.append(random.choice(list(ab)))
    else:
      print('bye')
      break

ab2 = ''.join(random.sample(list(ab1),len(list(ab1))))

with open('pass.txt','w') as p:
  p.write(str(ab2))

  print("Your new password is in pass.txt. Bye!")

  p.close()
