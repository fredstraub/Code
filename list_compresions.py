# get all the combinations of the lists [1, 2, 3] and [4, 5, 6]
print([[x,y] for x in [1,2,3] for y in [4,5,6]])

# Mulitiple of 3, 0 to 9
print([x for x in range (10) if x % 3 == 0])

# Given x, y, z, and n, print list of lists [x, y, z] not equal to n
x = 1
y = 2
z = 1
n = 3
print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if (a + b + c != n)])

# return 2nd greatest value from list[arr]
arr = [1, 3, 3, 4, 23, 543]
print(sorted(list(set(arr)))[-2])

# nested list = multi-dimensional array
# printing elements of the list
nested_list = [[1, 'Fred'], [2, 'Kristin'], [3, 'Jessica'], [4, 'Matador']]
print(len(nested_list))
print(nested_list[2])
print(nested_list[1][1])
for inner in nested_list:
    for value in inner:
        print(value)

# input method for list
for _ in range(int(input())):
        name = input()
        score = float(input())
        # make a list to hold the input
        list = []
        list.append([name, score])

"""     # sample input
    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39

    if __name__ == '__main__':
        records = [] 
        for _ in range(int(input())):
            name = input()
            score = float(input())
            records.append([name, score])
        sorted_records = sorted(list(set([x[1] for x in records])))
        second_lowest = sorted_records[1]
        
        second_lowest_record_list = []
        for student_name in records:
            if second_lowest == student_name[1]:
                second_lowest_record_list.append(student_name[0])
        for student_name in sorted(second_lowest_record_list):
            print(student_name) """

