import numpy as np


def create_random_loss():
    a = np.random.uniform(2, 4)     # Make sine higher frequency
    b = np.random.uniform(1, 3)
    c = np.random.uniform(0.2, 1.0) # More aggressive upward curve
    d = np.random.uniform(-1.0, 1.0) # Add occasional bias/skew
    return lambda x: 3 * np.sin(a * x) + 1.5 * np.cos(b * x) + c * x**2 + d * x


def apply_curve_transform(base_func, name):
    if name == "Identity":
        return base_func
    elif name == "Clipped":
        return lambda x: np.clip(base_func(x), -2, 2)
    elif name == "Normalized":
        return lambda x: base_func(x) / (1 + abs(base_func(x)))
    elif name == "Squared":
        return lambda x: np.sign(base_func(x)) * base_func(x)**2
    elif name == "Exponential":
        return lambda x: np.exp(base_func(x) * 0.5)
    elif name == "Absolute":
        return lambda x: abs(base_func(x))
    else:
        return base_func
