
n = int(input())
stack= []
result=[]

count = 1
for i in range(1,n+1):
    targetNum = int(input())
    while count <= targetNum:
        stack.append(count)
        count = count +1
        result.append("+")
    print(stack)
    print(result)
    if stack[-1] == targetNum:
        stack.pop(-1)
        result.append("-")
        print(stack)
        print(result)
    else:
        print("NO")
        exit(0)

print('\n'.join(result))




# n = int(input())
# sequence = list(range(0,n+1))
# stack= []

# for i in range(n):
#     targetNum = int(input())
    
#     if len(stack) != 0 and stack[0] is targetNum:
#         stack.pop(0)
#         print("-")
#         print("current stack is ",stack)
#         print("current sequence is ",sequence)
#     else:
#         targetIndex = sequence.index(targetNum)
#         for i in range(targetIndex,0,-1):
#             stack.append(sequence[i])
#             print("+")
#         sequence = sequence[targetIndex+1:]
#         print("+")
#         print("-")
#         print("current stack is ",stack)
#         print("current sequence is ",sequence)
        