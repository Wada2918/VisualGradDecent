# 🌀 Gradient Descent Visualizer

An interactive desktop app to visualize how different gradient descent transformations affect optimization on complex loss surfaces.

Built with:
- 🧠 Python + Tkinter for UI
- 📈 Matplotlib for animated plots
- 🎨 sv-ttk for modern theming (dark/light)
- ⚙️ Custom loss surfaces with aggressive local minima

---

## 🔍 Features

✅ Visualize two gradient descent runs side-by-side  
✅ Choose different learning rates, transformations, and curve types  
✅ See vector directions and point-by-point descent  
✅ Randomize loss surfaces and start positions  
✅ Toggle between aggressive or smooth functions  
✅ Fully dark-mode compatible (Tkinter + Matplotlib)

---

## 🖼 Preview

> Coming soon — add screenshots or gifs showing:
> - Side-by-side curves
> - Start/stop descent
> - Clipped vs normalized descent

---

## 🛠 Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourname/gradient-descent-visualizer.git
cd gradient-descent-visualizer
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # on Linux/macOS
venv\\Scripts\\activate     # on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the App

```bash
python main.py
```

---

## 🧠 Transformations Supported

- **Identity** – Raw loss surface  
- **Clipped** – Gradient and loss capped to [-2, 2]  
- **Normalized** – Smooth out gradient magnitudes  
- **Squared** – Emphasizes large losses  
- **Exponential** – Harsh penalty for loss spikes  
- **Absolute** – Makes loss strictly positive and steep  

---

## 🎨 Customization

### Modify colors
See `themes.py` — you can update:

```python
STYLE_COLORS = {
    "left_curve": "#00bfff",
    "right_curve": "#7fff00",
    "original_curve": "#ffffff",
    "point": "#ff4c4c",
    "vector": "#ffa500",
    "path": "#888888",
}
```

### Change background color
In `themes.py`, update:

```python
mpl.rcParams['figure.facecolor'] = '#0a192f'
mpl.rcParams['axes.facecolor'] = '#0a192f'
```

---

## 🧪 Advanced Ideas

Want to extend it?
- Add support for momentum or Adam optimizer
- Export plots as GIFs
- Visualize in 3D (loss surface as `z=f(x,y)`)
- Make it web-based with PyScript or Streamlit

---

## 📄 License

MIT License. Use it, modify it, break it — just give credit.
