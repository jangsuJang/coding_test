test_case = int(input())

for i in range(test_case):
    n,m = list(map(int,input().split(" ")))
    queue = list(map(int,input().split(" ")))
    queue = [(i,idx) for idx, i in enumerate(queue)]

    count = 0
    print(queue)
    while max(queue,key= lambda x:x[0])[1] != m:
        max_num = max(queue,key= lambda x:x[0])[0]
        if(max_num == queue[0][0]):
            queue.pop(0)
            count = count+1
        else:
            temp_node = queue[0]
            queue.pop(0)
            queue.append(temp_node)
        print(queue)
    count = count+1


    # print(n)
    # print(m)
    print(queue)
    print(count)

