def show(menu):
    print('this are the menu list items \n')
    for i in menu:
        print(menu[i])  
        
def add(menu):
    item=input('enter the item to add in menu')
    menu['Food'].append(item)
    print(menu) 
        
def update(menu):
    print(menu['Food'])
    update_item=input('enter the item to update').lower()
    pos=int(input('in which position is update:'))
    menu['Food'][pos]=update_item
    print(menu['Food'])

    
def remove(menu):
    item=input('enter the element to remove:').lower()
    menu['Food'].remove(item)
    print('item removed successfuly.')
    print(menu['Food'])





if __name__=="__main__":
    menu={
    'Food':['Veg 65','choco chips','cheese burger','chicken sandwitch'],
    
    }
    print('''
          show - 1
          add-2
          update-3
          remove-4
          exit-5
        
          ''')
    while(True):
        option=int(input('enter your option:'))
        if option==1:
            show(menu)
        
        elif option==2:
            add(menu)


        elif option==3:
            update(menu)

        elif option==4:
            remove(menu)  

        else:
            break

            
    