import csv
import os.path
from os import system, name

#Global Variable used in the Program
file_name ='record_program.csv'
file_header = ['ID','NAME','ADDRESS','JOB']
data=[]
menu = True

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#This function return the last ID
def get_last_id()->int:
    last_index = 0
    with open(file_name,'r') as csv_file:
        record_person = csv.reader(csv_file,delimiter=',')
        data = list(record_person)
        if len(data)>1:
            last_index =  int(data[-1][0]) + 1
            data.clear() 
        else:
            last_index = 1   
    return last_index

# Verify that the file exist if not create the file
def Verify_fileExist(file)->int:
    path = './'+file
    check_file = os.path.isfile(path)
    if check_file == False:
        with open(file,'w',newline='') as csv_file:
            record_person = csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            record_person.writerow(file_header)
    return(os.path.exists(path))

# print(Verify_fileExist(file_name))

#Record data in the file using append mode
def get_input():
    data.clear()
    data.append(get_last_id())
    data.append(input('Enter Name : '))
    data.append(input('Enter Address : '))
    data.append(input('Enter Job : '))
    append_info(data)


def append_info(list_info):
    with open(file_name,'a',newline='') as csv_file:
    #    data.append([1,'Virgo','Brooklyn','Software Dev'])
    #    data.append([2,'Victoria','Brooklyn NY','Entrepreneur'])
    #    print(data)
        record_info = csv.writer(csv_file,delimiter=',')
        record_info.writerow(list_info)
        data.clear()
        print('Record saved')
        system('pause')
#record_info([3,'Jean','Bizoton','Police Officer'])

#Write the data in the file
def write_info(data_info):
 with open(file_name,'w',newline='') as csv_file:
    record_person = csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    record_person.writerows(data_info)

# Retrieve Data in the file
def find_info(str_name): 
 with open(file_name,'r') as csv_file:
    record_person = csv.reader(csv_file,delimiter=',')
    data = list(record_person)
    count = 0
    print('-'*50)
    for record in data:
       if record[1] == str_name:
          count += 1
          i = 0
          display =''
          while i < len(record):
            display +=str(record[i])+' '
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
    record_person = csv.reader(csv_file,delimiter=',')
    data = list(record_person)
    count = 0
    print('-'*50)
    for record in data:
        count += 1
        i = 0
        display =''
        if count == 1:
            while i < len(file_header):
                display +=str(file_header[i])+' '
                i += 1
            print(display)
            continue
        while i < len(record):
           display +=str(record[i])+' '
           i += 1
        print(display,'[',f'{count-1}',']')   
    if count > 0:
       print('-'*50,f'\nThe number of record found is: {count-1}\n')
    else:
       print('-'*50,f'\nNo Record Found\n',)
    system('pause')

#Find the indexes for all the record present for input search
def delete_info(id):
 with open(file_name,'r') as csv_file:
    record_person = csv.reader(csv_file,delimiter=',')
    data = list(record_person)
    index = []
    count = 0
    for record in data:
        if record[0] == str(id):
            data.pop(count) 
            index.append(count)
        count += 1
    print(data)
    write_info(data)
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
                displayall_record()
            case 'S':
                clear()
                print(f'The case is {choice}')
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

