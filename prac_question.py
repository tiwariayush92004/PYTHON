# *******find all unique roll numbers of the list[101,105,102,101,108,105,110]
# roll_nums = {101,105,102,101,108,105,110}
# print("unique roll numbers are : ", roll_nums)


#****** ques 2 : find the employee from the list by its employee id 
# emp_list = [
#     (101, "Alice", 50000),
#     (102, "Bob", 70000),
#     (103, "Charlie", 43000)
# ]

# search_emp = int(input("Enter the Employee Id you want to search : "))
# for search in emp_list:
#     if search_emp == search:
#         print("Employee found : " )




# ******* check if number is odd or even 

# def odd_even(num):
#     if(num%2 == 0):
#         print("even")
#     else:
#         print("odd")
# num = int(input("Enter a number : "))
# odd_even(num)




# count the number of vowels in the string 
# def count_vowels(text):
#     count = 0  # Initialize count locally inside the function
    
#     for char in text:
#         if char.lower() in 'aeiou':  # Checks if character is a vowel (case-insensitive)
#             count += 1
            
#     if count > 0:
#         print(f"Total vowels found: {count}")
#     else:
#         print("No vowels found")

# inpu = input("Enter the String: ")
# count_vowels(inpu)






# function to return the average marks if a list of marks is passed as parameter
def avg_mark(marks):
    if len(marks) == 0:
        return 0
    else:
        average = sum(marks)/len(marks)
        return average

student1_marks = [90,88,59,87,73,91,77]
print(avg_mark(student1_marks))