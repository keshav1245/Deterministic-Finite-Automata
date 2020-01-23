## PRINT FUNCTION AND STRING PROCESSING FUNCTIONS

key1 = "a"
key2 = "b"
input_sym = [key1,key2]

def printTable(table,final,start):
    print("|{0:^8} | {1:^8} | {2:^8}  | \n".format("states","a","b"))
    print("-{0:-^8}---{1:-^8}---{2:-^8}----\n".format("","",""))
        
    for i in table.keys():
        if i in final and i in start:
            tab = "->*"+i
            print(f"|{tab:^8} | ",end ="")
        elif i in final:
            tab = "*"+i
            print(f"|{tab:^8} | ",end ="")
        elif i in start:
            tab = "->"+i
            print(f"|{tab:^8} | ",end ="")
        else:
            print(f"|{i:^8} | ",end ="")
            
        for j in input_sym:
            print(f"{table[i][j]:^8} | ",end =" ")
        print("\n")


def processString(start,final,tableDict):

    while True:
        choice = input("Do you want to Do some String Processing ?")
        if choice.upper()[0] == "Y":
            strProcess = input("Enter your string on alphabets a and b : ")
            print("\n\n")
            currstate = start
            if currstate in final:
                print("->*"+start,end="")
            else:
                print("->"+start,end="")
            for char in strProcess:
                print("--"+char+"--",end="")
                currstate = tableDict[currstate][char]
                if(currstate in final):
                    print("*"+currstate,end="")
                else:
                    print(currstate,end="")
            else:
                if currstate in final:
                    print("\nString Accepted !\n")
                else:
                    print("\nString Not Accepted !\n")
        elif choice.upper()[0] == "N":
            print("Have a Good Day !")
            break
        else:
            print("Enter Correct Input (Yes or No)")

#PREFIX FUNCTION

def Prefix():
    print("Fixing alphabets to a & b and dead state as qD")
    print("For DFAs starting with : ")
    pattern = input("Enter your stating with pattern : ")

    tableDict = {}
    index = 0
    start = "q"+str(index)
    final = ""

    
    for char in pattern:
        if index == 0:
            if char == key1:
                transition = {key1:"q"+str(index+1),key2:"qD"}
                tableDict['q'+str(index)] = transition
            elif char == key2:
                transition = {key1:"qD",key2:"q"+str(index+1)}
                tableDict['q'+str(index)] = transition
        
        else:
        
            if char == key1:
                transition = {key1:"q"+str(index+1),key2:"qD"}
                tableDict["q"+str(index)] = transition
            elif char == key2:
                transition = {key1:"qD",key2:"q"+str(index+1)}
                tableDict["q"+str(index)] = transition
        index += 1
    else:
        if index == len(pattern):
            transition = {key1:"q"+str(index),key2:"q"+str(index)}
            tableDict['q'+str(index)] = transition
            tableDict["qD"] = {key1:"qD",key2:"qD"}
            final = "q"+str(index)

    printTable(tableDict,final,start)
    processString(start,final,tableDict)
    
#ATLEAST FUNCTION

def Atleast_A():
    print("Fixing alphabets to a & b and dead state as qD")
    print("For DFAs at least with (a) : ")
    try:
        noOf_a = int(input("Enter at least no of a : "))
        if noOf_a < 0:
            print("\n\nCan't be negative !\n\n")
            return
    except:
        print("\n\nInvalid Input Detected !\n\n")
        return
        
    tableDict = {}
    counter = 0
    start = "q"+str(counter)
    final = ""
    

    while counter < noOf_a:
        transition = {key1:"q"+str(counter+1),key2:"q"+str(counter)}
        tableDict['q'+str(counter)] = transition
        counter += 1
    else:
        transition = {key1:"q"+str(counter),key2:"q"+str(counter)}
        tableDict["q"+str(counter)] = transition
        final = "q"+str(counter)
    

    printTable(tableDict,final,start)
    processString(start,final,tableDict)

#ATMOST FUNCTION

def Atmost_A():
    print("Fixing alphabets to a & b and dead state as qD")
    print("For DFAs at most (a) : ")
    try:
        noOf_a = int(input("Enter at most no of a : "))
        if noOf_a < 0:
            print("\n\nCan't be negative !\n\n")
            return
    except:
        print("\n\nInvalid Input Detected !\n\n")
        return
    
    tableDict = {}
    counter = 0
    start = "q"+str(counter)
    final = set()

    while counter < noOf_a:
        transition = {key1:"q"+str(counter+1),key2:"q"+str(counter)}
        tableDict['q'+str(counter)] = transition
        final.add("q"+str(counter))
        counter += 1
    else:
        transition = {key1:"qD",key2:"q"+str(counter)}
        tableDict["q"+str(counter)] = transition
        tableDict["qD"] = {key1:"qD",key2:"qD"}
        final.add("q"+str(counter))
    

        printTable(tableDict,final,start)
        processString(start,final,tableDict)
        
#START FUNCTION
def start():
    print(f"{'WELCOME TO DFA GENERATOR & STRING CHECKER': ^80}")
    while True:
        print("Choose Any 1 from below : ")
        print("1. Prefix DFA")
        print("2. Atmost No. of a ")
        print("3. Atleast No. of a ")
        print("4. Exit ")
        
        try:
            choice = int(input("Enter your choice : "))
        except:
            print("\n\nInvalid Input !\n\n")
            continue
        
        if choice == 1:
            Prefix()
        elif choice == 2:
            Atmost_A()
        elif choice == 3:
            Atleast_A()
        elif choice == 4:
            break
        else:
            print("Input not recognized !\n\n\n\n")
            continue
        
        print("\n\nDo you want to Try Again : ")
        ans = input()
        if ans[0].upper() == "Y":
            continue
        elif ans[0].upper() == "N":
            break
        else:
            print("In valid Input ! Aborting !")
            break
            
if __name__ == "__main__":
	start()
