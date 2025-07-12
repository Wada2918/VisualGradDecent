import tkinter as tk
from themes import apply_theme, style_matplotlib
from utils import create_random_loss
from descent import run_optimization
from plot import setup_plots, update_static, animate_frame, stop_animation
from ui import build_ui
from matplotlib.animation import FuncAnimation
import numpy as np

class GradientDescentVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Gradient Descent Visualizer")
        apply_theme(self.root)
        style_matplotlib()

        self.lr1 = tk.DoubleVar(value=0.1)
        self.lr2 = tk.DoubleVar(value=0.1)
        self.min_error = tk.DoubleVar(value=1e-4)
        self.max_steps = tk.IntVar(value=100)
        self.x0 = 0.0
        self.transform1 = tk.StringVar(value="Identity")
        self.transform2 = tk.StringVar(value="Clipped")
        self.base_loss_function = create_random_loss()

        self.animation = None  # <- Add this

        self.path1 = self.path2 = []
        self.losses1 = self.losses2 = []
        self.current_step1 = self.current_step2 = 0
        self.finished1 = self.finished2 = False

        build_ui(self)
        self.fig, (self.ax1, self.ax2), self.canvas = setup_plots(self.root)
        self.reset_start_position()

        


    def new_curve(self):
        self.base_loss_function = create_random_loss()
        self.reset_start_position()

    def reset_start_position(self):
        stop_animation(self)
        self.x0 = np.random.uniform(-3, 3)
        update_static(self)

    def on_transform_change(self, *_):
        update_static(self)

    def start_animation(self):
        stop_animation(self)
        self.path1, self.losses1, self.loss_func1 = run_optimization(
            self.base_loss_function, self.x0, self.lr1.get(), self.transform1.get(),
            self.max_steps.get(), self.min_error.get()
        )
        self.path2, self.losses2, self.loss_func2 = run_optimization(
            self.base_loss_function, self.x0, self.lr2.get(), self.transform2.get(),
            self.max_steps.get(), self.min_error.get()
        )

        update_static(self)
        self.dot1, = self.ax1.plot([], [], 'ro', markersize=10)
        self.dot2, = self.ax2.plot([], [], 'ro', markersize=10)
        self.arrow1 = self.ax1.annotate('', xy=(0,0), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='red'))
        self.arrow2 = self.ax2.annotate('', xy=(0,0), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='red'))

        self.current_step1 = self.current_step2 = 0
        self.finished1 = self.finished2 = False

        self.animation = FuncAnimation(self.fig, lambda f: animate_frame(self, f),
                                       frames=max(len(self.path1), len(self.path2)),
                                       interval=150, repeat=False, blit=False)
        self.canvas.draw()
