<div align="center">
    <img width="600px" src="upsetty/public/images/readme/assets/logo.png" alt="upsetty logo">

</div>

<p align="center">
    <img src="https://img.shields.io/badge/Latest%20release-v0.1.2-blue?style=flat&logo=GitHub&logoColor=white&labelColor=black&color=%23e02d60">
    <img src="https://img.shields.io/badge/Downloads-109-blue?style=flat&logo=GitHub&logoColor=white&labelColor=black&color=%235696d0">
</p>

<div align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
<img src="https://img.shields.io/badge/PLOTLY-%233F4F75?style=for-the-badge&logo=plotly&logoColor=white&labelColor=%233F4F75&color=%233F4F75" alt="Plotly">
<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
</div>

# 📖 Table of Contents

<ul>
    <a href="#🧮-what-is-upsetty" style="text-decoration:none">
        <li>🧮 What is upsetty?</li>
    </a>
        <ul>
            <a href="#🤔-whats-an-upset-plot" style="text-decoration:none">
                <li>🤔 What's an UpSet plot?</li>
            </a>
            <a href="#✨-why-create-upsetty" style="text-decoration:none">
                <li>✨ Why create upsetty?</li>
            </a>
        </ul>
    <a href="#🚀-quickstart" style="text-decoration:none">
        <li>🚀 Quickstart</li>
    </a>
        <ul>
            <a href="#⬇️-installation" style="text-decoration:none">
                <li>⬇️ Installation</li>
            </a>
            <a href="#⚙️-usage" style="text-decoration:none">
                <li>⚙️ Usage</li>
            </a>
        </ul>
    <a href="#📌-future-plans" style="text-decoration:none">
        <li>📌 Future Plans</li>
    </a>
</ul>

# 🧮 What is upsetty? <img src="upsetty/public/images/readme/assets/B_watermark.svg" height="30" align="center" alt="Watermark">

Python package for creating [UpSet plots](https://en.wikipedia.org/wiki/UpSet_Plot) using [Plotly](https://github.com/plotly/plotly.py).

### 🤔 What's an UpSet Plot?

An UpSet plot is a diagram used to quantitatively visualize sets and their interactions. They are particularly useful visuals for determining the overlap between different groups, as an alternative to [Venn](https://en.wikipedia.org/wiki/Venn_diagram) or [Euler diagrams](https://en.wikipedia.org/wiki/Euler_diagram), which can become cluttered and hard to read with more than a few sets.

<div align="center">
    <img width="600px" src="upsetty/public/images/readme/examples/comparing_venn_and_upset.png" alt="Comparing Venn Diagram and UpSet Plot for 5 Interacting Sets">
</div>

### ✨ Why create upsetty?

Currently, the number of tools to create UpSet plots is very limited. Indeed, many of the previous packages for creating these plots have been deprecated or are too verbose. 

To that end, **we offer upsetty as a lightweight, easy-to-use alternative for analyzing overlapping sets in Python.**

> #### 🤩 Like this repository? Giving a ⭐️ really helps out!

# 🚀 Quickstart

### ⬇️ Installation

```
pip install upsetty
```

### ⚙️ Usage

```
from upsetty import Upset
```

To create an UpSet plot, we structure the data like this: 

```
import pandas as pd

# create sample data ({'class_name': [boolean indicators]})
data = {
    'Class A': [True, True, True, False, False, True],
    'Class B': [True, True, True, True, True, False],
    'Class C': [False, False, False, True, True, True]
}

# convert sample data dict to pd.DataFrame
df = pd.DataFrame(data)
```

Then, simply pass the DataFrame to the `generate_plot` method to create a Plotly figure of an UpSet plot.

```
# create UpSet figure
upset = Upset.generate_plot(df)

# show the figure
upset.show()
```

Using the sample data provided above, the output is pictured below:

<p align="center">
    <img src='upsetty/public/images/readme/examples/upset_chart_demo_0.png' alt="Example UpSet Plot">
</p>

> [!NOTE]  
> If you're having trouble getting the output pictured above, you can run the demo script located at [upsetty/demo.py](upsetty/demo.py).

You can also change the colors and sizing for various aspects of the plot by passing additional parameters to the `generate_plot` function like so:

```
upset = Upset.generate_plot(
    
    # sample data
    df,

    # change category colors to a light blue, green, and yellow
    categories_colors=['#3987CA', '#FFC300', '#39CA41'],

    # change the category label color to a dark black
    categorylabel_color='#2F2F2F',

    # change the bar intersect color to a soft black
    bar_intersect_color='#454545',

    # change the marker line color to a soft black
    markerline_color='#454545'
)
```
<p align="center">
    <img src="upsetty/public/images/readme/examples/upset_chart_demo_1.png" alt="Example UpSet Plot with Custom Format">
</p>

# 📌 Future Plans

### Auto-adjusting margins for variable class labels

Currently, the **upsetty** works best with 3-4 class labels. More or less than that causes the class labels to be misaligned. Future improvements will add capabilities for auto-adjusting the margins based on the number of class labels contained in the visual. 

### Intersection highlighting

The ability to highlight specific intersections would give the user a way to focus their visual on specific set interactions as opposed to the basic highlighting.

### Intersection count makeup

The ability to show the makeups of the different classes in a set intersection count.



