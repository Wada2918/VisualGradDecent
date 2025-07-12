from utils import apply_curve_transform

def compute_gradient(f, x, eps=1e-5):
    return (f(x + eps) - f(x - eps)) / (2 * eps)

def run_optimization(base_func, x0, lr, transform_name, max_steps, min_error):
    loss_func = apply_curve_transform(base_func, transform_name)
    path = [x0]
    losses = [loss_func(x0)]
    x = x0

    for _ in range(max_steps):
        grad = compute_gradient(loss_func, x)
        x_new = x - lr * grad
        loss_new = loss_func(x_new)
        path.append(x_new)
        losses.append(loss_new)
        if abs(losses[-1] - losses[-2]) < min_error:
            break
        x = x_new

    return path, losses, loss_func
