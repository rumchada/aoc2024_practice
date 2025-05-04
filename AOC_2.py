data = []
file = "C:/Users/gdtbo/aoc2024_practice/data/rudolph_data.txt"
with open(file, "r") as file:
    for line in file:
        report = list(line.rstrip("\n").replace(' ',""))
        data.append(report)
row_idx = len(data)
col_idx = len(data[0])


diff_matrix = []
for row in range(row_idx):
    #converting each row in an integer
    data[row] = [int(x) for x in data[row]]
    row_diffs = []
    for j in range(col_idx - 1):
        # find the difference between each row entry
        # the abs is required for later conditionals
        diff = abs(data[row][j + 1] - data[row][j])
        row_diffs.append(diff)
    diff_matrix.append(row_diffs)
#differences matrix: intermediate data point
print(diff_matrix)

#checking each row of the diff matrix
#summarizing if the report given is unsafe or safe
# based on the differences

        
