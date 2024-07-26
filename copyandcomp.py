import os
import filecmp

def copy_file(file1, file2):
    if not os.path.exists(file1):
        print(f'File not exists: {file1}')
    else:
        file_1 = open(file1, 'r')
        students = file_1.read()
        file_1.close()
        
        file_2 = open(file2, 'w')
        file_2.write(students)
        file_2.close()
        
        print(f'Success -> Content copied from {file1} to {file2}')

def comp_files(filename1, filename2):
    if not os.path.exists(filename1):
        print(f'Not Exist: {filename1}')
    elif not os.path.exists(filename2):
        print(f'Not Exist: {filename2}')
    else:
        compare = filecmp.cmp(filename1, filename2)
        if compare:
            print('Success -> The files are the same')
        else:
            print('Failure -> The files are different')

def main():
    print("Copy File Content:")
    file1 = input('Enter the name of the file1: ')
    file2 = input('Enter the name of the file2 to be created: ')
    copy_file(file1, file2)
    print()
    print("Compare Files:")
    file1_compare = input('Enter the name of the first file to compare: ')
    file2_compare = input('Enter the name of the second file to compare: ')
    comp_files(file1_compare, file2_compare)

if __name__ == "__main__":
    main()
