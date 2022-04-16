#By XKMR
import sys
import pylab as plt
import os
import time
import keyboard
guimode = False
usegraph = False
#function list:

def help():
    print("   error with command arguments - correct argument examples:")
    print("")
    print("-  to use the program on any number (I used 35 here): main.py 35")
    print("   the plrogram also saves a log to the file: 'function.txt'")
    print("   to clear the file: main.py clr")
    print("-  I also made it to show a graph of the output. to use it, add 'graph' (without quests)")
    print("   after the number to enable it.")
    print("-  hint: add the python execution at first - and no hyphen ( - ) is needed")
    print("-  you can also use negetive numbers to see what they do! also don't forgot--")
    print("   -- to press q when you are stuck in a loop of numbers. (only for - numbers)")
    print("-  you can use easy mode by just using the argument 'ez' on the command or not using any arguments")
    print("-  tested on: Windows 11 - 10  I will soon test in on linux builds too :)")
    print("")
    print("   Coded by XKMR")
    if(guimode):
        input()
    quit()

#inputs
try:
    inf = sys.argv[1]
except:
    print("command used wrongly - input 1 to run for help | input 2 to run in easy mode")
    getez = input(">>> ")
    if(getez == "1"):
        help()
    elif(getez == "2"):
        guimode = True
    else:
        print("Wrong input")
        input()
        quit()
else:
    if(sys.argv[1] == "ez"):
        guimode = True

if not guimode:
    try:
        grf = sys.argv[2]
    except:
        inf = inf
    else:
        if(sys.argv[2] == "graph"):
            usegraph = True

    inf = sys.argv[1]
    if(inf == "help"):
        help()

    if inf == "clr":
        fs = open("function.txt", "w")
        fs.write("")
        fs.close()
        print("done")
        quit()
    else:
        try:
            int(inf)
        except:
            print("input is not a valid number - use: 'python main.py help'")
            quit()

elif(guimode):
    print("input number or if you want to clear the file input 'clr'")
    inf = input(">>> ")
    if inf == "clr":
        fs = open("function.txt", "w")
        fs.write("")
        fs.close()
        print("done")
        time.sleep(2)
        quit()
    else:
        try:
            int(inf)
        except:
            print("input is not a valid number - use: 'python main.py help'")
            input()
            quit()
    print("number verified.")
    if(num > 0):
        print("do you want a graph of the output? (y/n)")
        usin = input(">>> ")
        if(usin == "y"):
            usegraph = True
        elif(usin == "n"):
            usegraph = False
        else:
            print("invalid input")
            time.sleep(2)
            quit()

#actual functioning
num = int(inf)
num = num * 2
num = num / 2
print(str(num))
num_list = [num]
count = 1
inf = 10
f = open("function.txt", "a")
f.write("num: "+str(num)+"\n")
if num == 0:
    print("number must not be 0 - use: 'python main.py help'")
    if(guimode):
        input()
    quit()
if num > 0:
    while num > 1:
        if (num % 2) == 0:
            num = num/2
            f.write("num: "+str(num)+"\n")
        else:
            num = (num*3)+1
            f.write("num: "+str(num)+"\n")
        print(num)
        num_list.append(num)
        count = count + 1
    f.write("\n----- DONE count: "+str(count)+" -----\n\n\n")
    f.close() 
    print("Coded by XKMR - DONE - count: "+str(count))
    if(usegraph):
        olst = list(range(0,count))
        Year = olst
        Unemployment_Rate = num_list
        plt.plot(Year, Unemployment_Rate, color='red', marker='o')
        plt.title('Coded by XKMR | Output Numbers:', fontsize=14)
        plt.xlabel('Number Count', fontsize=14)
        plt.ylabel('Numbers', fontsize=14)
        plt.grid(True)
        plt.show()
        if(guimode):
            input()
elif num < 0:
    print("IMPORTANT: press 'q' to exit if you are in a loop")
    time.sleep(3)
    while num < 0:
        if (num % 2) == 0:
            num = num/2
            f.write("num: "+str(num)+"\n")
        else:
            num = (num*3)+1
            f.write("num: "+str(num)+"\n")
        print(num)
        num_list.append(num)
        count = count + 1
        try:
            if keyboard.is_pressed('q'):
                break
        except:
            break            
    f.write("\n----- DONE count: "+str(count)+" -----\n\n\n")
    f.close()
    print("Coded by XKMR - DONE - count: "+str(count))
    if(guimode):
        input()
else:
    print("unknown error: please make an issue on github.com/XKMR/ and tell me the input that you used.")
    if(guimode):
        input()
