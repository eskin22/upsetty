import itertools
import pandas as pd

def find_subsets(df):
    subsets = []
    for i in range(1, len(df.columns) + 1):
        subsets = subsets + [list(x) for x in list(itertools.combinations(df.columns, i))]
    return subsets

def find_subset_sizes(df, subsets):
    subset_sizes = []
    for s in subsets:
        curr_bool = [1] * len(df)
        for col in df.columns:
            if col in s: curr_bool = [x and y for x, y in zip(curr_bool, list(df.loc[:, col].copy()))]
            else: curr_bool = [x and not y for x, y in zip(curr_bool, list(df.loc[:, col].copy()))] 
        subset_sizes.append(sum(curr_bool))
    return subset_sizes

def create_plot_df(subsets, subset_sizes):
    plot_df = pd.DataFrame({'Intersection': subsets, 'Size': subset_sizes})
    plot_df = plot_df.sort_values(by='Size', ascending=False)
    return plot_df

def determine_pos_x_y(df, subsets, plot_df):
    max_y = max(plot_df['Size']) + 0.1 * max(plot_df['Size'])
    subsets = list(plot_df['Intersection'])
    scatter_x, scatter_y = [], []
    for i, s in enumerate(subsets):
        for j in range(len(df.columns)):
            scatter_x.append(i)
            scatter_y.append(-j * max_y / len(df.columns) - 0.1 * max_y)
    return subsets, scatter_x, scatter_y, max_y