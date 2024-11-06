from sentiment_analysis.sentiment_model import create_model
from sentiment_analysis.preprocess import preprocess_comment
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Burada eğitmek için veri setini yüklemeniz ve işlemeniz gerekmektedir
def train_model(X_data, y_data):
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)
    input_dim = 10000  # kelime sayısı
    model = create_model(input_dim=input_dim, output_dim=128, input_length=100)
    y_train_cat = to_categorical(y_train, num_classes=3)
    y_test_cat = to_categorical(y_test, num_classes=3)
    model.fit(X_train, y_train_cat, epochs=5, validation_data=(X_test, y_test_cat))
    model.save("sentiment_model.h5")