import math
import numpy as np

def f(n):
    if n == 0:
        return 1
    return (f(n-1)*2) + (6 ** (n-1))

def a(data):
    np_data = np.array(data)
    return np_data.shape, np_data.mean(), np_data.std(), np_data.max()

def replace_outliers(data, x, new):
    mask = np.absolute(data) > x
    data[mask] = new
    return data

def exer2():
    data = np.array([1, 3, -5, 10, -2, 8, -12])
    threshold = 5
    replacement_value = 0
    result = replace_outliers(data, threshold, replacement_value)
    print(result)

def reshape_and_sum(data, r, c):
    data = np.reshape(data, (r, c))
    return np.sum(data, axis = 0)

def exer3():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    rows = 3
    cols = 4
    result = reshape_and_sum(data, rows, cols)
    print(result)

def create_border(data, w):
    a, b=np.shape(data)
    n_a = a+ w*2; n_b =b+ w*2
    x = (n_a, n_b)
    new = np.full(x, int(0))
    new[w:a+w, w:b+w] = data
    return new

def exer4():
    data = np.array([[1, 2], [3, 4]])
    border_width = 1
    result = create_border(data, border_width)
    print(result)

def handle_special_values(data):
    data[np.isnan(data)] = -1
    x = np.max(data[~np.isinf(data) & ~np.isnan(data)])
    data[np.isinf(data)] = x if x > 0 else 0
    return data

def exer5():
    data = np.array([np.inf, np.nan, np.inf, np.inf, -np.inf])
    result = handle_special_values(data)
    print(result)

def moving_average(arr, window_size):
    indices = np.arange(window_size) + np.arange(arr.size - window_size + 1)[:, None]
    # Use advanced indexing to create the window matrix
    windows = arr[indices]
    print(indices)
    print(windows)
    # Compute mean along the second axis (axis=1)
    return np.mean(windows, axis=1)
def exer6():
    arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    window1 = 3
    output1 = moving_average(arr1, window1)
    print("Input 1:", arr1)
    print("Window size:", window1)
    print("Output 1:", output1)
    
    arr2 = np.array([2, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    window2 = 4
    output2 = moving_average(arr2, window2)
    print("\nInput 2:", arr2)
    print("Window size:", window2)
    print("Output 2:", output2)

def dis(p_a, p_b):
    x = p_a[:, None, :] - p_b[None, :, :]
    return np.sum(x**2, axis = 2)

def find_closest_points(p_a, p_b):
    x = dis(p_a, p_b)
    i = np.argmin(x, axis = 1)
    return p_b[i, :], np.sqrt(np.min(x, axis = 1))

def exer7():
    points_a = np.array([[1, 2], [4, 5], [7, 8]])
    points_b = np.array([[2, 3], [5, 6], [8, 9], [0, 1]])
    closest_indices, min_distances = find_closest_points(points_a, points_b)
    print(closest_indices)
    print(min_distances)

def main():
    exer7()

if __name__ == "__main__":
    main()