import sys


if len(sys.argv) <= 1:

    print("Please, inform your login: ")
    login = input()
    print("Please, inform your password: ")
    password = input()

else:

    login = sys.argv[1]
    password = sys.argv[2]

    

driver_path = 'C:\selenium_drivers\chromedriver'
