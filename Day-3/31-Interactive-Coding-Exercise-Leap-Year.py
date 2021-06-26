#31. [Interactive Coding Exercise] Leap Year

#https://replit.com/@appbrewery/day-3-3-exercise

'''
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

    on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops. 
'''

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

''''''
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Not leap year.")
    else:
        print("Leap year!")
else:
    print("Not leap year.")

''''''

list_of_leap_years = [1804,1808,1812,1816,1820,1824,1824,1832,1836,1840,1844,1848,1852,1856,1860,1864,1868,1872,1876,1880,1884,1888,1892,1896,1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096]

'''

for year in list_of_leap_years:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year!")
            else:
                print("Not leap year.")
        else:
            print("Leap year!")
    else:
        print("Not leap year.")

#print(list_of_leap_years)

'''