def exercise_1():
    print("Exercise 1 \n Given two integer numbers, return their product only if the \n product is equal to or lower than 1000. Otherwise, return their sum")
    calc1()

def calc1():
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))

    while(True):
        try:
            if a * b >= 1000:
                print(a + b)
                break
            elif a * b < 1000:
                print(a *b)
                break
        except ValueError:
            print("Invalid input. Please input a valid integer")
             
def exercise_2():
    print("Exercise 02: \n Enter two numbers and get a list of the sum of each of the previous number.")
    calc()

def calc():

    #loop to handle user input
    while True:
        try:
            a = int(input("Enter the lower limit: "))
            b = int(input("Enter the upper limit: "))
            if a >= b:
                print("Upper limit must be greater than lower limit. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter integers only.")

    # Initialize previous number and current number, using the given range
    if a == 0:
        previous_number = 0
    else:
        previous_number = a - 1
    current_number = a

    # Iterate through the numbers in the given range
    for i in range(a, b):
        print(current_number + previous_number)
        
        # Update previous number and current number for the next iteration
        previous_number = current_number
        current_number += 1

def exercise_3():
    print("Enter a string and get the characters at even indices.")
    given_string = input("Enter a string: ")
    print(evenIndex(given_string))

def evenIndex(text):
    # Collect characters at even indices
    return [text[i] for i in range(len(text)) if i % 2 == 0]

def exercise_4():
    print("Enter a string and get a modified string.")
    text = input("Enter a string: ")
    while (True):
        try:
            num = int(input("Enter a number: "))
            if num > len(text) or num < 0:
                print("Number given must be a positive number that is less than the length of the string given.")
            else:
                print(text[num:])
                break
        except ValueError:
            print("Invalid input. Please enter a valid number")


def exercise_5():
    print("Returns the result of the comparison of the first and last element in an array.")
    numbers_x = [10, 20, 30, 40, 10]
    numbers_y = [75, 65, 35, 75, 30]
    numbers_z = []
    print(numbers_x)
    print(f"Result is " + str(check(numbers_x)))

def check(nums):
    # Check if the list is empty
    if not nums:
        return None  # or True, depending on how you want to handle an empty list
    
    # Compare the first and last elements
    return nums[0] == nums[-1]

def exercise_6():
    print("Given a list, prints all the numbers divisible by a given number")
    num = int(input("Enter a number/dividend: "))
    nums = [12,7,25,34,46,19,3,28,39,50,22,17,8,44,31,10,27,4,36,14,42,18,29,1,23]
    print(nums)
    divideByFive(nums,num)

def divideByFive(nums,num):
    for i in nums:
        if i % num == 0:
            print(i)

def exercise_7():
    given_text = "Emma is good developer. Emma is a writer. Emma is also a tennis player"
    sub_text = "a"
    count(given_text,sub_text)

def count(given_text,sub_text):
    count = 0
    start = 0
    
    while True:
        start = given_text.find(sub_text, start)
        if start == -1:
            break
        count += 1
        start += len(sub_text)  # Move past the last found occurrence
    print(f"The substring '{sub_text}' appears {count} times in the string: " + given_text)

def exercise_8():
    print("PrettyPrint")
    num = int(input("Enter a number: "))
    """
    for i in range(1,6):
        ls = []
        for k in range(i):
            ls.append(i)
        print(ls)

    """
    for i in range(1, num + 1):
        
        print(' '.join([str(i)] * i))

def exercise_9():
    print("Enter text to check if it's a palindrome.")
    given_text = input("Enter text: ")
    if checkpalidrome(given_text) is True:
        print("The given number " + str(given_text) + " is a palindrome")
    else:
        print("The given number " + str(given_text) + " is not a palindrome")

def checkpalidrome(text):
    return text == text[::-1]


def exercise_10():
    print("Combines odd numbers from one list and even numbers from a second list into a new list")
    # Sample lists
    list1 = [1, 2, 3, 4, 5, 6]  # List with numbers
    list2 = [10, 15, 20, 25, 30]  # List with numbers

    # Create a new list to store the results
    new_list = []

    # Add odd numbers from the first list
    for num in list1:
        if num % 2 != 0:  # Check if the number is odd
            new_list.append(num)

    # Add even numbers from the second list
    for num in list2:
        if num % 2 == 0:  # Check if the number is even
            new_list.append(num)

    # Print the resulting list
    print(list1)
    print(list2)
    print("New list with odd numbers from list1 and even numbers from list2:", new_list)



def main():
    print("Python Beginner Exercises.")
    print('Choose an exercise to execute from the below list.')

    print('Exercise 1: Takes two integers and returns their product or sum based on a condition.\n'
        'Exercise 2: Takes two numbers and prints the sum of each number with its previous number in the range.\n'
        'Exercise 3: Returns characters at even indices from a given string.\n'
        'Exercise 4: Modifies a string based on a user-provided index.\n'
        'Exercise 5: Compares the first and last elements of a list.\n'
        'Exercise 6: Prints numbers from a list that are divisible by a user-defined number.\n'
        'Exercise 7: Counts occurrences of a substring in a given text.\n'
        'Exercise 8: Pretty prints numbers in a triangular format.\n'
        'Exercise 9: Checks if a given text is a palindrome.\n'
        'Exercise 10: Combines odd numbers from one list and even numbers from another into a new list.')
    choice = int(input("Enter your exercise number: "))
    runMain(choice)


def runMain(choice):
    if choice == 1:
        exercise_1() 
    elif choice == 2:
        exercise_2()
    elif choice == 3:
        exercise_3()
    elif choice == 4:
        exercise_4()
    elif choice == 5:
        exercise_5()
    elif choice == 6:
        exercise_6()
    elif choice == 7:
        exercise_7()
    elif choice == 8:
        exercise_8()
    elif choice == 9:
        exercise_9()
    elif choice == 10:
        exercise_10()    
    else:
        print("Enter valid input. An integer between 1 and 10.")







if __name__ == "__main__":
    main()