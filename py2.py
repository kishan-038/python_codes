print("enter 5 numbers!")
li=[]
sum=0
for i in range(5):
    print(f'enter number {i}')
    li.append(int(input()))
    sum+=li[i]
li.reverse()
print('numbers in reverse order:', li)
print(f'sum is: {sum}')
print(f'average is: {sum/len(li)}')
