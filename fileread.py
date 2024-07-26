import os
import filecmp
def comparefiles(filename1,filename2):
    if(not os.path.exists(filename1)):
        print('not exists:',filename1)
    elif(not os.path.exists(filename2)):
        print('not exists:',filename2)
    else:
        compare=filecmp.cmp(filename1,filename2)

        if compare:
            print('success-> the files are same')
        else:
            print('failure -> the files are different')

def main():
    file_01=input('enter the first file')
    file_02=input('enter the second file')
    comparefiles(file_01,file_02)

    
if __name__ == '__main__':
     main()
             

         