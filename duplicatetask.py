import os
import filecmp

def compare_files(filename1, filename2):
    if not os.path.exists(filename1):
        print(f'File not exists')
        return False
    elif not os.path.exists(filename2):
        print(f'File not exists')
        return False
    else:
        compare = filecmp.cmp(filename1, filename2)
        if compare:
            print('The files are the same')
        else:
            print('The files are different')
        return compare

def delete_file(filename):
    if not os.path.exists(filename):
        print(f'File not exists')
    else:
        os.remove(filename)
        print(f'{filename} has been deleted')

def main():
    print("Compare Files:")
    file1_compare = input('Enter the name of the first file to compare: ')
    file2_compare = input('Enter the name of the second file to compare: ')
    if compare_files(file1_compare, file2_compare):
        delete_file(file1_compare)
        print(f'{file1_compare} has been deleted since the files were the same.')

if __name__ == "__main__":
    main()
