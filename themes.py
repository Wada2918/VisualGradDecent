def apply_theme(root):
    try:
        import sv_ttk
        sv_ttk.set_theme("dark")
    except ImportError:
        root.tk_setPalette(background="#131313", foreground="#ffffff")

import matplotlib as mpl

def style_matplotlib():
    mpl.rcParams.update({
        'figure.facecolor': '#121212',     # dark background for the whole figure
        'axes.facecolor': '#1e1e1e',       # background inside the plot box
        'axes.edgecolor': '#ffffff',
        'axes.labelcolor': '#ffffff',
        'xtick.color': '#aaaaaa',
        'ytick.color': '#aaaaaa',
        'text.color': '#ffffff',
        'grid.color': '#444444',
        'lines.linewidth': 2,
    })

STYLE_COLORS = {
    "left_curve": "#00bfff",    # Bright blue
    "right_curve": "#ffc800",   # Chartreuse
    "original_curveL": "#ffffff", # White dashed
    "original_curveR": "#ffffff", # White dashed
    "point": "#ff4c4c",         # Red
    "vector": "#ffa500",        # Orange arrow
    "path": "#888888",          # Faint gray line
}
