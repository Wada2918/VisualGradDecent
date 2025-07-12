import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from utils import apply_curve_transform
from themes import STYLE_COLORS

def setup_plots(root):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    fig.tight_layout()
    return fig, (ax1, ax2), canvas

def update_static(app):
    app.ax1.clear()
    app.ax2.clear()
    x_range = np.linspace(-5, 5, 1000)
    base = app.base_loss_function
    f1 = apply_curve_transform(base, app.transform1.get())
    f2 = apply_curve_transform(base, app.transform2.get())

    app.ax1.plot(x_range, [f1(x) for x in x_range], color=STYLE_COLORS["left_curve"], label='Transformed')
    app.ax2.plot(x_range, [f2(x) for x in x_range], color=STYLE_COLORS["right_curve"], label='Transformed')

    app.ax1.plot(x_range, [base(x) for x in x_range], color=STYLE_COLORS["original_curveL"], alpha=0.3, label='Original')
    app.ax2.plot(x_range, [base(x) for x in x_range], color=STYLE_COLORS["original_curveR"], alpha=0.3, label='Original')

    app.ax1.plot(app.x0, f1(app.x0), 'ro')
    app.ax2.plot(app.x0, f2(app.x0), 'ro')
    app.ax1.legend()
    app.ax2.legend()
    app.ax1.grid(True, alpha=0.3)
    app.ax2.grid(True, alpha=0.3)
    app.canvas.draw()

def animate_frame(app, frame):
    done = True

    if not app.finished1 and app.current_step1 < len(app.path1):
        done = False
        x, y = app.path1[app.current_step1], app.losses1[app.current_step1]
        app.dot1.set_data([x], [y])
        if app.current_step1 + 1 < len(app.path1):
            x2, y2 = app.path1[app.current_step1 + 1], app.losses1[app.current_step1 + 1]
            app.arrow1.set_position((x, y))
            app.arrow1.xy = (x2, y2)
        app.current_step1 += 1
        if app.current_step1 >= len(app.path1):
            app.finished1 = True

    if not app.finished2 and app.current_step2 < len(app.path2):
        done = False
        x, y = app.path2[app.current_step2], app.losses2[app.current_step2]
        app.dot2.set_data([x], [y])
        if app.current_step2 + 1 < len(app.path2):
            x2, y2 = app.path2[app.current_step2 + 1], app.losses2[app.current_step2 + 1]
            app.arrow2.set_position((x, y))
            app.arrow2.xy = (x2, y2)
        app.current_step2 += 1
        if app.current_step2 >= len(app.path2):
            app.finished2 = True

    if done:
        stop_animation(app)

def stop_animation(app):
    if app.animation:
        app.animation.event_source.stop()
        app.animation = None
