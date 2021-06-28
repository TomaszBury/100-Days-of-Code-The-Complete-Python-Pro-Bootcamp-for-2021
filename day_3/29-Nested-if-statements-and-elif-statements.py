#29. Nested if statements and elif statements

'''
https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1J7_rw1flGeF0hmc_zrMzPX7t6xkbcsiX%26export%3Ddownload
'''

'''
https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload
'''

height = int(input("What is you'r height:\n"))

if height >= 120:
    print("You'r going for this ride!")
    age = int(input("What is your age?:\n"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Grow up!!!!!!\n")