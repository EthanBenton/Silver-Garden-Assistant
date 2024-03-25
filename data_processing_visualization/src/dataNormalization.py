import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.discriminant_analysis import StandardScaler

def preprocess_data(data):
    try:
        # preprocessing steps here
        scaler = StandardScaler()
        normalized_data = scaler.fit_transform(data)
        return normalized_data
    except Exception as e:
        print("Error preprocessing data:", str(e))
        return None