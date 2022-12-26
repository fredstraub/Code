# Create json files with increment name and coressponding log info inside

def createFiles(n):
    totalLoops = n
    i=0
    while i < totalLoops:
        i = i + 1
        f = open("myfile" + str(i) + ".json", "x")
        f.write('{ "name":"File", "Number":' + str(i) + 'log}')

# Create directories and json files with increment name and coressponding log info inside

import os

def createDirectoriesAndFiles(n):
    totalLoops = n
    topDirectory = "Test"
    parent_dir = "/Users/fred"
    path = os.path.join(parent_dir, topDirectory)
    os.mkdir(path)
    i=0
    while i < totalLoops:
        i = i + 1
        new_parent_dir = "/Users/fred/" + str(topDirectory)
        json_dir = str(i) + "directory"
        path2 = os.path.join(new_parent_dir, json_dir)
        os.mkdir(path2)
        f = open( "Test/" + json_dir + "/myfile" + str(i) + ".json", "x")
        open( "Test/" + json_dir + "/myfile" + str(i) + ".txt", "x")
        p = open( "Test/" + json_dir + "/log.txt", "x")
        p.write("This is a log file.")
        f.write('{ "name":"File", "Number":' + str(i) + 'log}')

# createDirectoriesAndFiles(4)

# Delete the files and directories. n needs to equal the number of directories.

def deleteTest(n):
    lops = n
    i = 0
    while i < n:
        i = i + 1
        os.remove("/users/fred/Test/" + str(i) + "directory/log.txt")
        os.remove("/users/fred/Test/" + str(i) + "directory/myfile"  + str(i) + ".txt")
        os.remove("/users/fred/Test/" + str(i) + "directory/myfile"  + str(i) + ".json")
        os.rmdir("/users/fred/Test/" + str(i) + "directory")
    os.rmdir("/users/fred/Test/")

# deleteTest(3)

# increment 