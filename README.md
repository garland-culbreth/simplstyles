# simplstyles

[![python versions](https://img.shields.io/badge/3.11_%7C_3.12_%7C_3.13-3776AB?style=flat-square&logo=python&logoColor=ffffff&label=python&labelColor=393f46)](https://github.com/garland-culbreth/simplstyles)
[![pypi version](https://img.shields.io/pypi/v/simplstyles?style=flat-square&logo=pypi&logoColor=ffffff&labelColor=393f46)](https://pypi.org/project/simplstyles/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=flat-square&labelColor=393f46)](https://github.com/astral-sh/uv)

Simple and clean matplotlib style sheets.

## Installation

The latest release can be installed from PyPI:

```txt
pip install simplstyles
```

## Use

Import simplstyles as you would any other package

```py
>>> import simplstyles
```

and use stylesheets as you would any other matplotlib style, with the same import structure as regular package modules:

```py
>>> import matplotlib.pyplot as plt
>>> plt.style.use("simplstyles.clean.light")
```

All stylesheets use a font stack which prefers Inter, then Helvetica, then falls back on system defaults. Inter is freely available [from its creator](https://rsms.me/inter/).

## Examples

### Clean

<p float="left">
  <img src="./examples/clean-light.png" width="24%" alt="clean" />
  <img src="./examples/clean-light-talk.png" width="24%" alt="clean talk" /> 
  <img src="./examples/clean-dark.png" width="24%" alt="clean dark" />
  <img src="./examples/clean-dark-talk.png" width="24%" alt="clean dark talk" />
</p>

### [ayu](https://github.com/ayu-theme/ayu-colors)

<p float="left">
  <img src="./examples/ayu-light.png" width="24%" alt="clean" />
  <img src="./examples/ayu-light-talk.png" width="24%" alt="clean talk" /> 
  <img src="./examples/ayu-mirage.png" width="24%" alt="clean dark" />
  <img src="./examples/ayu-mirage-talk.png" width="24%" alt="clean dark talk" />
</p>

### [Nord](https://github.com/nordtheme/nord)

<p float="left">
  <img src="./examples/nord-light.png" width="24%" alt="clean" />
  <img src="./examples/nord-light-talk.png" width="24%" alt="clean talk" /> 
  <img src="./examples/nord-dark.png" width="24%" alt="clean dark" />
  <img src="./examples/nord-dark-talk.png" width="24%" alt="clean dark talk" />
</p>

### [Everforest](https://github.com/sainnhe/everforest)

<p float="left">
  <img src="./examples/everforest-light.png" width="24%" alt="clean" />
  <img src="./examples/everforest-light-talk.png" width="24%" alt="clean talk" /> 
  <img src="./examples/everforest-dark.png" width="24%" alt="clean dark" />
  <img src="./examples/everforest-dark-talk.png" width="24%" alt="clean dark talk" />
</p>

### [Solarized](https://github.com/altercation/solarized)

<p float="left">
  <img src="./examples/solarized-light.png" width="24%" alt="clean" />
  <img src="./examples/solarized-light-talk.png" width="24%" alt="clean talk" /> 
  <img src="./examples/solarized-dark.png" width="24%" alt="clean dark" />
  <img src="./examples/solarized-dark-talk.png" width="24%" alt="clean dark talk" />
</p>

### fleet

<p float="left">
  <img src="./examples/fleet-light.png" width="24%" alt="clean" />
  <img src="./examples/fleet-light-talk.png" width="24%" alt="clean talk" /> 
  <img src="./examples/fleet-dark.png" width="24%" alt="clean dark" />
  <img src="./examples/fleet-dark-talk.png" width="24%" alt="clean dark talk" />
</p>

## Accessibility

Color cycles are selected to be as colorblind safe as possible from the basis theme's available colors. However, some limitations are inevitable as many of the basis themes were not originally developed for data visualization. Please be mindful when preparing figures to ensure they are legible to all viewers.
