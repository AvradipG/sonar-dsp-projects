
import matplotlib.pyplot as plt
import numpy as np

def plot_polar_array_response(theta, response_db, title="Array Pattern"):
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    ax.plot(np.radians(theta), response_db)
    ax.set_title(title)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.grid(True)
    plt.show()
