try:
    "hello" + 1
except TypeError:
    print("NOPE")

#raise TypeError ("I raised TypeError!")

#READ FILE
my_file = open("file.txt", "rt")

#print all lines
for line in my_file:
    print(line)

my_file.close()

#WRITE FILE
my_file = open("file.txt", "wt")

#print all lines
fleet = {'BS62': 'Pegasus', 'BS75': 'Galactica', 'BS36': 'Valkyrie'}
for designated_no in fleet.keys():
    my_file.write(fleet[designated_no] + '\n')

my_file.close()

#IF FILE DOESN'T EXIST
my_file = open("non_existing_file.txt", "rt")

#READING FILE AND HANDLE EXCEPTION
try:
    my_file = open("non_existing_file.txt", "rt")
    try:
        for line in my_file:
            print(line)
    finally:
        my_file.close()
except IOError as e:
    #print what's wrong
    print(e)

#COMPLICATED SOLUTION
my_file = None
try:
    my_file = open("non_existing_file.txt", "rt")

    for line in my_file:
        print(line)

except IOError as e:
    print(e)
finally:
    if my_file is not None:
        my_file.close()

#EASY WITH "with" STATEMENT
with open("test.py", "rt") as my_file:
    for line in my_file:
        print(line)
