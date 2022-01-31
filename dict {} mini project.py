#creating student name and marks from the keyboard in dictionary,display the searched item
n = int(input('enter number of students:'))
d = {}
for i in range (n):
  name = input("enter student name:")
  marks = int(input('enter student marks:'))
  d[name] = marks                            # inserting name and marks
print('all student data inserted')
while True:
    name = input('enter student name to get the marks:')
    if name in d:
        print('the marks of {} : {}'.format(name,d[name])) # projecting the result if the name is entered correctly
    else:
        print('student not found:')
    option = input('do you want search another student maeks[yes|no]')
    while option.lower() not in ['yes','no']:                # loop runs until getting yes or no
       option = input('invalid option. enter [yes|no]')
    if option.lower() == 'no':                            # if no loop breaks and comes out
        break
print('thanks for using the application')
