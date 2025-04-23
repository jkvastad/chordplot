import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
from math import gcd
from functools import reduce

# standard chords
major_chord = [1, Fraction(5, 4), Fraction(3, 2)]
minor_chord = [1, Fraction(6, 5), Fraction(3, 2)]
major_7_chord = [1, Fraction(5, 4), Fraction(3, 2), Fraction(9, 5)]
dim_chord = [1, Fraction(6, 5), Fraction(5, 3)]


# Helper function to compute LCM of a list
def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_list(numbers):
    return reduce(lcm, numbers)


def plot_chord(frequency_fractions, title, num_points=1000, plot_components=True):
    # Convert all inputs to Fraction objects
    frequencies = [Fraction(f) for f in frequency_fractions]

    # Extract denominators
    denominators = [f.denominator for f in frequencies]

    # Compute LCM of denominators
    lcm_val = lcm_list(denominators)

    # Set time domain: 0 to 2π * LCM
    t = np.linspace(0, 2 * np.pi * lcm_val, num_points)

    # Compute sum of sine waves
    y = sum(np.sin(float(f) * t) for f in frequencies)

    # Plot the sum
    plt.plot(t, y, label='Sum of sines')

    # Plot each component
    if plot_components:
        for f in frequencies:
            plt.plot(t, np.sin(float(f) * t), linestyle='--', alpha=0.5, label=f'sin({f}t)')

    plt.title(title)
    plt.xlabel("t")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage

# plot_chord(major_chord, "Major Chord")
# plot_chord(minor_chord, "Minor Chord")
# plot_chord(major_7_chord, "Major 7 Chord")
# plot_chord(dim_chord, "Diminished Triad Chord")


def plot_multiple_chords(frequency_sets, num_points=1000):
    # Convert to Fractions
    frequency_sets = [[Fraction(f) for f in freq_set] for freq_set in frequency_sets]

    # Get LCMs of denominators for each set
    lcm_values = [lcm_list([f.denominator for f in freq_set]) for freq_set in frequency_sets]

    # Use the largest LCM to define the time window
    max_lcm = max(lcm_values)
    t_end = 2 * np.pi * max_lcm
    t = np.linspace(0, t_end, num_points)

    # Store plot line references to get their colors
    plot_lines = []

    # Plot each sum and keep reference to the line and its period
    for i, (frequencies, lcm_val) in enumerate(zip(frequency_sets, lcm_values)):
        y = sum(np.sin(float(f) * t) for f in frequencies)
        label = f"Set {i+1}: " + ", ".join([f"{f}" for f in frequencies])
        line, = plt.plot(t, y, label=label)
        plot_lines.append((line, 2 * np.pi * lcm_val))

    # Draw vertical lines at each multiple of each set's period
    for line, period in plot_lines:
        k = 1
        while period * k <= t_end:
            plt.axvline(x=period * k, linestyle=':', color=line.get_color())
            k += 1

    plt.title(f"Superimposed Chords")
    plt.xlabel("t")
    plt.ylabel("Amplitude")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage
plot_multiple_chords([major_chord, major_7_chord])
# plot_multiple_sine_sums([major_chord])
