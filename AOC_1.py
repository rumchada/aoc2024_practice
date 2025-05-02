# AOC_2024_Day1:
#by holding the two lists up side by side (your puzzle input),
# it quickly becomes clear that the lists aren't very similar.
# Maybe you can help The Historians reconcile their lists?

#Within each pair, figure out how far apart the two numbers are;
# you'll need to add up all of those distances.
# For example, if you pair up a 3 from the left list with a 7 from the right list,
# the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

#find the total distance between the left list and the right list, add up the distances between all of the pairs you found.
# In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

#Your actual left and right lists contain many location IDs. What is the total distance between your lists?
import random

def gen_rand_list(length, max_value):
    #generates a random list of integers
    random_list = []
    for _ in range(length):
        random_list.append(random.randint(0, max_value))
    return random_list
# call the function twice as the "left" and "right" list
left = gen_rand_list(20, 100)
right = gen_rand_list(20, 100)

def sort_int(num_list):
    #sort them based on numerical order
    num_len = len(num_list)
    for i in range(num_len):
        for j in range(0, num_len-i-1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return(num_list)

ord_left = sort_int(left)
ord_right = sort_int(right)

#zip them together to make tuples as "pairs"
paired_nums =  [num for num in zip(ord_left, ord_right)]
print(paired_nums)

#make a dictionary of the paired numbers and their differences as the problem refers to them "distances"
diff_dict = {}
for pair in paired_nums:
    num_dist = pair[0] - pair[1]
    if pair[0] < pair[1]:
        num_dist = pair[1] - pair[0]
    diff_dict[pair] = num_dist
print(diff_dict)

#take the sum of the values of "distances" of the pairs
dist_sum = sum([diff_dict[key] for key in diff_dict])

print(dist_sum)
