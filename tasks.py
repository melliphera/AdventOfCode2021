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

def task2a():
    with open('data\\task2.txt', 'r') as f:
        data = f.readlines()
    depth = 0
    distance = 0

    for line in data:
        match line.split(" "):
            case ['forward', num]:
                distance += int(num)
            case ['down', num]:
                depth += int(num)
            case ['up', num]:
                depth -= int(num)

    return depth*distance

def task2b():
    with open('data\\task2.txt', 'r') as f:
        data = f.readlines()
    depth = 0
    aim = 0
    distance = 0

    for line in data:
        match line.split(" "):
            case ['forward', num]:
                distance += int(num)
                depth += int(num)*aim
            case ['down', num]:
                aim += int(num)
            case ['up', num]:
                aim -= int(num)

    return depth*distance

def task3a():
    from bitstring import BitArray

    with open('data\\task3.txt', 'r') as f:
        data = f.readlines()

    out = ""
    half = len(data)//2

    bflag = False
    for j in range(len(data[0])):
        counter = 0
        for d, val in enumerate(data):
            if val[j] == '\n':
                bflag = True
                break
            if int(val[j]):
                counter += 1
        print(counter)
        if bflag:
            break

        if counter >= half:
            bit = "1"
        else:
            bit = "0"
        out += bit
    print(out)
    bits = len(out)
    bin = BitArray(bin=out)
    ans = bin.uint * (2 ** bits - bin.uint - 1)
    return(ans)

def task3b1(data=None):
    if not data:
        with open('data\\task3.txt', 'r') as f:
            data = f.readlines()

    bflag = False
    commons = ""
    half = len(data)//2
    for j in range(len(data[0])):
        counter = 0
        for d, val in enumerate(data):
            if val[j] == '\n':
                bflag = True
                break
            if int(val[j]):
                counter += 1
        print(counter)
        if bflag:
            break

        if counter >= half:
            bit = "1"
        else:
            bit = "0"
        commons += bit

    return commons

def task3b():
    from copy import copy
    with open('data\\task3.txt', 'r') as f:
        data = f.readlines()
    d2 = copy(data)
    bitlength = len(data[0]) - 1

    out = ""
    bflag = False
    for i in range(bitlength):
        removals = []
        half = len(data) // 2
        counter = 0

        for d in data:
            if d[i] == '1':
                counter += 1
            elif d[i] == '0':
                pass
            else:
                bflag = True
                break
        if bflag:
            break
        elif counter >= half:
            outbit = "1"
        else:
            outbit = "0"
        out += outbit
        print(out)

        for j, d in enumerate(data):
            if d[i] != out[i]:
                removals.append(j)

        removals = removals[::-1]
        for i in removals:
            del data[i]

    out = ""
    bflag = False
    for i in range(bitlength):
        if len(d2) == 1:
            break
        removals = []
        half = len(d2) // 2
        counter = 0

        for d in d2:
            if d[i] == '1':
                counter += 1
            elif d[i] == '0':
                pass
            else:
                bflag = True
                break
        if bflag:
            break
        elif counter >= half:
            outbit = "0"
        else:
            outbit = "1"
        out += outbit
        print(out)

        for j, d in enumerate(d2):
            if d[i] != out[i]:
                removals.append(j)

        removals = removals[::-1]
        for i in removals:
            del d2[i]
    a, b = data[0][:-1], d2[0][:-1]
    print(a, b, int(a, 2)*int(b, 2))


if __name__ == '__main__':
    print(task3b())