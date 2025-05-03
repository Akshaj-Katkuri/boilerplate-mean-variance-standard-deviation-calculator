import numpy as np


def calculate(arr):
    if len(arr) < 9: 
        raise ValueError("List must contain nine numbers.")
    
    nums = [arr[0:3], arr[3:6], arr[6:9]]
    calculations = {
        'mean': [np.mean(nums[0:3], axis=0).tolist(), np.mean(nums[0:3], axis=1).tolist(), np.mean(nums).tolist()],
        'variance': [np.var(nums[0:3], axis=0).tolist(), np.var(nums[0:3], axis=1).tolist(), np.var(nums).tolist()],
        'standard deviation': [np.std(nums[0:3], axis=0).tolist(), np.std(nums[0:3], axis=1).tolist(), np.std(nums).tolist()],
        'max': [np.max(nums[0:3], axis=0).tolist(), np.max(nums[0:3], axis=1).tolist(), np.max(nums).tolist()],
        'min': [np.min(nums[0:3], axis=0).tolist(), np.min(nums[0:3], axis=1).tolist(), np.min(nums).tolist()],
        'sum': [np.sum(nums[0:3], axis=0).tolist(), np.sum(nums[0:3], axis=1).tolist(), np.sum(nums).tolist()]
    }

    return calculations
