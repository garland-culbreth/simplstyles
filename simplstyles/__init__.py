import os
import matplotlib.pyplot as plt

for dir, _, _ in os.walk("simplstyles"):
    styles = plt.style.core.read_style_directory(dir)
    plt.style.core.update_nested_dict(plt.style.library, styles)
plt.style.core.available[:] = sorted(plt.style.library.keys())
