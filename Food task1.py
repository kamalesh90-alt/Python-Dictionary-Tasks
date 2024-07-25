def show(Food):
    print('this are the menu list items \n',Food)
    for i in Food:
        print(i)  
        
def add(Food):
    item=input('enter the item to add in menu')
    Food.append(item)
    for i in Food:
        print(i) 
        
def update(Food):
    update_item=input('enter the item to update').lower()
    pos=int(input('in which position is update:'))
    Food[pos]=update_item
    for i in Food:
        print(i) 
    
def remove(Food):
    item=input('enter the element to remove:').lower()
    Food.remove(item)
    print('item removed successfuly.')





if __name__=="__main__":
    
    Food=['Veg 65','choco chips','cheese burger','chicken sandwitch']
   
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
            show(Food)
        elif option==2:
            add(Food)
        elif option==3:
            update(Food)
        elif option==4:
            remove(Food)
        elif option==5:
            exit()
        else:
            print('your are selecting wrong input.....')