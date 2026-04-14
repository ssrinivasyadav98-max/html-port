from sklearn.linear_model import LogisticRegression
import numpy as np

def train_model(data):
    X = np.array([[d["hours"]] for d in data])
    y = np.array([d["result"] for d in data])

    model = LogisticRegression()
    model.fit(X, y)

    return model