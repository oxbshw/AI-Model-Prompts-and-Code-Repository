import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter=200):
    """
    Generate a 2D array of a Julia set fractal for a specific complex parameter c.

    :param xmin: Minimum x-value in the complex plane
    :param xmax: Maximum x-value in the complex plane
    :param ymin: Minimum y-value in the complex plane
    :param ymax: Maximum y-value in the complex plane
    :param width: Number of points along the x-axis for computing
    :param height: Number of points along the y-axis for computing
    :param c: Complex parameter for the Julia set
    :param max_iter: Maximum number of iterations
    :return: 2D NumPy array representing the fractal
    """
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    Zx, Zy = np.meshgrid(x, y)
    Z = Zx + 1j * Zy

    output = np.zeros(Z.shape, dtype=int)

    # For each point, iterate and see how quickly it diverges
    for i in range(max_iter):
        mask = np.abs(Z) <= 4
        Z[mask] = Z[mask] * Z[mask] + c
        output[mask] = i

    return output

# Animation setup
fig, ax = plt.subplots(figsize=(6, 6))
plt.axis('off')

# These define the region of the complex plane we visualize
xmin, xmax = -1.5, 1.5
ymin, ymax = -1.5, 1.5

width, height = 800, 800
max_iter = 200

# Initial complex parameter c
c_start = complex(-0.8, 0.156)
# Final complex parameter c
c_end   = complex(0.4, -0.3)

# Generate an initial frame
fractal_data = julia_set(xmin, xmax, ymin, ymax, width, height, c_start, max_iter)
im = ax.imshow(fractal_data, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='hot')

def update(frame):
    """
    Update function for the animation. We gradually move from c_start to c_end
    using linear interpolation over frames to create the “moving” effect.
    """
    t = frame / 100  # choose how quickly c changes over frames
    c_current = (1 - t) * c_start + t * c_end

    data = julia_set(xmin, xmax, ymin, ymax, width, height, c_current, max_iter)
    im.set_data(data)
    return [im]

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=101, interval=50, blit=True)

# If you want to save the animation (GIF), uncomment the next two lines:
# ani.save("fractal_animation.gif", writer="pillow")
# print("Created/Modified files during execution:\nfractal_animation.gif")

plt.show()