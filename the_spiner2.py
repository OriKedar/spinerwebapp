##Ori Kedar##

import random 
import argparse
import sys
import linecache
import os

##count the numbers of the lines in the text file for the random and the record count
# def file_len(file_name): 
#     with open(file_name + ".txt", "r") as f: 
#         for i, l in enumerate(f):
#             pass

#     f.close


#     return (i + 1) 

def file_len(file_name): 
    with open(file_name + ".txt", "r") as f:
        lines = f.readlines()
    return len(lines)

#Get the location of the file
# A = os.path.dirname(os.path.realpath("My_records.txt"))
#print(A)

#read all the file
def read_file(file_name):
    with open(file_name + ".txt") as f:
        read_data = f.read()
    return(read_data)

#the best way to addinig text, don't have an sucsses\unsucsses to the addinig
def add_text(file_name):
    new_data = input("Add your new record here: ")
    with open(file_name + ".txt", "a+") as f:
        f.write("\n" + new_data)

#the basic function. 
#def Spiner(user_name):
#    print('############################################')
#    print('spin the record: ' + random.choice(user_name))
#    print('############################################')
#the 2.0 spiner
#def the_Spiner(file_name):
#    random_line = (random.randint(1,file_len("text")))
#    record_name = linecache.getline(file_name + ".txt", random_line)
#    print('############################################\n')
#    print('spin the record: ' + record_name)
#    print('############################################')
#the 2.1 spiner
def Spiner(file_name):
    side = ['A side', 'B side']
    random_line = (random.randint(1,file_len(file_name)))
    record_name = linecache.getline(file_name + ".txt", random_line)
    print('############################################')
    print('spin the record: ' + record_name.strip()) 
    print(random.choice(side))
    print('############################################')

def welcome_screen():
    print('Hallo and welcome to the new record choose cesnter.')
    print('Please choose what do whant to do:')
    # print("1.Get a random record\n2.See the record list.\n3.Add a new record\n4.Get a record count.")
    print("1.Get a random record","2.See the record list.","3.Add a new record","4.Get a record count.", sep="\n")
    return input("Enter the number: ")
#print(user_choice)

if  __name__ == "__main__":
    user_choice = welcome_screen()

    if user_choice == "1":
        Spiner("My_records")
    elif user_choice == "2":
        print(read_file("My_records"))
    elif user_choice == "3":
        add_text("My_records")
        print("Record added sucssefuly")
    elif user_choice == "4":
        print(file_len("My_records"))
    else:
        print("Error")
