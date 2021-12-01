def main():
    print(task1a())

def task1a():
    counter = 0
    with open('data\\task1.txt', 'r') as f:
        data = f.readlines()

    oldval = int(data[0]) # set oldval to the first data so the first test returns 0 always
    for strval in data:
        val = int(strval) # take off newline, turn to number
        if val > oldval:
            counter += 1
        else:
            print(f'Didn\'t increment for {val=}, {oldval=}')
        oldval = val

    return counter

if __name__ == '__main__':
    main()