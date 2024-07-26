
import os
def delete(file):
    if  os.path.exists(file):
        os.remove(file)
        print('file removed successfully')
    else:
        print('the file doesnot exists')
       
def main():
    print('enter the filename to delete: ')
    filename=input()
    delete(filename)

   
if __name__=="__main__":
    main()
 