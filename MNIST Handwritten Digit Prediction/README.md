
# MNIST Handwritten Digit Classification

## Overview

This project focuses on designing a Deep Convolutional Neural Network (CNN) for the classification of handwritten digits in the MNIST dataset. The task involves training a model to accurately identify digits (0-9) based on their pixel values.

## Dataset

The MNIST dataset consists of 28x28 grayscale images of handwritten digits. It is commonly used for training various image processing systems. The dataset is split into training and testing sets, with corresponding labels for each image.

## Implementation

The project is implemented using the Keras library with a TensorFlow backend. The following steps are performed in the Jupyter Notebook (`DL Lab 6.ipynb`):

1. **Importing Packages**: Necessary libraries, including Keras, are imported.

2. **Loading the Dataset**: The MNIST dataset is loaded and divided into training and testing sets.

3. **Data Normalization**: Pixel values in the images are normalized to a range between 0 and 1 to facilitate model training.

4. **Building the CNN Model**: A sequential model is created with layers for flattening the input, followed by dense layers with ReLU activation. The output layer uses softmax activation for multiclass classification.

5. **Model Summary**: The architecture of the CNN model is displayed.

6. **Compiling the Model**: The model is compiled with the Adam optimizer and sparse categorical crossentropy loss.

7. **Model Training**: The model is trained on the training dataset using the `fit` method with 10 epochs.

8. **Model Evaluation**: The trained model is evaluated on the test dataset to measure its accuracy.

9. **Saving the Model**: The trained model is saved as `model.h5` for future use.

10. **Prediction**: The model predicts the labels for the first 10 images in the test dataset.

11. **Visualization**: The predictions are visualized by displaying the original images alongside the predicted and actual labels.

## Model Architecture

The CNN model architecture is as follows:

- Input Layer: Flatten layer with shape (28, 28).
- Hidden Layers: Dense layers with 300, 200, and 100 neurons, respectively, using ReLU activation.
- Output Layer: Dense layer with 10 neurons (softmax activation) for digit classification.

## Training

The model is trained using the Adam optimizer and sparse categorical crossentropy loss. The training process involves iterating over the dataset for 10 epochs.

## Confusion Matrix and Model Analysis

 Classification Report

              precision    recall  f1-score   support

           0       0.99      0.99      0.99       980
           1       0.99      0.99      0.99      1135
           2       0.98      0.98      0.98      1032
           3       0.97      0.98      0.97      1010
           4       0.97      0.99      0.98       982
           5       0.98      0.97      0.98       892
           6       0.98      0.98      0.98       958
           7       0.98      0.98      0.98      1028
           8       0.97      0.97      0.97       974
           9       0.98      0.96      0.97      1009

    accuracy                           0.98     10000
   macro avg       0.98      0.98      0.98     10000
weighted avg       0.98      0.98      0.98     10000

## Model Accuracy


- The model achieved an impressive accuracy of 98% on the MNIST test dataset, showcasing its effectiveness in handwritten digit classification.



## References

-   MNIST Dataset: [MNIST Dataset Documentation](https://keras.io/api/datasets/mnist/)
-   `model.evaluate` Method: [Keras Model Evaluate Documentation](https://keras.io/api/models/model_training_apis/#evaluate-method)

