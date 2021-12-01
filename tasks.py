def main():
    print(task1(offset=3))

def task1(offset=1):  # offset=1 for task a, 3 for task b.
    """iterates through task1 dataset, checks for all items if item is greater than the object
    [offset] items earlier in the list."""
    counter = 0
    with open('data\\task1.txt', 'r') as f:
        data = f.readlines()

    for i, strval in enumerate(data[:-offset]):
        firstval = int(strval)
        secondval = int(data[i+offset])
        if secondval > firstval:
            counter += 1
        else:
            print(f'Didn\'t increment for {firstval=}, {secondval=}')

    return counter

if __name__ == '__main__':
    main()