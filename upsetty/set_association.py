import itertools
import pandas as pd

def find_classes(df):
    classes = [x for x, y in zip(df.columns, df.dtypes) if y == bool]
    return classes

def find_subsets(classes):
    subsets = []
    for i in range(1, len(classes) + 1):
        subsets = subsets + [list(x) for x in list(itertools.combinations(classes, i))]
    return subsets

def determine_condition(classes, subset):
    true_string, false_string = "`{}` == True", "`{}` == False"
    conditions = []
    not_subset = [x for x in classes if x not in subset]
    for ent in subset: conditions.append(true_string.format(ent)) 
    for ent in not_subset: conditions.append(false_string.format(ent))
    condition = " and ".join(conditions) 
    
    return condition

# def find_subset_sizes(df, subsets):
#     subset_sizes = []
#     for s in subsets:
#         curr_bool = [1] * len(df)
#         for col in df.columns:
#             if col in s: curr_bool = [x and y for x, y in zip(curr_bool, list(df.loc[:, col].copy()))]
#             else: curr_bool = [x and not y for x, y in zip(curr_bool, list(df.loc[:, col].copy()))] 
#         subset_sizes.append(sum(curr_bool))
#     return subset_sizes

def find_subset_sizes(df, classes, subsets, val_col=None):
    subset_sizes = []
    for s in subsets:
        condition = determine_condition(classes, s)
        truncated_df = df.query(condition)
        if val_col is not None:
            subset_sizes.append(sum(truncated_df[val_col]))
        else:
            curr_bool = [1] * len(df)
            for cls in df.columns:
                if cls in s: curr_bool = [x and y for x, y in zip(curr_bool, list(df.loc[:, cls].copy()))]
                else: curr_bool = [x and not y for x, y in zip(curr_bool, list(df.loc[:, cls].copy()))]
            subset_sizes.append(sum(curr_bool))
            # print(sum(curr_bool))
    return subset_sizes

def create_plot_df(subsets, subset_sizes):
    plot_df = pd.DataFrame({'Intersection': subsets, 'Size': subset_sizes})
    plot_df = plot_df.sort_values(by='Size', ascending=False)
    return plot_df

def determine_pos_x_y(classes, subsets, plot_df):
    max_y = max(plot_df['Size']) + 0.1 * max(plot_df['Size'])
    subsets = list(plot_df['Intersection'])
    scatter_x, scatter_y = [], []
    for i, s in enumerate(subsets):
        for j in range(len(classes)):
            scatter_x.append(i)
            scatter_y.append(-j * max_y / len(classes) - 0.1 * max_y)
    return subsets, scatter_x, scatter_y, max_y

def find_class_counts(classes, df, val_col=None):
    sums = []
    for cls in df[classes].columns:
        if val_col is not None:
            filtered_df = df[[cls, val_col]].query(f"`{cls}` == True")[val_col]
        else: filtered_df = df[[cls]].query(f"`{cls}` == True")[cls]
        sums.append(filtered_df.sum())
    return pd.Series(sums)