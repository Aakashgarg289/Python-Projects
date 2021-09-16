import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    set_test_size = int(len(data) * ratio)
    train_indices = shuffled[set_test_size:]
    test_indices = shuffled[:set_test_size]
    return data.iloc[train_indices], data.iloc[test_indices]


if __name__=='__main__':
    df = pd.read_csv("data.csv")
    train, test = data_split(df, 0.4)
    X_train = train[["fever", "body pain", "age", "runnyNose", "diffBreath"]].to_numpy()
    X_test = test[["fever", "body pain", "age", "runnyNose", "diffBreath"]].to_numpy()

    Y_train = train[["infectionProb"]].to_numpy().reshape(1830, )
    Y_test = test[["infectionProb"]].to_numpy().reshape(1219, )

    clf = LogisticRegression()
    clf.fit(X_train, Y_train)

    # inpu = [102, 90, 1, 1, 1]
    # infec = clf.predict_proba([inpu])[0][1]

    f = open("model.pkl", "wb")
    pickle.dump(clf, f)
    f.close()