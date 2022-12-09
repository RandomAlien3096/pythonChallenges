"""
Task
The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i^2.
"""

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)

"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a 
leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to 
orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 
2200, 2300 and 2500 are NOT leap years. Source

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
"""
        
def is_leap(year):
    leap = False
    if ((year % 400 == 0) and (year % 100 == 0)) | ((year % 4 ==0) and (year % 100 != 0)):
        leap = True
    return leap

year = int(input())
print(is_leap(year))


"""
The included code stub will read an integer,n , from STDIN.

Without using any string methods, try to print the following:
123...n
Note that "" represents the consecutive values in between.
"""

if __name__ == '__main__':
    n = int(input())
    i=1
    for i in range(n):
        print(i+1, end="")
        
        
"""
A newly opened multinational brand has decided to base their company logo on the three most 
common characters in the company name. They are now trying out various combinations of company 
names and logos based on this condition. Given a string s, which is the company name in lowercase 
letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""
import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    frequency = Counter(list(sorted(s)))
    
    for i,j in frequency.most_common(3):
        print(i,j)
        
        
 
