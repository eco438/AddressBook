import os
import os.path
import sys


def Createdata(filename):
    with open(filename,'w') as f:
        s = os.stat(filename)
        if s.st_size == 0:
            f.write('                                                   '+ 'ADDRESS BOOK\n' )
            f.write('FirstName:'+'            '+'LastName:'+'                 '+'Address:'+'          '+'PhoneNumber:'+'           '+'Company:\n')
        else:
            return

def inputdata(filename):
    with open(filename,'a') as f:
        firstname = input('/n/nEnter the first name of the person you want to add: ')
        lastname = input('Enter the last name of the person you want to add: ')
        Address = input('Enter their address: ')
        phonenumber = input('Enter their phone number: ')
        company = input('Enter the name of their work/company name: ')
        data = (firstname+'                 '+lastname+'                  '+Address+'            '+phonenumber+'               '+company)
        f.write(data +'\n')

def main():
    filename = input('Enter the name of the AddressBook:')
    os.path.isfile(filename)
    if True:
        Createdata(filename)
        inputdata(filename)
    else:
        pass
    inputdata(filename)
main()
