#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
# %matplotlib inline

iris_dataset = load_iris()

print('Keys of iris_dataset:\n{}'.format(iris_dataset.keys()))

print(iris_dataset['DESCR'][:193]+'\n...')

print('Target names: {}'.format(iris_dataset['target_names']))
