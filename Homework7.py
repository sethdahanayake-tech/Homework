def check_char_ascii():
    char = input("Enter a single character: ")
    
    # Ensure the user entered exactly one character
    if len(char) != 1:
        print("Please enter exactly one character.")
        return
        
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}")

check_char_ascii()

