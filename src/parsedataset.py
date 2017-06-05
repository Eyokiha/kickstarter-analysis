import json
import codecs

def main():
    filename = '../data/Kickstarter_2017-02-15T22_22_48_377Z.json'

    with codecs.open(filename, 'r', 'utf-8') as datafile:
        with open("../data/webrobot_dataset_parsed.txt", "w") as outputfile:
            n = 1000
            for i in range(0, n):
                project = json.loads(datafile.readline())

                # Write: url - goal - percentage reached - category
                outputfile.write(project['data']['urls']['web']['project'] + ' ' + str(project['data']['goal']) + ' ' + str(float(project['data']['pledged']) / float(project['data']['goal']) * 100) + ' ' + (project['data']['category']['slug']).replace(' ', '_') + '\n')

if __name__ == '__main__':
    main()