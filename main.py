# I changed a few things.
# You can quit the program by typing digit "0".
# To create a user - "1". 
# To read a list of users - "2". 
# To update something in the list - "3". 
# To delete - "4". 

# When user creates or updates information it also goes through basic validation.

# library to validate input
import re

# this function removes spaces and new lines for column from right and left
def strip(string):
    return string.strip()

# this function reads database from contacts.txt file
def read_database():
    file = open("C:/Users/jaana/OneDrive/Documents/tpt/margus/test1/contact.txt", encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

# this function writes contacts to file
def write_database(db):
    file = open("C:/Users/jaana/OneDrive/Documents/tpt/margus/test1/contact.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db: 
        rows.append(", ".join(row))
    file.write("\n".join(rows))
    file.close()

# this function prints all contacts from db that is in memory
def print_out_database(db):
    print("Index \t Name \t\t Phone \t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")

def print_out_commands():
    print("Commands are:")
    print("0. to quit")
    print("1. add user")
    print("2. list users")
    print("3. edit user")
    print("4. delete user")

#####################################
# My code

# VALIDATION STARTS
# Checks if name is correct
def valid_name():
  while True:
    try:
      new_fullname = ""
      new_username = input("Name? ")
      new_surname = input("Surname? ")
      
      new_username = strip(new_username)
      new_surname = strip(new_surname)
    except ValueError:
      print("Not valid. Type your real phone number.")
      continue
    if new_username.isalpha() and new_surname.isalpha():
      if len(new_username) > 1 and len(new_username) < 40 and len(new_surname) > 1 and len(new_surname) < 40:
        # Good to go
        new_fullname = new_username.capitalize() + " " + new_surname.capitalize()
        break
      else:
        print("Write a valid name")
        continue
    else:
      print("Only letters")
      continue

  return new_fullname

# Checks if phone number is valid
# A valid number is 7 or 8 digits and as default is estonian
def valid_phone():
  while True:
    try:
      new_userphone = input("Phone? ")
      validate_phone = r"^[0-9]{7,8}$"
      valid_phone = re.search(validate_phone, new_userphone)
    except ValueError:
      print("Not valid. Type your real phone number.")
      continue
    if valid_phone:
      # Good to go
      new_userphone = "+372 " + str(new_userphone)
      break
    else:
      print("Please enter correct phone number. (7 or 8 digits)")
      continue
  return new_userphone

# Checks if age is valid
def valid_age():
  while True:
    try:
      new_userage = int(input("Age? "))
    except ValueError:
      print("Not valid. Type your real age.")
      continue
    if new_userage <= 0 or new_userage > 130:
      print("Not valid. Type your real age.")
      continue
    else:
      # Good to go
      new_userage = str(new_userage)
      break
  return new_userage

# Checks if email is correct
def valid_email():
  while True:
    try:
      new_usermail = input("Mail? ")
      validate_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      valid_email = re.search(validate_email, new_usermail)
    except ValueError:
      print("Not valid. Type your real phone number.")
      continue
    if valid_email:
      # Good to go
      break
    else:
      print("Write correct email please")
      continue
  return new_usermail

# VALIDATION ENDS

# Pretty string to print for user in the terminal
def listToString(s): 
    # initialize an empty string
    str1 = ", " 
    
    # return string  
    return (str1.join(s))

# ADD user
def add_user():
  new_userlist = []
  print("Adding a user")

  # Checks if name is correct
  name = valid_name()

  # Checks if phone number is valid
  # A valid number is 7 or 8 digits and as default is estonian
  phone = valid_phone()

  # Checks if age is valid
  age = valid_age()

  # Checks if mail is correct
  email = valid_email()

  new_userlist.insert(0, name)
  new_userlist.insert(1, phone)
  new_userlist.insert(2, age)
  new_userlist.insert(3, email)

  print("User succesfully added! :D")
  print(*new_userlist)

  new_userstring = listToString(new_userlist)
  # Add contact to a file
  with open("contact.txt", "a+", encoding="utf-8") as file:
    file.seek(0)
    data = file.read(100)
    if len(data) > 0 :
        file.write("\n")
    file.write(new_userstring)

# READ a list of users
def list_users():
  print("List of users")
  f = open("contact.txt", "r", encoding="utf-8")
  print(f.read())

# UPDATE an information of a chosen user
def edit_user():
  db = read_database()
  print("Which user you would like to edit?")
  print("Choose an index of the user. (You can find it the full list.)")

  while True:
    try:
      user_index = int(input())
      row = db[user_index]
    except ValueError:
      print("Not valid. Type correct index.")
      continue
    except IndexError:
      print("Not valid. List index out of range.")
      continue
    if user_index:
      # Good to go
      break
    else:
      print("Write correct index.")
      continue

  print(listToString(row))

  user_info_index = 0

  # Delete a whole string in a file
  del_file = open("contact.txt", "r", encoding="utf-8")
  lines = del_file.readlines()
  del_file.close()

  del lines[user_index]

  delete_file = open("contact.txt", "w+", encoding="utf-8")

  for line in lines:
    delete_file.write(line)

  delete_file.close()

  print("Choose which element you want to change")
  print("(name, phone, age, email)")
  
  while True:
    try:
      user_info = input()
    except ValueError:
      print("Not valid. Choose correct element")
      continue
    # Edit NAME
    if user_info == "0" or user_info == "quit":
      print("Byeee")
      break
    elif user_info == "name":
      user_info_index = 0
      print("You chose to change a name. Please, type a new one.")
      # Delete the name
      row.pop(user_info_index)

      # Create a new one
      new_name = valid_name()

      # Replace an old name with a new one
      # (put a new one on the position of the old one) 
      row.insert(user_info_index, new_name)

      break
    # Edit PHONE
    elif user_info == "phone":
      user_info_index = 1
      print("You chose to change a phone number")
      # Delete the name
      row.pop(user_info_index)

      # Create a new one
      new_phone = valid_phone()

      # Replace an old name with a new one
      # (put a new one on the position of the old one) 
      row.insert(user_info_index, new_phone)

      break
    elif user_info == "age":
      user_info_index = 2
      print("You chose to change an age")
      # Delete the name
      row.pop(user_info_index)

      # Create a new one
      new_age = valid_age()

      # Replace an old name with a new one
      # (put a new one on the position of the old one) 
      row.insert(user_info_index, new_age)

      break
    elif user_info == "email":
      user_info_index = 3
      print("You chose to change an email")
      # Delete the name
      row.pop(user_info_index)

      # Create a new one
      new_email = valid_email()

      # Replace an old name with a new one
      # (put a new one on the position of the old one) 
      row.insert(user_info_index, new_email)

      break
    else:
      print("Choose correct element")
      continue

  # Add a changed element to a file
  new_userstring = listToString(row)
  # Add contact to a file
  with open("contact.txt", "a+", encoding="utf-8") as file:
    file.seek(0)
    data = file.read(100)
    if len(data) > 0 :
        file.write("\n")
    file.write(new_userstring)

# DELETE a user
def delete_user():
  db = read_database()
  print("Choose an index of the user you want to delete.")
  user_index = int(input())

  row = db[user_index]
  print(listToString(row))

  del_file = open("contact.txt", "r", encoding="utf-8")
  lines = del_file.readlines()
  del_file.close()

  del lines[user_index]

  delete_file = open("contact.txt", "w+", encoding="utf-8")

  for line in lines:
    delete_file.write(line)

  delete_file.close()

# User chooses an operation
def choose_command():
  db = read_database()
  while True:
    decision = input("What is your command?: ")
    print("______________________")
    # Quit

    if decision == "0" or decision == "quit":
      print("Byeee :c")
      break
    # Add a new user
    elif decision == "1" or decision == "add user":
      add_user()
      break
    # Print a list of users from contact.txt
    elif decision == "2" or decision == "list users":
      # Maybe i can steal some of your code?
      print_out_database(db)
      # if not then
      # list_users()

      sum_age = 0
      for user in db:
        age = user[2]
        sum_age+=int(age)

      avg_age= sum_age / len(db)
      print("Medium age is:")
      print(round(avg_age))

      continue
    # Update a chosen user
    elif decision == "3" or decision == "edit user":
      edit_user()
      break
    elif decision == "4" or decision == "delete user":
      delete_user()
      break
    else:
      print("Please type a number listed above")
 
def main():
  db = read_database()
  print_out_database(db)
  print_out_commands()
  choose_command()


main()