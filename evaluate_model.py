import keras
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import confusion_matrix

model_location = 'Models/base_model_asl_70'
model = load_model(model_location)

test_df = pd.read_csv("MNSIT/sign_mnist_test/sign_mnist_test.csv")

# print(test_df)

y_test = test_df['label']
del test_df['label']

x_test = test_df.values
x_test = x_test / 255
x_test = x_test.reshape(-1, 28, 28, 1)

label_binarizer = LabelBinarizer()
y_test = label_binarizer.fit_transform(y_test)

print('Accuracy of the model ' + model_location[7:] + ' is - ', model.evaluate(x_test, y_test)[1] * 100, "%")
