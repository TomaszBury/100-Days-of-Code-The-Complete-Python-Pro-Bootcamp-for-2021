year = int(input("Which year do you want to check?"))
# list_of_leap_years = [1804,1808,1812,1816,1820,1824,1824,1832,1836,1840,1844,1848,1852,1856,1860,1864,1868,1872,1876,1880,1884,1888,1892,1896,1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096]
# print(f"How long is the list of leap years: {len(list_of_leap_years)}")
# how_many_leap_years_i_found = 0

# for year in list_of_leap_years:
print(f"Type of input: {type(year)}")
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
            # how_many_leap_years_i_found += 1
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
        # how_many_leap_years_i_found += 1
else:
    print("Not leap year.")

# print(f"This many leap years i found: {how_many_leap_years_i_found}")
    