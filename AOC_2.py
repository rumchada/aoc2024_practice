data = []
file = "C:/Users/gdtbo/aoc2024_practice/data/rudolph_data.txt"
with open(file, "r") as file:
    for line in file:
        report = list(line.rstrip("\n").replace(' ',""))
        data.append(report)
# one day we can build this out generate a 2d list using numpy

#tomorrow gonna have to annotate this so that I can use it later

def get_diff_matrix(data):
    # for reading purposed I stored the len of the rows and cols into vars
    row_idx = len(data)
    col_idx = len(data[0])
    #set up diff matrix
    diff_matrix = []
    # iterating through each of the rows
    for row in range(row_idx):
        #converting each row into an integer
        # for each entry in the row convert to in an integer
        # Set up a the row differences list
        data[row] = [int(x) for x in data[row]]
        row_diffs = []
        for j in range(col_idx - 1):
            # find the difference between each row entry
            # the abs is required for later conditionals
            diff = data[row][j + 1] - data[row][j]
            row_diffs.append(diff)
        diff_matrix.append(row_diffs)
    #differences matrix: intermediate data point
    return diff_matrix

diff_matrix = get_diff_matrix(data)

#checking each row of the diff matrix
#summarizing if the report given is unsafe or safe
# based on the differences
def get_sign(number):
   if (number>0):
      return 1
   elif (number<0):
      return -1
   else:
      return 0

def get_report(diff_matrix):
    report_sum_list = []
    for row in diff_matrix:
        unsafe = False
        direction = None
        for entry in row:
            if abs(entry) >= 4:
                unsafe = True
            if entry == 0:
                unsafe = True

            sign = get_sign(entry)
            if direction is None:
                direction = sign
            elif sign != direction:
                unsafe = True
                break

        if unsafe:
            report_sum_list.append("Unsafe")
        else:
            report_sum_list.append("Safe")

    report_dict = {}
    for row, report in zip(data, report_sum_list):
        report_dict[str(row)] = report

    return report_dict

print(get_report(diff_matrix))

        
