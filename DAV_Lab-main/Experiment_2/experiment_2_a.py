"""
Experiment 2A: Working with NumPy arrays
AIM: To understand and implement various NumPy operations, including array creation, indexing, slicing,
     element-wise operations, aggregations, boolean operations, fancy indexing, reshaping, and structured arrays.
"""

import numpy as np

def main():
    print("=== EXPERIMENT 2A: NUMPY OPERATIONS ===")
    
    # Check NumPy version
    print("NumPy Version:", np.__version__)
    
    # Creating different types of arrays
    arr_1d = np.array([1, 2, 3, 4, 5])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_0d = np.array(42)
    arr_ones = np.ones((3, 3))
    
    print("\n1D Array:", arr_1d)
    print("2D Array:\n", arr_2d)
    print("0D Array:", arr_0d)
    print("Ones Array:\n", arr_ones)
    
    # Indexing and Slicing
    print("\nElement at index 2 in 1D array:", arr_1d[2])
    print("Element at row 1, column 2 in 2D array:", arr_2d[1, 2])
    print("Slice from 1D array (index 1 to 3):", arr_1d[1:4])
    print("Slice row 1 from 2D array:", arr_2d[1, :])
    
    # Element-wise operations
    arr_a = np.array([10, 20, 30])
    arr_b = np.array([1, 2, 3])
    print("\nArray A:", arr_a)
    print("Array B:", arr_b)
    print("Addition:", arr_a + arr_b)
    print("Subtraction:", arr_a - arr_b)
    print("Multiplication:", arr_a * arr_b)
    print("Division:", arr_a / arr_b)
    print("Scalar Multiplication (Array A * 2):", arr_a * 2)
    
    # Aggregations
    print("\nSum of Array A:", np.sum(arr_a))
    print("Mean of Array A:", np.mean(arr_a))
    print("Standard Deviation of Array A:", np.std(arr_a))
    
    # Element-wise comparison
    print("\nElement-wise comparison (A > B):", arr_a > arr_b)
    
    # Boolean masking
    print("Elements of A greater than 15:", arr_a[arr_a > 15])
    
    # Fancy Indexing
    indices = [0, 2]
    print("\nSelected elements from A at indices [0, 2]:", arr_a[indices])
    
    # Reshape
    reshaped_arr = arr_1d.reshape(5, 1)
    print("\nReshaped 1D array to 2D (5x1):\n", reshaped_arr)
    
    # Structured array
    structured_arr = np.array([(25, 90.5), (30, 85.2)], dtype=[('age', 'i4'), ('score', 'f4')])
    print("\nStructured array:", structured_arr)
    print("Ages from structured array:", structured_arr['age'])
    print("Scores from structured array:", structured_arr['score'])

if __name__ == "__main__":
    main()
