#!/usr/bin/env python
# coding: utf-8

#IMPORTS

import math
import os
import sys


###PREREQS###

probes = 0

#increment function
def increment_probes():
    global probes
    probes += 1

n = int(sys.argv[1])
c = []
for i in range(n):
    c.append(i)

#now, lets obtain the optimal coverage for the files that we were given
cov = ""
    #first we can clean our previous contents using "rm *.gcda pngout.png"
os.system("rm *.gcda pngout.png")

    #next, lets run every file give by "value in ./pngtest
for i in c:
    command  = "./pngtest ~/Desktop/EECS481/HW5/pc/libpng-1.6.34/large-png-suite/{}.png".format(i)
    os.system(command)

    #now, lets get our gcov output and save it to the file.
os.system("gcov *.c > gcov_output.txt")

    #now we can access gcov_output.txt and obtain the coverage percentage.
with open("gcov_output.txt", 'r') as file:
    lines = file.readlines()
    cov = lines[len(lines) - 1]
    cov = cov.strip().split(":")
    cov = cov[1].split(" ")
    cov = cov[0]
    cov = cov[:len(cov)-1]

#clearing results for our real delta debugging
os.system("rm *.gcda pngout.png")

###INTERESTING FUNCTION###

def Interesting(value):
    increment_probes()
    result = ""
    #first we can clean our previous contents using "rm *.gcda pngout.png"
    os.system("rm *.gcda pngout.png")

    #next, lets run every file give by "value in ./pngtest
    for i in value:
        command  = "./pngtest ~/Desktop/EECS481/HW5/pc/libpng-1.6.34/large-png-suite/{}.png".format(i)
        os.system(command)

    #now, lets get our gcov output and save it to the file.
    os.system("gcov *.c > gcov_output.txt")

    #now we can access gcov_output.txt and obtain the coverage percentage.
    with open("gcov_output.txt", 'r') as file:
        lines = file.readlines()
        result = lines[len(lines) - 1]
        result = result.strip().split(":")
        result = result[1].split(" ")
        result = result[0]
        result = result[:len(result)-1]

    #now we have the result, lets compare it with our desired coverage. If they are the same, return true, else return false.
    #before returning, clean once again
    os.system("rm *.gcda pngout.png")

    if result == cov:
        return True
    else:
        return False

##DELTA FUNCTION
p = []

def delta(p , c):

    if len(c) == 1:
        return c
    mid = len(c) // 2
    p2 = c[mid:]
    p1 = c[:mid]

    if Interesting(list((set(p)).union(set(p1)))):
        return delta(p, p1)
 
    if Interesting(list((set(p)).union(set(p2)))):
        return delta(p, p2)

#    else:
    delta_result_1 = delta(list(set(p).union(set(p2))), p1)
    delta_result_2 = delta(list(set(p).union(set(p1))), p2)
    final_result = list(set(delta_result_1).union(set(delta_result_2)))
    return final_result


###RESULTS

return_list = delta(p, c)
return_list.sort()

print("Return list: ", return_list)
print("Number of files: ", len(return_list))
print("Probes: ", probes)
print("Original Coverage: ", cov)

end_cov = ""

    #first we can clean our previous contents using "rm *.gcda pngout.png"
os.system("rm *.gcda pngout.png")

    #next, lets run every file give by "value in ./pngtest
for i in return_list:
    command  = "./pngtest ~/Desktop/EECS481/HW5/pc/libpng-1.6.34/large-png-suite/{}.png".format(i)
    os.system(command)

    #now, lets get our gcov output and save it to the file.
os.system("gcov *.c > gcov_output.txt")

    #now we can access gcov_output.txt and obtain the coverage percentage.
with open("gcov_output.txt", 'r') as file:
    lines = file.readlines()
    end_cov = lines[len(lines) - 1]
    end_cov = end_cov.strip().split(":")
    end_cov = end_cov[1].split(" ")
    end_cov = end_cov[0]
    end_cov = end_cov[:len(end_cov)-1]

#clearing results for our real delta debugging
os.system("rm *.gcda pngout.png")

print("Result Coverage: ", end_cov)
