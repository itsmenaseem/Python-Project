import fontstyle
 
def printMultiplicationTable(num):
    print(fontstyle.apply('       Table  of   {}'.format(num),'Bold/Blue'))
    for j in range(1, 11, 1):
  
        print(fontstyle.apply('         {} * {} ='.format(num,j),'faint/yellow'),fontstyle.apply(num * j,'itallic/red'))

class multiplicationTable:
 def __init__(self, __number):
    self.number = number
 def callMultiplicationTable(self):
    for i in range(2, self.number + 1, 1):
        printMultiplicationTable(i)
if __name__ == "__main__":

    number = int(input("Enter the range of table you want : "))
    obj = multiplicationTable(number)
    obj.callMultiplicationTable()