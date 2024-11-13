# src/models/models.py
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def knn_model(n_neighbors=3):
    return KNeighborsClassifier(n_neighbors=n_neighbors)

def decision_tree_model(max_depth=None):
    return DecisionTreeClassifier(max_depth=max_depth, random_state=42)

def neural_network_model(input_dim, hidden_units=64):
    model = Sequential([
        Dense(hidden_units, activation='relu', input_shape=(input_dim,)),
        Dense(hidden_units, activation='relu'),
        Dense(10, activation='softmax')  # For 10 classes in MNIST
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model
