
def addItem(sandwitch):

    size = int(input('How Many item do you want :'))
    for i in range(size):
        add_item = input('Enter the Item sandwitch : ')
        if not add_item in sandwitch:
            sandwitch.append(add_item)
        else:
            print('already it has exists')

def showItem(*sandwitch):
    print('\nSandwich contains')
    for xtra in sandwitch:
        print(xtra)

def main():
    
    sandwitch = []

    addItem(sandwitch)

    showItem(*sandwitch)

if __name__ == '__main__':
    main()