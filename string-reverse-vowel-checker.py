#Awfera Python Programming Course Assignment No 01 - Question No 01 
def clean_user_input(u_input):
    #Remove Numbers, operators or any other Special Characters from the input string, if entered by the user
    cleaned_input = ""
    for char in u_input:
        if char.isalpha() or char.isspace(): 
            cleaned_input += char
        #char.isalpha(): Returns True if char is a letter (A-Z or a-z).
        #char.isspace(): Returns True if char is a space (' ').
        #If either condition is True, the character is included; otherwise, it's ignored.

    return " ".join(cleaned_input.split()) # Remove extra spaces and keep only single space between words
user_input = input("Enter a String: ")
cleaned_user_input = clean_user_input(user_input) # Calls the function clean_user_input and pass user_input as an argment
print(f"Cleaned String: {cleaned_user_input}")


#Method-01: Reverse Input String using Slicing
reversed_string = cleaned_user_input[::-1] #start and stop are left empty, meaning the entire string is considered.step = -1 means we move backward through the string, effectively reversing it.
print(f"Reversed string (using Slicing Method): {reversed_string}")


#Method-02: Reverse Input String using for Loop, Conditions and User-Defined Function
def reverse_string(str):
    if len(str) == 0:
        return str
    else:
        reversed_str = ""
        for char in str:
            reversed_str = char + reversed_str  # Adding each character at the beginning
        return reversed_str

print("Reversed String (using Loop, Condition and User-Defined Function):", reverse_string(cleaned_user_input))

#User-Defined Function to check The number of vowels in the input string
def check_vowels(str):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in str: #iterate each charcter of the cleaned input string 
        if char in vowels: #check whether character is vowel or not
            vowel_count += 1 #add 1 in vowel_count variable if character is vowel
    return vowel_count
        
print(f"Number of vowels in input string '{cleaned_user_input}' is: {check_vowels(cleaned_user_input)}")
