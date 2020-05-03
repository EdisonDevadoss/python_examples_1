

employee_file = open("employees.txt", "r")

print(employee_file.readable()) # can read or not
# print(employee_file.read()) # read all the info from the file
# print(employee_file.readline()) # read the individual line
# print(employee_file.readlines()) # array of info return

for employee in employee_file.readlines():
    print(employee)


employee_file.close()