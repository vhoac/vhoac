#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_vhoac.py
Author: "Victor Hoac"
The python code in this file (a1_vhoac.py) is original work written by
"Victor Hoac". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    '''
    determines whether year given is a leap year
    '''
    status = ''
    if year % 4 == 0:
        status = True
    else:
        status = False
    return status

def sanitize(obj1,obj2):
    '''
    takes user input of YYYYMMDD, YYYY/MM/DD, YYYY-MM-DD, or YYYY.MM.DD, and converts it into YYYYMMDD format
    
    allowed characters in user input include:
    numbers from 0-9
    special characters: '/', '-' and '.'
    ''' 
    results = ''
    for char in user_raw_data:
        if char in '0123456789':
            results += char
    return results

def size_check(obj, intobj):
    '''
    after data is sanitized, check whether the resulting object has a length of 8 characters
    '''
    status = ''
    if len(dob) != 8:
         status = False
    else:
         status = True
    return status

def range_check(obj1, obj2):
    '''
    check range values for year, month and day

    acceptable year values: 1900 - 9999
    acceptable month values: 1 - 12
    acceptable day values:
        - If month is 'Jan', 'Mar', 'May', 'Jul', 'Oct' or 'Dec': 31
        - If month is 'Feb' and year is not leap year: 28
        - If month is 'Feb' and year is leap year: 29
        - If month is 'Apr', 'Jun', 'Aug', 'Sep' or 'Nov': 30
    '''
    status = ''
    if year >= 1900 and year <= 9999:
        try:
            if month in days_in_month.keys():
                if day in days_in_month.values():    
                    status = True
        except KeyError:
            status = False
    else:
        status = False
    return status

def usage():    
    '''
    if incorrect number of arugments are entered, activate this function
    display a message indicating how to use the program
    '''
    status = "Usage: a1_vhoac.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   # step 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)  
