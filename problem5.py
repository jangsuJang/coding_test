test_case = int(input())

for i in range(test_case):
    cursor = 0
    input_list= input()
    password_list = []

    for key in input_list:
        if(key == "<"):
            cursor = cursor-1
            if cursor < 0:
                cursor = 0

        elif(key == ">"):
            cursor = cursor+1
            if cursor > len(password_list):
                cursor = len(password_list)
        
        elif(key=="-"):
            if len(password_list) == 0:
                pass
            else:
                password_list.pop(cursor-1)
                cursor = cursor-1
        else:
            password_list.insert(cursor,key)
            cursor = cursor + 1
    print("".join(password_list))
