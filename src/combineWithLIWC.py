def main():
    combi = []

    with open('../data/combiOutput.txt', 'r') as part1:
        for line in part1:
            line = line.split()
            data = []
            for elem in line:
                data.append(elem)
            combi.append(data)
    
    with open('../data/texts/LIWC2015 Results (TXT files (1000 files)).txt', 'r') as part2:
        for line in part2:
            line = line.split()
            if (line[0] != 'Filename'):
                i = int(line[0][7:-4])
                combi[i].extend([elem for elem in line][2:])

    with open('../data/texts/LIWC_Combi.txt', 'w') as LIWC_Combi:
        for project in combi:
            LIWC_Combi.write(' '.join(project)+'\n')


if __name__ == '__main__':
    main()