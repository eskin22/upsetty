import pandas as pd
from .upset import Upset

def demo():
    data = {
        'Class A': [True, True, True, False, False, True],
        'Class B': [True, True, True, True, True, False],
        'Class C': [False, False, False, True, True, True]
    }

    df = pd.DataFrame(data)

    upset = Upset.generate_plot(df)
    upset.show()