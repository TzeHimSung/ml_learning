# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from os import listdir
from sklearn.neighbors import KNeighborsClassifier as kNN


def img2vector(filename):
    returnVec = np.zeros((1, 1024))
    with open(filename) as fr:
        for i in range(32):
            lineStr = fr.readline()
            for j in range(32):
                returnVec[0, 32 * i + j] = int(lineStr[j])
    return returnVec


def handWritingClassTest():
    hwLabels = []
    trainingFileList = listdir('./data/trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        classNumber = int(fileNameStr.split('_')[0])
        hwLabels.append(classNumber)
        trainingMat[i, :] = img2vector(
            './data/trainingDigits/%s' % (fileNameStr))
    neigh = kNN(n_neighbors=3, algorithm='auto')
    neigh.fit(trainingMat, hwLabels)
    testFileList = listdir('./data/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        classNumber = int(fileNameStr.split('_')[0])
        vectorUnderTest = img2vector('./data/testDigits/%s' % (fileNameStr))
        classifierResult = neigh.predict(vectorUnderTest)
        print('Classify result: %d\treal result: %d' %
              (classifierResult, classNumber))
        if classifierResult != classNumber:
            errorCount += 1.0
    print('total wrong: %d\nwrong rate: %f%%' %
          (errorCount, errorCount / mTest * 100))


if __name__ == '__main__':
    handWritingClassTest()
