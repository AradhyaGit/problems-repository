def solve(s):
    separate = s.split(" ")
    capitalised = [word.capitalize() for word in separate ]
    
    return " ".join(capitalised)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()