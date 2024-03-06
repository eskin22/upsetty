from plotly.subplots import make_subplots

from .set_association import *
from .plotting import * 
from .utils import *

class Upset:
    
    def generate_plot(df, value_col=None, **kwargs):
        
        params = get_params(kwargs)
        params = get_category_color_mapping(df, params)
        
        classes = find_classes(df)
        class_counts = find_class_counts(classes, df, value_col)
        
        subsets = find_subsets(classes)
        subset_sizes = find_subset_sizes(df, classes, subsets, value_col)
        plot_df = create_plot_df(subsets, subset_sizes)
        subsets, scatter_x, scatter_y, max_y = determine_pos_x_y(classes, subsets, plot_df)
        
        fig = make_subplots(1, 3, horizontal_spacing=0)
        fig = add_association_markers(fig, classes, subsets, scatter_x, scatter_y, max_y, params)
        fig = add_subset_counts_bar(fig, subsets, plot_df, params)
        fig = add_category_labels(fig, classes, scatter_y, params)
        fig = add_category_counts_bar(fig, class_counts, params)
        fig = autosize(fig, class_counts)
        
        return fig
        