import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def julia_set(width, height, c, x_range=(-2, 2), y_range=(-2, 2), max_iter=100):
    """Generate Julia set fractal array"""
    x = np.linspace(x_range[0], x_range[1], width)
    y = np.linspace(y_range[0], y_range[1], height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    fractal = np.zeros(Z.shape, dtype=np.float32)

    for i in range(max_iter):
        mask = np.abs(Z) < 10  # Escape radius
        Z[mask] = Z[mask]**2 + c
        fractal += mask.astype(np.float32)

    return np.log(fractal + 1)

# Figure setup
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')
img = ax.imshow(np.random.rand(400, 400), cmap='twilight_shifted',
                interpolation='bicubic', vmin=0, vmax=5)

# Animation parameters
params = {
    'width': 400,
    'height': 400,
    'max_iter': 70,
    'x_range': (-1.5, 1.5),
    'y_range': (-1.5, 1.5)
}

def init():
    """Initialize animation frame"""
    theta = 0
    c = 0.7885 * np.exp(1j * theta)
    img.set_data(julia_set(c=c, **params))
    return [img]

def animate(frame):
    """Update frame with new Julia set parameters"""
    theta = 2 * np.pi * frame / 100
    c = 0.7885 * np.exp(1j * theta)
    img.set_data(julia_set(c=c, **params))
    return [img]

# Create animation
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=50, blit=True)

# Save animation
anim.save('julia_fractal_animation.mp4', writer='ffmpeg',
          fps=20, dpi=100, bitrate=2000)

plt.show()

# Created/Modified files during execution:
print("julia_fractal_animation.mp4")