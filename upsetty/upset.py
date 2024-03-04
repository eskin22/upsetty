from plotly.subplots import make_subplots

from .set_association import *
from .plotting import * 
from .utils import *

class Upset:
    
    def generate_plot(df, **kwargs):
        
        params = get_params(kwargs)
        params = get_category_color_mapping(df, params)
        
        subsets = find_subsets(df)
        subset_sizes = find_subset_sizes(df, subsets)
        plot_df = create_plot_df(subsets, subset_sizes)
        subsets, scatter_x, scatter_y, max_y = determine_pos_x_y(df, subsets, plot_df)
        
        fig = make_subplots(1, 3, horizontal_spacing=0)
        fig = add_association_markers(fig, df, subsets, scatter_x, scatter_y, max_y, params)
        fig = add_subset_counts_bar(fig, subsets, plot_df, params)
        fig = add_category_labels(fig, df, scatter_y, params)
        fig, true_counts = add_category_counts_bar(fig, df, params)
        fig = autosize(fig, true_counts)
        
        return fig
        