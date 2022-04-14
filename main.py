#By XKMR

import pylab as plt

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
    print("   -- to press Ctrl+C when you are stuck in a loop of numbers.")
    print("-  tested on: Windows 11 - 10  I will soon test in on linux builds too :)")
    print("")
    print("   Coded by XKMR")
    quit()


import sys
usegraph = False

try:
    inf = sys.argv[1]
except:
    help()

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
    num = int(inf)
    print(str(num)+".0")

num_list = [num]
count = 1
inf = 10
f = open("function.txt", "a")
f.write("num: "+str(num)+"\n")
if num == 0:
    print("number must not be 0 - use: 'python main.py help'")
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
        olst = list(range(1,count+1))
   
        Year = olst
        Unemployment_Rate = num_list
  
        plt.plot(Year, Unemployment_Rate, color='red', marker='o')
        plt.title('Coded by XKMR | Output Numbers:', fontsize=14)
        plt.xlabel('Number Count', fontsize=14)
        plt.ylabel('Numbers', fontsize=14)
        plt.grid(True)
        plt.show()


elif num < 0:
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
    f.write("\n----- DONE count: "+str(count)+" -----\n\n\n")
    f.close()

    print("Coded by XKMR - DONE - count: "+str(count))
else:
    print("unknown error: please make an issue on github.com/XKMR/ and tell me the input that you used.")