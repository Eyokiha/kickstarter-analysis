import json
import codecs
import string

def readability(text):
    # RE = 206.835 – (1.015 * (total words / total sentences)) – (84.6 * (total syllables / total words))
    text = text.lower()

    totalSyllables    = 0
    totalSentences    = 0
    prevLetterIsVowel = 0
    for letter in text:
        # calculate total number of syllables in text
        if letter in 'aeiouy':
            if not prevLetterIsVowel:
                totalSyllables += 1
            prevLetterIsVowel = 1
        else:
            prevLetterIsVowel = 0

        # calculate total number of sentences in text
        if letter in '!?.':
            totalSentences += 1

    # calculate total number of words in text
    for ch in string.punctuation:
        text = text.replace(ch, ' ')
    totalWords = len(text.split())

    if (totalSentences == 0 or totalWords == 0):
        RE = 100
    else:
        RE = 206.835 - (1.015 * (totalWords / totalSentences)) - (84.6 * (totalSyllables / totalWords))

    return RE


def main():
    with codecs.open("../data/ks_scraped_data.jl", "r", "utf-8") as ksFile:
        with open("../data/webrobot_dataset_parsed.txt", "r") as wrFile:
            with codecs.open("../data/combiOutput.txt", "w", "utf-8") as combiOutput:
                for line in wrFile:
                    l = ksFile.readline()
                    if (l != ''):
                        data  = json.loads(l)
                        
                        words = len(data['descText'].split())
                        RE    = readability(data['descText'])

                        splitLine = line.split()
                        goal      = int(splitLine[1])
                        perc      = splitLine[2]

                        # Write: percentage of goal reached - goal - image count - duration - word count - readability score
                        combiOutput.write(str(perc) + ' ' + str(goal) + ' ' + str(data['imgCount']) + ' ' + str(data['duration']) + ' ' + str(words) + ' ' + str(RE) + '\n')


if __name__ == '__main__':
    main()