# emp = [1 ,"John", "cloud", "USA", "developr"]
# print("printing employee data...");
# print(" ID: %d\n Name : %s\n project : %s\n Location: %s\n desig : %s\n "%(emp[0],emp[1],emp[2],emp[3],emp[4]))

#
#
# employee = ["1", "kavi" ,"developer", "cloud", "chennai"]
#
# print(employee[0],employee[1],employee[2],employee[3],employee[4])

# string1, string2, string3 =  'savi', 'Trondheim', 'Hammer Dance'
# non_null = string1 or string2 or string3
# print(non_null)
#
# emp=[('id', '1'), ('name', 'kavi'), ('desig', 'developr'), ('project', 'cloud'), ('location', 'chennai')]
# details = dict(emp[])
# print(details)

employee1 = dict({'id': 1, 'name':'kavi', 'desig':'developr','project':'cloud','location':'chennai'})
employee2 = dict({'id': 1, 'name':'kavi', 'desig':'developr','project':'cloud','location':'chennai'})
employee_details=[employee1,employee2]
for e in employee_details:
     print(e)


def employee():
    id = "1"
    name = "kavi"
    desig = "developer"
    project = "cloud"
    location = "chennai"
    print("id: {}\nname: ({})\ndesig: {} \nproject: {} \nlocation: {}".format(id , name ,desig ,project ,location))

employee()
# matrix = [
#      [1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
# ]
# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)



# squares = list(map(lambda x: x**2, range(10)))
# print(squares)



# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("terry")
# print(queue)
