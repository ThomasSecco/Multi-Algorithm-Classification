# src/data_loader.py
from sklearn.datasets import load_iris
from tensorflow.keras.datasets import mnist

def load_iris_data():
    data = load_iris()
    X, y = data.data, data.target
    return X, y

def load_mnist_data():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train, X_test = X_train.reshape(-1, 28 * 28) / 255.0, X_test.reshape(-1, 28 * 28) / 255.0
    return X_train, X_test, y_train, y_test
