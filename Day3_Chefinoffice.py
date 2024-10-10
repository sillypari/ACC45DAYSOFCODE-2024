# Chef in his office
# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/OFFICE

X=int(input("Enter no. of hours employees each day, \nwork from Monday to Thursday :   "))
Y=int(input("Enter no. of hours emplyees work on chill day (Friday) : "))

MT=4*X
Total=MT+Y
print(f"Total no . of hours employees work in week is : {Total} hours")