# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 
grade_list = []

def input_from_user():
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_mean(grade_list):
    sum = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum =+ grade
        mean = sum / len(grade_list)
    return mean 

def calculate_sd(mean):
    for grade in grade_list:
        sd = 0 # standard deviation
        sum_of_sqrs = 0
        sum_of_sqrs += (grade - mean) ** 2
        sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd

def print_results(mean, sd):
   # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


input_from_user()
calculate_mean(grade_list)
calculate_sd(calculate_mean(grade_list))
print_results(calculate_mean(grade_list), calculate_sd(calculate_mean(grade_list)))
