import os
import matplotlib.pyplot as plt

import simplstyles

# Register stylesheets with matplotlib
styles_path = os.path.join(simplstyles.__path__[0], "styles")
styles = {}
for dir, _, _ in os.walk(styles_path):
    new_styles = plt.style.core.read_style_directory(dir)
    styles.update(new_styles)
plt.style.core.update_nested_dict(plt.style.library, styles)
plt.style.core.available[:] = sorted(plt.style.library.keys())
