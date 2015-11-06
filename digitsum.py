__author__ = 'MOHAMMED REDA JAIFAR'

from sys import argv
import re

script, filename = argv

def sum(filename):
    file = open(filename, 'r')
    sum = 0
    for line in file:
        digitList = re.findall('[0-9]+', line)
        sum = sum + sum_of_digitList(digitList)
    return sum

def sum_of_digitList(digitList):
    sum = 0
    try:
        for item in digitList:
            temp = int(item)
            sum = sum + temp
    except ValueError:
        return 0
    return sum

def main():
    print sum(filename)

if __name__ == "__main__":
    main()