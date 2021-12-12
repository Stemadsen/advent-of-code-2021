import fileinput as fi

def find_num_greater_than_previous(file_input):
    result = 0

    previous_window = [int(file_input.readline()), int(file_input.readline()), int(file_input.readline())]
    current_window = [previous_window[1], previous_window[2], int(file_input.readline())]

    while True:
        if sum(current_window) > sum(previous_window):
            result += 1
        next_line = file_input.readline()
        if not next_line:
            break
        previous_window = current_window.copy()
        current_window[0] = current_window[1]
        current_window[1] = current_window[2]
        current_window[2] = int(next_line)

    return result


print(find_num_greater_than_previous(fi.FileInput("../input.txt")))
