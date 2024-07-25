import re

def contains_spl_char(input_string):
   
    pattern = re.compile(r'[^a-zA-Z0-9]')
    
   
    if pattern.search(input_string):
        return True
    return False

def main():
    input_string = input("Enter a string: ")
    if contains_spl_char(input_string):
        print("The string contains special characters.")
    else:
        print("The string does not contain any special characters.")

if __name__ == "__main__":
    main()
