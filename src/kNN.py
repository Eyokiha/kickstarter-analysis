# import json
# import codecs
import numpy as np
import sklearn
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier

def main():
    #--- Collect data ---#
    featuresData = []
    successData  = []
    with open("../data/texts/LIWC_combi.txt", "r") as data:
        for line in data:
            line = line.replace(",",".").split()

            # ! Choose one of the following: (First is all features, second is only with significant correlation)
            # featuresData.append(line[1:])
            featuresData.append( [line[2], line[4], line[5], line[9], line[10], line[11], line[12]] )

            successData.append(float(line[0])>=100)


    #--- Train classifier ---#
    featuresDataTraining = np.array(featuresData[:750])
    featuresDataTest     = np.array(featuresData[750:])
    nbrs                 = KNeighborsClassifier(n_neighbors=3).fit(featuresDataTraining, successData[:750])


    #--- Use classifier on test set ---#
    reality   = successData[750:]
    predicted = nbrs.predict(featuresDataTest)


    #--- Calculate and output results ---#
    TP = 0
    FN = 0
    FP = 0
    TN = 0

    for i, r in enumerate(reality):
        if (r):
            if (predicted[i]):
                TP += 1
            else:
                FN += 1
        else:
            if (predicted[i]):
                FP += 1
            else:
                TN += 1

    print("True Positive:", TP)
    print("False Negative:", FN)
    print("False Positive:", FP)
    print("True Negative:", TN)

    precision = TP / (TP+FP)
    recall    = TP / (TP+FN)

    print("Precision:", precision)
    print("Recall:", recall)

    print("Accuracy:", sklearn.metrics.accuracy_score(reality, predicted, normalize=True, sample_weight=None))

    F = 2 * ((precision*recall) / (precision+recall))
    
    print("F-score:", F)


if __name__ == '__main__':
    main()