import plotly.graph_objects as go
import pandas as pd
import itertools
from plotly.subplots import make_subplots

from upset import Upset

import numpy as np

data = {
    'Class A': np.random.choice([True, False], size=100000).tolist(),
    'Class B': np.random.choice([True, False, True, True], size=100000).tolist(),
    'Class C': np.random.choice([True, False], size=100000).tolist(),
    'Class D': np.random.choice([True, False], size=100000).tolist()
}

df = pd.DataFrame(data)

upset = Upset.generate_plot(df)

upset = Upset.generate_plot(
    df,
    categories_colors=['#FFC300', '#3987CA', '#39CA41', '#8439CA'],
    # datalabel_color='#454545',
    categorylabel_color='#2F2F2F',
    bar_intersect_color='#454545',
    markerline_color='#454545'
)

# upset = Upset(
#     df,
#     categories_colors=['#FFC300', '#3987CA', '#39CA41', '#8439CA'],
#     datalabel_color='#454545',
#     categorylabel_color='#2F2F2F',
#     bar_intersect_color='#454545',
#     markerline_color='#454545'
# )
# upset.generate_plot()
upset.show()