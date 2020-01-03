import os
from os import path,system
import sys


def Createdata(filename):
    with open(filename,'w') as f:
        s = os.stat(filename)
        if s.st_size == 0:
            f.write('                                                   '+ 'ADDRESS BOOK\n' )
            f.write('FirstName:'+'            '+'LastName:'+'                 '+'Address:'+'          '+'PhoneNumber:'+'           '+'Company:\n')
        else:
            return
def Displaydata(filename):
    with open(filename,'r') as f:
        s = os.stat(filename)
        if s.st_size ==0:
            print("There is no data in the file")
        else:
            for line in f:
                print(line)
                
                


def inputdata(filename):
    with open(filename,'a') as f:
        firstname = input("\n\n Enter the first name of the person you want to add: ")
        lastname = input('\n\n Enter the last name of the person you want to add: ')
        Address = input('\n\n Enter their address: ')
        phonenumber = input('\n\n Enter their phone number: ')
        company = input('\n\n Enter the name of their work/company name: ')
        data = (firstname+'                 '+lastname+'                  '+Address+'            '+phonenumber+'               '+company)
        f.write(data +'\n')

def main():
    filename = input('Enter the name of the AddressBook:')
    while(1):
        if(path.exists(filename) ==False):
            print("There is no such file\n")
            ans = input("Do you want to make a new filename? (Y/N)")
            if ans == "N":
                print("Error, no such file")
                break
            else:
                Createdata(filename)
        system('cls')
        print("\t\t\t\t\t====== AddressBook ======\t\t")
        print("\n\n                  ")  
        print("\n \t\t\t\t\t 1. Enter new information")
        print("\n \t\t\t\t\t 2. Display your current entries")
        print("\n \t\t\t\t\t 3. Exit Program")
        print("\n\n");   
        choice = int(input("\t\t\t\t\t Select Your Choice :=> "))
        system('cls')
        if(choice ==1):
            inputdata(filename)
        elif(choice == 2):
            Displaydata(filename)
            input()
        elif(choice==3):
            break

    print("Thanks for using my system")
            

main()
        #if True:
        #   Createdata(filename)
        #   inputdata(filename)
       # else:
       #     pass
       # inputdata(filename)
