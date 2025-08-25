import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    a = np.array(list)
    a = a.reshape((3,3))

    mean_axis0 = np.mean(a, axis=0).tolist()
    mean_axis1 = np.mean(a, axis=1).tolist()
    mean_flat = np.mean(a).tolist()
    mean = [mean_axis0, mean_axis1, mean_flat]

    var_axis0 = np.var(a, axis=0).tolist()
    var_axis1 = np.var(a, axis=1).tolist()
    var_flat = np.var(a).tolist()
    var = [var_axis0, var_axis1, var_flat]

    std_axis0 = np.std(a, axis=0).tolist()
    std_axis1 = np.std(a, axis=1).tolist()
    std_flat = np.std(a).tolist()
    std = [std_axis0, std_axis1, std_flat]

    max_axis0 = np.max(a, axis=0).tolist()
    max_axis1 = np.max(a, axis=1).tolist()
    max_flat = np.max(a).tolist()
    max = [max_axis0, max_axis1, max_flat]

    min_axis0 = np.min(a, axis=0).tolist()
    min_axis1 = np.min(a, axis=1).tolist()
    min_flat = np.min(a).tolist()
    min = [min_axis0, min_axis1, min_flat]

    sum_axis0 = np.sum(a, axis=0).tolist()
    sum_axis1 = np.sum(a, axis=1).tolist()
    sum_flat = np.sum(a).tolist()
    sum = [sum_axis0, sum_axis1, sum_flat]
    
    calculations = {
      'mean': mean,
      'variance': var,
      'standard deviation': std,
      'max': max,
      'min': min,
      'sum': sum
    }

    return calculations
