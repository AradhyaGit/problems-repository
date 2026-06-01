def split_and_join(line):
    initial_line = line.split(" ")
    final_line = "-".join(initial_line)
    return final_line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)