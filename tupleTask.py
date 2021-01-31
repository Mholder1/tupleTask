import operator
import sys
import time

def createListFromFile(tupleList, fileName):
    dataLists=[]
    with open(fileName, 'r') as t:
        for item in t:
            item.strip()
            dataLists.append(item.strip().split(","))
            for dList in dataLists:
                dList[1] = int(dList[1])
                dList[2] = int(dList[2])
                dList[3] = int(dList[3])
    n = len(dataLists)
    for i in range(0, n):
        tupleList.append(tuple(dataLists[i]))

     

def itemGetter(*items):
    item = items[0]
    def g(obj):
        return obj[item]
    return g

def sortedTuples(tupleList, index, backwards):
    sorted_data = None
    try:
        sorted_data = sorted(tupleList, key = itemGetter(index), reverse = backwards)
    except Exception as e:
        print (f"Had exception: {e}")
    return sorted_data

def writeSortedFile(sorted_data):
    try:
        with open('tuple_list_sorted.txt', 'w') as output:
            for item in sorted_data:
                output.write(str(item)+'\n')
            with open('tuple_list_sorted.txt', 'r') as f:
                file_contents = f.read()
                print(file_contents)
    except Exception as e:
        print (f"Had exception: {e}")

def scoped_main():
    for arg in sys.argv[1:]:
        index = 0
        backwards = True
        if arg == 'team':
            index = 0
            backwards=False         
        if arg == 'win':
            index = 1
        if arg == 'draw':
            index = 2
        if arg == 'loss':
            index = 3
        tupleList = []
        createListFromFile(tupleList, 'tuple_list.txt')
        sorted_data = sortedTuples(tupleList, index, backwards)
        writeSortedFile(sorted_data)
        

    
  

if __name__ == "__main__":
    scoped_main()

    