from fileinput import FileInput

def find_num_greater_than_previous(file_input: FileInput):
    num_greater_than_previous = 0

    this_line = None
    while True:
        previous_line = this_line
        this_line = file_input.readline()
        if not previous_line:
            continue
        if not this_line:
            break
        if int(this_line) > int(previous_line):
            num_greater_than_previous += 1

    return num_greater_than_previous


print(find_num_greater_than_previous(FileInput('../input.txt')))
