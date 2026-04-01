import numpy as np
from numpy.typing import NDArray

class Solution:
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # return np.round(your_answer, 5)
        return np.round(np.matmul(X, weights), 5)

    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # model_prediction and ground_truth are Nx1 NumPy arrays
        # Use mean squared error
        mse = np.mean(np.square(model_prediction - ground_truth))
        return round(mse, 5)
