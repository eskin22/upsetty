DEFAULT_PARAMS = {
    'categories_colors': ['red', 'blue', 'green', 'purple', 'orange', 'yellow'],
    'categorylabel_size': 20,
    'categorylabel_color': 'black',
    'datalabel_color': 'black',
    'datalabel_size': 20,
    'marker_size': 20,
    'markerline_color': 'black',
    'markerline_size': 20,
    'bar_intersect_color': 'black',
}

def get_params(kwargs):
    
    params = {}
    
    for param in DEFAULT_PARAMS:
        params[param] = kwargs.get(param, DEFAULT_PARAMS[param])
        
    return params

def get_category_color_mapping(df, params):
    category_color_mapping = {category: color for category, color in zip(df.columns, params['categories_colors'])}
    params['category_color_mapping'] = category_color_mapping
    return params