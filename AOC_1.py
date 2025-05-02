import random
left = [3,4,2,1,3,3]
right = [4,3,5,3,9,3]

def gen_rand_list(length, max_value):





def sort_int(num_list):
    num_len = len(num_list)
    for i in range(num_len):
        for j in range(0, num_len-i-1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return(num_list)

ord_left = sort_int(left)
ord_right = sort_int(right)

paired_nums =  [num for num in zip(ord_left, ord_right)]
print(paired_nums)

diff_dict = {}
for pair in paired_nums:
    num_dist = pair[0] - pair[1]
    if pair[0] < pair[1]:
        num_dist = pair[1] - pair[0]
    diff_dict[pair] = num_dist
print(diff_dict)

dist_sum = sum([diff_dict[key] for key in diff_dict])

print(dist_sum)
