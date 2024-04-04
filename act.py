#Era Demeterio
list = []

def showItems():
    x = int(input('Enter No. of Items for List: '))
    for i in range(0,x):
        x = input('Item: ')
        if x.isdigit():
            if(isinstance(x, float)):
                list.append(float(x))
            else:
                list.append(int(x))
        else:
            list.append(x)
    for item in list:
        print(item, end = ' ')

def lenOfList(items):
    return len(items)

def datatypeOfList(items):
    print('\nData type of list: ',type(items))
    print('\nData type of list elements: ')
    for index in items:
        print('\nItem: ',index, 'Datatype: ', type(index), end=' ')

def tupleMake(items):
    tupleList = tuple(items)
    print('\n\nTuple: ',tupleList)
    print('\nNumber of items in Tuple: ', len(tupleList))
    if(len(tupleList)<4):
        tupleList += ('Default','Default','Default')
        
    print('\n\n3rd Index Item in Tuple: ', tupleList[3])
def main():
    print('\nSemifinal Activity 1')
    x = input('\nType yes to continue and no to exit...')
    while x:
        if x.lower() == 'no':
            break
        showItems()
        print('\n\nLength of List: ',lenOfList(list))
        datatypeOfList(list)
        tupleMake(list)
        x = input('\nType yes to continue and no to exit...')
main()




















