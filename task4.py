def count_freq(input_string):
   
    frequency_dict = {}
    
   
    for char in input_string:
       
        char = char.lower()
        
        if char.isalpha():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    
    return frequency_dict

def main():
    
    input_string = input("Enter a string value: ")
    
   
    frequency_dict = count_freq(input_string)
    
    
    for letter, frequency in frequency_dict.items():
        print(f"'{letter}': {frequency}")

if __name__ == "__main__":
    main()
