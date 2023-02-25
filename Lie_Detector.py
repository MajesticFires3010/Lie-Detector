import os                           # For Clearing the Screen while Reactivating the Lie Detector evertime
from pyfiglet import figlet_format  # For Stylish Heading
from termcolor import colored       # For Stylish Heading
import time                         # For End of Terminal Extra Time
import stdiomask                    # To Turn Off echoing while giving input

def Lie_Detector() :
    print("Welcome to the World's Most Fail Proof Lie Detector ;-)")
    # Enter Your Question (by the User)
    a = input("What's Your Question ? ")
    # Enter the Answer ('1' : "True" and '2' : "False")
    b = stdiomask.getpass(prompt="Hmmm... That's a Good Question... ", mask='')
    print()
    print("And the Answer is : ", end='')
    b = eval(b)
    if b == 1 :
        print("True")
    elif b == 0 :
        print("False")
    print("Got Ya Bro ;-)")
    print()
    time.sleep(5)

x = 'Y'
while x == 'Y' :
    a = figlet_format("Lie  Detector", font="starwars", width=1000)
    print(colored(a, "green"))
    print()
    x = input("Do You Want to Activate the Lie Detector (Y/N) : ")
    x = x.upper()   # To Avoid Upper/Lowercase Discrepancy
    Lie_Detector()
    x = input("Another Round (Y/N) ? ")
    x = x.upper()   # To Avoid Upper/Lowercase Discrepancy
    os.system("cls")
else:
    print("Have a Great Day ;-)")


time.sleep(10)