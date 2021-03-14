n,m = list(map(int, input().split(" ")))
card_list = list(map(int, input().split(" ")))

result = 0
list_size = len(card_list)

for i in range(list_size):
    for j in range(i+1, list_size):
        for k in range(j+1, list_size) :
            temp_result = card_list[i] + card_list[j] + card_list[k]
            if(temp_result > result and temp_result <= m):
                result = temp_result

print(result)
