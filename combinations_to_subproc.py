#!/bin/python.exe

import subprocess
import itertools
import time

# ss = space separated
def convert_tuple_to_ss_string(tup):
    ret = ""

    for i in tup:
        ret += str(i) + " "

    return ret.strip()

def run_subprocess(cmd):
    print("executing command: '" + str(cmd) + "'")
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate()[0])

def get_filenames(path):
    cmd = "find " + path + " -type f | head -n 10"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return proc.communicate()[0].decode("utf-8")

def get_command(str_combination):
    cmd='echo "' + str(str_combination) + '" | tr " " ","'
    return cmd

def run_test(test_arr):
    for L in range(0, len(test_arr)+1):
        for subset in itertools.combinations(test_arr, L):
            print(subset)

            ret = convert_tuple_to_ss_string(subset)
            print(ret)

            # echo the string to the terminal and replace every space with a comma
            cmd=get_command(ret)

            run_subprocess(cmd)


## test harness #1 - int array
test_arr = [1, 2, 3]
run_test(test_arr)


## test harness #2 - string array
start = time.time()

test_arr = get_filenames("/Users/GWM/Git/PythonExamples/python3")
print(type(test_arr.split("\n")))
print(len(test_arr.split("\n")))
run_test(test_arr.split("\n"))

end = time.time()
print('Elapsed time: ' + str(end - start) + " seconds")