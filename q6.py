name=input("Enter your name :")
marks = list(map(int, input("Enter your marks seperated with space: ").split()))
for x in marks:
    if x >=0 and x <=100:
        continue
    else:
        print("please enter a number between 0 and 100")
        exit()
import avg as gd
ag=gd.avg(marks)
ag=int(ag)
print(f"average of {name} is {ag}")
print(f"grade of {name} is {gd.grade(ag)} ")
