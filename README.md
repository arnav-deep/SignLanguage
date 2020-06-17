# SignLanguage

This project is about making a model for American Sign Language (ASL) that recognises hand gestures into letters.

<p align="center">
  <img id="ASL Alphabets" src="https://github.com/arnav-deep/SignLanguage/blob/master/MNSIT/amer_sign3.png"/>
</p>

The model uses MNIST Dataset from Kaggle, which has about 35,000 images in its dataset. Dataset is split in Train, Validate and Test sets at the ratio of 70:20:10.  The training set is further put to Data Augmentation to almost double, or even triple the inputs. Remember to not flip or rotate images as they might lead to misclassification. The data for each letter can be viualised in the below graph.

<p align="center">
  <img id="Dataset for alphabets" src="https://github.com/arnav-deep/SignLanguage/blob/master/Screenshots/dataset_graph.png"/>
</p>

The model uses 3 Convolutional Neural Networks and a Dense, Flatten and Dropout layer to form a model. Model is fitted on a batch size of 128 at a learning rate of 0.0001. The output model is saved for further use. You can find the learning curve of the model below.
All the code for this can be found in python script [train_model_asl.py](https://github.com/arnav-deep/SignLanguage/blob/master/train_model_asl.py).

The loss curve of the model is given below.

<p align="center">
  <img id="Loss curve" src="https://github.com/arnav-deep/SignLanguage/blob/master/Screenshots/loss_curve.png"/>
</p>

The saved model for 60 epochs in the [Models](https://github.com/arnav-deep/SignLanguage/tree/master/Models) is evaluated on test and validation set and gives the accuracy of 99.91% and 98.56%, which is better than most state-of-the-art systems. With a python script, a test image can be clicked via webcam and pre-processed and its alphabet can be predicted. A script can be written for live webcam sign language recognition. This will help visualise the project better.
Below, the confusion matrix of the predictions show how accurate the trained model is.

<p align="center">
  <img id="Confusion matrix" src="https://github.com/arnav-deep/SignLanguage/blob/master/Screenshots/confusion_matrix.png"/>
</p>

For future work, NLP can be introduced so the letters can be used to form meaningful words or even sentences. Grammar check can also be added, and this will give sentences as output, instead of single letters.
