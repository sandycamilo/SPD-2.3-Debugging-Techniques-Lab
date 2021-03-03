# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")

if __name__ == "__main__":
    user_name_input = input("Please enter your username: ")
    save_into_db(user_name_input)
    user_birthdate_input = int(input("Please enter your birth year: "))
    age = 2020 - user_birthdate_input
    print("You are", age, "years old.")
