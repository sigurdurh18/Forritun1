def make_new_row(old_row):
    ''' Makes a new row in the Pascal triangle given the previous row '''
    
    # Special case
    if old_row == []:
        return [1]
    if old_row == [1]:
        return [1,1]

    # General case
    new_row = [1]
    length = len(old_row)
    for i in range(0, length-1):
        new_row.append(old_row[i] + old_row[i+1])
    else:
        new_row.append(1)
    return new_row

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
