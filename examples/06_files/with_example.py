with open('r1.txt') as config, open('result.txt', 'w') as output:
    for line in config:
        print(line.split())
        output.write(line)


with open('r1.txt') as config:
    with open('result.txt', 'w') as output:
        for line in config:
            print(line.split())
            output.write(line)

