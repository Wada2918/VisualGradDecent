from tkinter import ttk

def build_ui(app):
    control = ttk.Frame(app.root)
    control.pack(side="top", fill="x", padx=10, pady=5)
    ttk.Button(control, text="New Curve", command=app.new_curve).pack(side="left", padx=5)
    ttk.Button(control, text="New Start", command=app.reset_start_position).pack(side="left", padx=5)
    ttk.Button(control, text="Play", command=app.start_animation).pack(side="left", padx=5)

    param_frame = ttk.Frame(app.root)
    param_frame.pack(side="top", fill="x", padx=10, pady=5)

    for side, label, var, lr_var in [
        ("left", "Left Plot", app.transform1, app.lr1),
        ("right", "Right Plot", app.transform2, app.lr2)
    ]:
        frame = ttk.LabelFrame(param_frame, text=label)
        frame.pack(side=side, fill="x", expand=True, padx=5)
        ttk.Label(frame, text="Curve Transform:").pack()
        combo = ttk.Combobox(frame, textvariable=var, values=[
            "Identity", "Clipped", "Normalized", "Squared", "Exponential", "Absolute"
        ], state="readonly")
        combo.pack()
        combo.bind("<<ComboboxSelected>>", app.on_transform_change)
        ttk.Label(frame, text="Learning Rate:").pack()
        ttk.Entry(frame, textvariable=lr_var, width=10).pack()

    global_frame = ttk.LabelFrame(app.root, text="Global Parameters")
    global_frame.pack(side="top", fill="x", padx=10, pady=5)
    ttk.Label(global_frame, text="Min Error:").pack(side="left")
    ttk.Entry(global_frame, textvariable=app.min_error, width=10).pack(side="left", padx=5)
    ttk.Label(global_frame, text="Max Steps:").pack(side="left")
    ttk.Entry(global_frame, textvariable=app.max_steps, width=10).pack(side="left", padx=5)
