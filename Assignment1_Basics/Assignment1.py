_author_ = "JunlinWU, 2014301610301"

print "Please choose a subtask number(1~11): "
SubtaskNum = input()

if SubtaskNum > 11 or SubtaskNum < 1:
    print "Subtask number is error!"
    exit()

if SubtaskNum == 1:
    print "The results of Assignment1.1 is followed:"
    C = 50.0
    H = 30.0
    # D = 1.0, 3.0, 4.0, 6.0, 10.0, 35.0 # for test
    print 'Please input the values of D(float) in a comma-separated sequence: D = '
    D = input()
    Qlist = []
    n = 0
    for i in D:
        Q = (2 * C * i) / H
        Q = Q ** 0.5
        Qlist.insert(n, Q)
        n = n + 1
    print "Q =", Qlist

if SubtaskNum == 2:
    print "The results of Assignment1.2 is followed:"
    print "Please input a number a(int) between 0~9:"
    a = input()
    if a > 9 or a < 0:
        print "The number a is error!"
        exit()
    ans = a + a + 10 * a + a + 10 * a + 100 * a + a + 10 * a + 100 * a + 1000 * a
    print "The answer is:", ans

if SubtaskNum == 3:
    print "The results of Assignment1.3 is followed:"
    def SquareListGeneration(List):
        ListSquare = []
        n = 0
        for i in List:
            ListSquare.insert(n, i ** 2)
            n = n + 1
        print "The original list is:", List
        print "The square list is:", ListSquare
        print "The last 5 elements of the square list are:", ListSquare[-5], ListSquare[-4], ListSquare[-3], ListSquare[
            -2], ListSquare[-1]
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    SquareListGeneration(List)

if SubtaskNum == 4:
    print "The results of Assignment1.4 is followed:"
    print 'Please input a number list(all int) in a comma-separated sequence:'
    # List = 1, 25, 6, 7, 8, 20, 22, 204, 27, 69, 82, 97 # for test
    List = input()
    Oddlist = []
    n = 0
    for i in List:
        if (i % 2) != 0:
            Oddlist.insert(n, i)
            n = n + 1
    print "The odd numbers in the list are:", Oddlist

if SubtaskNum == 5:
    print "The results of Assignment1.5 is followed:"
    def SquareNumbersDict(dictNum):
        # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        Dictionary = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
        print "The corresponding result of the key \'", dictNum, "\' is:", Dictionary[dictNum]
    print "Please input a number a(int) between 1~10:"
    dictNum = input()
    if dictNum > 10 or dictNum < 1:
        print "The number a is error!"
        exit()
    SquareNumbersDict(dictNum)

if SubtaskNum == 6:
    print "The results of Assignment1.6 is followed:"
    print "Please input a sequence of whitespace separated words:"
    # str = Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically # for test
    str = raw_input()
    strList = str.split(" ")
    print "The words in your input are:\n", strList
    # print strList[3], strList[7], strList[13], strList[15]
    # print strList[3][0], strList[7][0], strList[13][0], strList[15][0]
    # print len(strList)
    i = 0
    while i < len(strList)-1:
        j = i + 1
        while j < len(strList):
            if strList[i] == strList[j]:
                strList.pop(j)
            j = j + 1
        i = i + 1
    print "The words after removing all duplicate words are:\n", strList
    # print len(strList)
    # n = 10
    # while n != 0:
    #     n = 0
    #     for k in range(len(strList)-1):
    #         if ord(strList[k][0]) > ord(strList[k + 1][0]):
    #             strList[k], strList[k + 1] = strList[k + 1], strList[k]
    #             n = n + 1
    n = 10
    while n != 0:
        n = 0
        for k in range(len(strList)-1):
            if cmp(strList[k], strList[k + 1]) == 1:
                strList[k], strList[k + 1] = strList[k + 1], strList[k]
                n = n + 1
    print "The words after removing all duplicate words and sorting them alphanumerically are:\n", strList

if SubtaskNum == 7:
    print "The results of Assignment1.7 is followed:"
    print 'Please input a number list(all int) in a comma-separated sequence:'
    # List = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # List = 7, 10, 100, 76, 4, 82, 9
    # List = 7, 10, 100, 76, -35, 4, 82, 9
    List = input()
    FactorialList = []
    n = 0
    for i in List:
        if i < 0:
            print "The number", i, "is illegal!"
            exit()
        elif i == 0:
            FactorialList.insert(n, 1)
        else:
            Factorial = 1
            for j in range(1, i + 1):
                Factorial = Factorial * j
            FactorialList.insert(n, Factorial)
        n = n + 1
    print "The factorial of the input numbers are:", FactorialList

if SubtaskNum == 8:
    print "The results of Assignment1.8 is followed:"
    import math
    class Circle(object):
        def __init__(self, r):
            self.R = r
        def compute_area(self):
            print 'The area of the circle is:', math.pi*self.R*self.R
    print "Please input the radius r:"
    r = input()
    circle1 = Circle(r)
    circle1.compute_area()

if SubtaskNum == 9:
    print "The results of Assignment1.9 is followed:"
    class Shape(object):
        def compute_shapearea(self, area=0):
            self.area = area
            print 'The area of the shape is:', self.area
    class Square(Shape):
        def __init__(self, length):
            self.Length = length
        def compute_squarearea(self):
            self.area = self.Length*self.Length
            print 'The area of the shape is:', self.area
    shape1 = Shape()
    shape1.compute_shapearea() # 0
    shape1.compute_shapearea(8) # 8
    square1 = Square(8)
    square1.compute_squarearea() # 64
    square1.compute_shapearea() # 0
    square1.compute_shapearea(8) # 8

if SubtaskNum == 10:
    print "The results of Assignment1.10 is followed:"
    def BinarySearchFunc(SortedList, SearchNum):
        low = 0
        high = len(SortedList) - 1
        while (low <= high):
            mid = (low + high) / 2
            midval = SortedList[mid]
            if midval < SearchNum:
                low = mid + 1
            elif midval > SearchNum:
                high = mid - 1
            else:
                return mid
    print "Please input a sorted number list:"
    # SortedList = 0, 2, 7, 11, 26, 65, 98, 99, 105, 307, 999 # for test
    # SortedList = 0, 2, 7, 11, 26, 65, 77, 98, 99, 105, 307, 999 # for test
    SortedList = input() # for test
    print "Please input a search number:"
    # SearchNum = 105
    SearchNum = input()
    BinarySearch = BinarySearchFunc(SortedList, SearchNum)
    if BinarySearch == None:
        print "The number you search does not exist!"
    else:
        print "The the index(start at 0) of element to be searched in the list is:", BinarySearch

if SubtaskNum == 11:
    print "The results of Assignment1.11 is followed:"
    import numpy
    # Suppose there are x chicks, y rabbits, then:
    # x + y = 35
    # 2x + 4y = 94
    a = [[1, 1], [2, 4]]
    a = numpy.array(a)
    b = [35, 94]
    b = numpy.array(b)
    solve = numpy.linalg.solve(a, b)
    # dot = numpy.dot(a,solve) # dot product
    print "There are %d chicks, %d rabbits" %(solve[0], solve[1])