from timeit import timeit
import orjson
import simplejson
import json
import os
import sys
def show_menu():
    print('#######################')
    print('Choise the kind of function that you want to execute:')
    print('1. Testing time of parsing json libraries')
    print('2. Testing time of processing numbers algorithms')
    print('#######################')

#this json is used as a base of data. This challenge will run using this json
with open("campaign.json") as file:
    response = json.load(file)

#This function will process the current json using a certain lib that pass as an argument
def serialize(lib):
    lib.dumps(response)

#This function will create a file called list_of_numbers.txt and print there the increase of cont variable.
def writing_down(how_many_lines):
    with open('list_of_numbers.txt','w') as file:
        print(how_many_lines)
        for cont in range(int(how_many_lines)):
            file.write(str(cont)+"\n")
            print(cont)

#This function will convert the seconds in hours, minutes, seconds and milliseconds
def sec_convertion(sec, some_text):
    hours = sec // 3600
    left_seconds = sec % 3600
    minutes = left_seconds // 60
    tmp_seconds = left_seconds % 60
    print(tmp_seconds)
    seconds, milliseconds = divmod(tmp_seconds,1)
    milliseconds = round(milliseconds * 1000)
    text = '{}: It got {} hours ' + ' {} minutes' + ' {} seconds'+ ' {} milliseconds'
    
    print(text.format(some_text,hours,minutes,seconds,milliseconds))

#This function will measure the serialize function a certain number of times in my example I'm using 100 times. This will return the total of seconds of the execution
def testing_json_libraries(library_name):
    print(library_name)
    json_time = timeit(lambda: serialize(eval(library_name)), number = 100)
    sec_convertion(json_time, library_name)

#This function will measure the writing down functionality a certain number of times, 100 in my challenge. . This will return the total of seconds of the execution
def testing_writing_plain_file(how_many_lines):
    try:
        execution_time = timeit(lambda: writing_down(how_many_lines), number = 100)
        sec_convertion(execution_time, 'writing down')
        if how_many_lines < 0:
            raise ValueError('Number of lines should be a positive number')
    except ValueError as ve:
        print(ve)

#This is the function that will execute others functions with its arguments also.
def general_function_executor(function_name, arg):
    try:
        eval(function_name)(arg)
    except:
        print('An Error occurred' , sys.exc_info()[0])

os.system("cls")
#This portion will create the iteractive console menu. With the options of the challenge
while True:
    show_menu()
    opt = input('Enter here your choice number --> ')
    if opt == "1":
        print("Write the name of the function and the library to mesuere the execution time of parsing a big json: ")
        print('function name: testing_json_libraries')
        function = input()
        print('argument value: json, simplejson')
        library = input()
        general_function_executor(function,library)
    elif opt == "2":
        print("Write the name of the function and the number of lines to write down(A positive integer number): ")
        print('function name: testing_writing_plain_file')
        function = input()
        print('argument value: 1000? 10000?')
        lines_number = input()
        general_function_executor(function,lines_number)
    elif opt == "2":
        print('opt 3')
    else:
        print('You wrote an invalid option. Try again')

