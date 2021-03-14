input_list = list(map(int,input().split(' ')))

increase = None
mixed = False

for i in range(1,len(input_list)):
    if(input_list[i-1] < input_list[i]):
        if increase is None:
            increase = True
        elif not increase: 
            mixed = True
    else:
        if increase is None:
            increase = False
        elif increase:
            mixed = True
if mixed:
    print("mixed") 
else:
    if increase:
        print("increase")
    else:
        print("decrease")