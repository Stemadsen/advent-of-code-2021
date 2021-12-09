import fileinput as fi

def find_num_greater_than_previous(file_input):
    num_greater_than_previous = 0

    previous_line = file_input.readline()
    this_line = file_input.readline()

    while this_line:
        if int(this_line) > int(previous_line):
            num_greater_than_previous += 1
        previous_line = this_line
        this_line = file_input.readline()

    return num_greater_than_previous


print(find_num_greater_than_previous(fi.FileInput("input.txt")))
