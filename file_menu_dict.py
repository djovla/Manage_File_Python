import csv
import os.path
from os import system, name

#Global Variable used in the Program
file_name ='record_program.csv'
file_header = ['ID','NAME','ADDRESS','JOB']
data=[]
menu = True

# function to clear the terminal
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#This function return the last ID in the file and added 1 to it
def get_last_id()->int:
    last_index = 0
    with open(file_name,'r') as csv_file:
        record_person = csv.DictReader(csv_file,delimiter=',')
        data = list(record_person)
        if len(data)>1: 
            last_index =  int(data[-1][file_header[0]]) + 1
            data.clear() 
        else:
            last_index = 1   
    return last_index

# Verify that the file exist if not create the file and add the header in the file
def Verify_fileExist(file)->int:
    path = './'+file
    check_file = os.path.isfile(path)
    if check_file == False:
        with open(file,'w',newline='') as csv_file:
            record_person = csv.DictWriter(csv_file,fieldnames=file_header,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            record_person.writeheader()
    return(os.path.exists(path))

# print(Verify_fileExist(file_name))

#this function get the input from the user and send it to the append function to record the data in the file
def get_input():
    i =0
    record={}
    while i < len(file_header):
       if i == 0:
          record.update({file_header[i]:get_last_id()})
       else:
          user_input =input(f'Ennter the {file_header[i]} : ')
          record.update({file_header[i]:user_input})
       i += 1
    append_info(record) #call to the append function to record the data

#Append data into the file 
def append_info(list_info):
    with open(file_name,'a',newline='') as csv_file:
        record_info = csv.DictWriter(csv_file,fieldnames=file_header,delimiter=',')
        record_info.writerow(list_info)
        print('Record saved')
        system('pause')


#Write the data in the file
def write_info(data_info):
 with open(file_name,'w',newline='') as csv_file:
    record_person = csv.DictWriter(csv_file,fieldnames=file_header,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    record_person.writeheader() # write the header first in the file
    for record in data_info:
      record_person.writerow(record) #write the data in the file
    data_info.clear()

# Retrieve Data in the file unsing the name field
def find_info(str_name): 
 with open(file_name,'r') as csv_file:
    record_person = csv.DictReader(csv_file,delimiter=',')
    data = list(record_person)
    count = 0
    print('-'*50)
    for record in data:
       if record[file_header[1]] == str_name:
          count += 1
          i = 0
          display =''
          while i < len(record):
            display +=str(record[file_header[i]])+' '
            i += 1
          print(display,'[',f'{count}',']')
          
    if count > 0:
       print('-'*50,f'\nThe number of record found is: {count}\n')
    else:
       print('-'*50,f'\nNo Record Found\n',)
 system('pause')

# Display all the record 
def displayall_record(): 
 with open(file_name,'r') as csv_file:
    record_person = csv.DictReader(csv_file,delimiter=',')
    data = list(record_person)
    count = 0
    print('-'*50)
    for record in data:
        count += 1
        i = 0
        display =''
        # if count == 1:
        #     while i < len(file_header):
        #         display +=str(file_header[i])+' '
        #         i += 1
        #     print(display)
        #     continue
        while i < len(record):
           display +=str(record[file_header[i]])+' '
           i += 1
        print(display,'[',f'{count}',']')   
    if count > 0:
       print('-'*50,f'\nThe number of record found is: {count}\n')
    else:
       print('-'*50,f'\nNo Record Found\n',)
    system('pause')

#Delete the data in the file base on the id
def delete_info(id):
 with open(file_name,'r') as csv_file:
    record_person = csv.DictReader(csv_file,delimiter=',')
    data = list(record_person)
    count = 0
    for record in data:
        if record[file_header[0]] == str(id):
            data.pop(count) # remove the data in the list where the id id found
        count += 1
    write_info(data) # write the list in the file
    print('Record deleted ')
    system('pause')
    # for i in index:
    #     data.pop(i)
    # call function to write in the file


# Delete input in the file 

"""
Open a file in wirting mode that will create the file if not exist
inport data in the file. newline='' is used to remove the extra newline added afte each record.
"""

def start_menu(menu):
    while menu:
        clear()
        print('-'*50,'RECORD DATA IN FILE','-'*50)
        print('[','-'*10,'DISPLAY ALL RECORD:[A]','-'*10,']')
        print('[','-'*10,'SEARCH RECORD:[S]','-'*10,']')
        print('[','-'*10,'WRITE NEW RECORD:[W]','-'*10,']')
        print('[','-'*10,'DELETE RECORD:[D]','-'*10,']')
        print('[','-'*10,'EXIT THE PROGRAM:[X]','-'*10,']')
        choice =input('----------------------------------ENTER YOUR SELECTION : ')
        match choice.upper():
            case 'A':
                clear()
            # #     get_input()
            #     print(get_last_id())
            #     system('pause')
                displayall_record()
            case 'S':
                clear()
                find_info(input('Enter the name :'))
            case 'W':
                clear()
                get_input()
            case 'D':
                clear()
                delete_info(input('Enter the Id to delete in the Record :'))
            case 'X':
                clear()
                print('THANK YOUR AND GOOD BYE\n')
                menu = False
            case _:
                clear()
                print(f'Please Make a good Selection {choice}')

# Calling the function start_menu using the function that verify the file is present

start_menu(Verify_fileExist(file_name))

