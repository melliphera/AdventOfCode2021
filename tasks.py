def main():
    print(task1(offset=3))

def task1(offset=1):  # offset=1 for task a, 3 for task b.
    counter = 0
    with open('data\\task1.txt', 'r') as f:
        data = f.readlines()

    for i, strval in enumerate(data):
        if i >= offset:
            val = int(strval)
            compval = int(data[i-offset])
            if val > compval:
                counter += 1
            else:
                print(f'Didn\'t increment for {val=}, {compval=}')
            oldval = val

    return counter

if __name__ == '__main__':
    main()