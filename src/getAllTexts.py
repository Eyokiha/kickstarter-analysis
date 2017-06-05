import json
import codecs

def main():
    filename = '../data/ks_scraped_data.jl'

    with codecs.open(filename, 'r', 'utf-8') as ksFile:
        for i in range(0,998):
            # Write all project decription texts to separate txt files for processing in LIWC
            with codecs.open("../data/texts/allText"+str(i)+".txt", "w", "utf-8") as allText:
                data = json.loads(ksFile.readline())
                allText.write(data['descText'])


if __name__ == '__main__':
    main()