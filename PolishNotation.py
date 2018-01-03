#------------- import Library ---------------------------
from builtins import input
#-------------Define Methods ----------------------------
def isOperator(c):
    return ((c == '+') | (c == '-') | (c == '/') | (c == '*'))

def whichOperator(c):
    if c =='+':
        return 0
    elif c=='-':
        return 1
    elif c=='*':
        return 2
    elif c=='/':
        return 3
    else:
        return -1

def doIt (c,val1,val2):
    oprt = whichOperator(c)
    if (oprt == 0) : # addition
        return val1 + val2
    elif (oprt == 1): #extraction
        return val1 - val2
    elif (oprt == 2): #multiplication
        return val1 * val2
    elif (oprt == 3): #divide
        return val1 / val2
    else :
        print("value not operator..")
        return -1
#-------------------------MAIN CODE---------------------------------------------------
Lifo = []                                                                       #Operator Stack
Fifo = []                                                                       #Operator Queue
generalList = []                                                                #seperated polish notasyon
operandList = []                                                                #operands will be processed
lastOperand =''                                                                 #last operator
result=-1

notasyon = input("Enter Polish Notation :")                                     # get notasyon
generalList = notasyon.split(" ")                                               #split notasyon

isFine = False                                                                  #is it ok ?
lastOperand=""

for i in generalList :
    if(isOperator(i)):                                                          #is operator
        isFine=True
        lastOperand=i
        Lifo.append(i)
    elif(isOperator(i)==False):
        operandList.append(int(i))
        if(len(operandList)==2 ):
            if(isFine):
                result = doIt(Lifo[len(Lifo)-1],operandList[0],operandList[1])
                del operandList[0:]
                del Lifo[len(Lifo)-1]
                Fifo.append(result)
                isFine=False
            else:
                Fifo.append(operandList[0])
                Fifo.append(operandList[1])
        else:
            if(i == generalList[-1]):
                Fifo.append(int(i))
                                                           #You can add print("Fifo :",Fifo),print("Lifo :",Lifo)
lenght = len(Lifo)
for i in range(lenght):
    result = doIt(Lifo[len(Lifo)-1],Fifo[0],Fifo[1])
    del Fifo[0:2]
    Fifo.insert(0,result)
    del Lifo[len(Lifo)-1]

print("Result :",Fifo[0])