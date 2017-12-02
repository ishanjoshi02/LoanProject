import pydotplus
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from functions import encode_target, encode_col, TargetColumn, exclude_columns
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def get_loan_data():

    df = pd.read_csv("dataset.csv", )

    return df



if __name__ == '__main__':
    df = get_loan_data()
    df2, targets = encode_target(df)
    features = []

    for col in df2.columns:
        if col not in exclude_columns:
            df2[col] = encode_col(df2, col)
            features.append(col)
    y = df2["Target"]
    x = df2[features]
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, random_state=0
    )
    Classifier = DecisionTreeClassifier(min_samples_split=20, random_state=99)
    Classifier.fit(X_train, y_train)
    print (f"Accuracy score for testing set\n{Classifier.score(X_test, y_test)}")
    resultList = Classifier.predict(X_test)
    labelList = y_test
    for result, label in zip(resultList, labelList):
        print (targets[result])

        if result == label:
            print (True)
        else:
            print (False)

    graph=pydotplus.graph_from_dot_data(export_graphviz(Classifier, out_file=None))
    graph.write_png("tree.png")

