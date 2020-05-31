import keras
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer

model = load_model('Models/base_model_asl_50_v2')

test_df = pd.read_csv("MNSIT/sign_mnist_test/sign_mnist_test.csv")

# print(test_df)

y_test = test_df['label']
del test_df['label']

x_test = test_df.values
x_test = x_test / 255
x_test = x_test.reshape(-1, 28, 28, 1)

label_binarizer = LabelBinarizer()
y_test = label_binarizer.fit_transform(y_test)

print('Accuracy of the model is - ', model.evaluate(x_test, y_test)[1] * 100, "%")
