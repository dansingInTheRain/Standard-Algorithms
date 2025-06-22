#standard algorithms - max and min
#Daniel Seix
#01/03/2022


def getlist():
    import random
    #list of values
    testscore=0, 9, 100, 24
    print(testscore)
    return testscore

def findMax(testscore):
    #find the highest number in the list
    #set maximum to testscore 0 (first one in the list)
    maximum=testscore[0]
    #loop through the rest of the list
    for counter in range(1,len(testscore)):
        if testscore[counter]>maximum: #compare each item with maximum
            #if it is bigger, then set max to this value
            maximum=testscore[counter]
    return maximum
    
def findMin(testscore):
    #find the lowest number in the list
    #set minimum to testscore 0 (first one in the list)
    minimum=testscore[0]
    #loop through the rest of the list
    for counter in range(1,len(testscore)):
        if testscore[counter]<minimum: #compare each item with maximum
            #if it is bigger, then set max to this value
            minimum=testscore[counter]
    return minimum

def display(maximum,minimum):
    #display max and min
    print("The highest test score is",maximum,)
    print("The lowest test score is",minimum,)
    
#main program
testscore=getlist()
maximum=findMax(testscore)
minimum=findMin(testscore)
display(maximum,minimum)
