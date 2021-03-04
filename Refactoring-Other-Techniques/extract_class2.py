# # by Kami Bigdely
# # Extract class

# class Email:
#     def __init__(self, first_name, last_name, birthdate, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birthdate = birthdate
#         self.email = email

#     def send_hiring_email(self):
#         print("email sent to: ", self.email)

#     def compose_email(self):
#         for i, value in enumerate(emails):
#             if birth_year[i] > 1985:
#                 print(first_names[i], last_names[i])
#                 print('Movies Played: ', end='')
#                 for m in movies[i]:
#                     print(m, end=', ')
#         return send_hiring_email(value)
                    

# if __name__ == "__main__":
#     first_names = ['elizabeth', 'Jim']
#     last_names = ['debicki', 'Carrey']
#     birth_year = [1990, 1962]
#     movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
#         ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
#     emails = ['deb@makeschool.com', 'jim@makeschool.com']


    



# by Kami Bigdely
# Extract class

class Email:
    def __init__(self, firstnames, lastnames, emails, birthdates):
        self.firstnames = firstnames
        self.lastnames = lastnames
        self.emails = emails
        self.birthdates = birthdates

    def send_hiring_email(self):
        print("email sent to: ", self.emails)

        for i, value in enumerate(emails):
            if birthdate[i] > 1985:
                print(firstname[i], lastname[i])
                print('Movies Played: ', end='')
                for movie in movies[i]:
                    print(movie, end=', ')
                print()
                send_hiring_email(value)

if __name__ == "__main__":
    firstname = ['elizabeth', 'Jim']
    lastname = ['debicki', 'Carrey']
    birthdate = [1990, 1962]
    movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
        ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
    emails = ['deb@makeschool.com', 'jim@makeschool.com']