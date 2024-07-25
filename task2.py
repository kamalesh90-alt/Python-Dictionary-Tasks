def addofList(list):
    sum=0
    for val in list:
        sum=sum+val
    
    return sum

def maximumNumber(list):
    max_num=0
    for i in list:
        if(i>max_num):
            max_num=i
            
    return max_num




def main():
    list=[]
    size=int(input('enter the size of list:'))
    for i in range(size):
        value=int(input())
        list.append(value)
    print(addofList(list))
    print(maximumNumber(list))

if __name__=="__main__":
    main()