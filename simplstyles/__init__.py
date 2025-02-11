import os
import matplotlib.pyplot as plt

styles = {}
for dir, _, _ in os.walk("simplstyles"):
    new_styles = plt.style.core.read_style_directory(dir)
    styles.update(new_styles)
plt.style.core.update_nested_dict(plt.style.library, styles)
plt.style.core.available[:] = sorted(plt.style.library.keys())
