from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM

def create_model(input_dim, output_dim, input_length):
    model = Sequential()
    model.add(Embedding(input_dim=input_dim, output_dim=output_dim, input_length=input_length))
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(3, activation='softmax'))  # Pozitif, negatif, nötr
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model