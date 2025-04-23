import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


def plot_sum_of_sines(frequency_fractions, num_points=1000):
    # Convert all inputs to Fraction objects
    frequencies = [Fraction(f) for f in frequency_fractions]

    # Create time values
    t = np.linspace(0, 2 * np.pi, num_points)

    # Sum of sine waves
    y = sum(np.sin(float(f) * t) for f in frequencies)

    # Plot the sum
    plt.plot(t, y, label='Sum of sines')

    # Plot each component
    for f in frequencies:
        plt.plot(t, np.sin(float(f) * t), linestyle='--', alpha=0.5, label=f'sin({f}t)')

    plt.title("Sum of Sine Waves")
    plt.xlabel("t")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage
plot_sum_of_sines([1, Fraction(5, 4), 2])