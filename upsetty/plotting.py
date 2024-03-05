import plotly.graph_objects as go

def add_association_markers(fig, df, subsets, scatter_x, scatter_y, max_y, params):
    fig.add_trace(go.Scatter(
        x=scatter_x,
        y=scatter_y,
        mode='markers',
        showlegend=False,
        marker=dict(
            size=params['marker_size'],
            color='#C9C9C9'
        ),
    ), row=1, col=3)
    
    for i, s in enumerate(subsets):
        scatter_x_has, scatter_y_has, marker_colors = [], [], []
        for j in range(len(df.columns)):
            if df.columns[j] in s:
                scatter_x_has.append(i)
                scatter_y_has.append(-j * max_y / len(df.columns) - 0.1 * max_y)
                marker_colors.append(params['category_color_mapping'][df.columns[j]])
                fig.add_trace(go.Scatter(
                    x=scatter_x_has,
                    y=scatter_y_has,
                    mode='markers+lines',
                    showlegend=False,
                    marker=dict(
                        size=params['marker_size'],
                        color=marker_colors,
                        line=dict(
                            color=params['markerline_color']
                        ),
                        showscale=False
                    ),
                    line=dict(
                        color=params['markerline_color'],
                        width=4
                    )
                ), row=1, col=3)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_traces(hoverinfo=None)
    
    return fig

def add_subset_counts_bar(fig, subsets, plot_df, params):
    fig.add_trace(go.Bar(
        x=list(range(len(subsets))),
        y=plot_df['Size'],
        marker=dict(
            color=params['bar_intersect_color'],

        ),
        text=plot_df['Size'],
        textposition='outside',
        hoverinfo='none',
        textfont=dict(
            size=params['datalabel_size'],
            color=params['datalabel_color']
        )
    ), row=1, col=3
    )
    
    return fig
    
def add_category_labels(fig, df, scatter_y, params):
    max_string_len = max([len(x) for x in df.columns])
    fig.add_trace(go.Scatter(
        x=[-0.01 * max_string_len]*len(df.columns), 
        y=scatter_y,
        text=[f'<b>{col}</b>' for col in df.columns],
        mode='text',
        textposition='middle center',
        showlegend=False,
        textfont=dict(
            size=params['categorylabel_size'],
            color=params['categorylabel_color']
        )
    ), row=1, col=2
    )
    
    return fig
    
def add_category_counts_bar(fig, df, params):
    true_counts = df.sum()
    
    # create bar chart for the true counts of each overarching set 
    fig.add_trace(go.Bar(
        y=true_counts.index,
        x=-true_counts.values,
        orientation='h',
        marker_color=params['categories_colors'],
        text=true_counts.values,
        textposition='outside',
        width=0.4,
        textfont=dict(
            size=params['datalabel_size'],
            color=params['datalabel_color']
        )
    ), row=1, col=1
    )
    
    return fig, true_counts
    
def autosize(fig, true_counts):
    yaxis_domain = [0.055, 0.43] if len(true_counts.keys()) == 3 else [0.035, 0.45]
    fig.update_layout(
        plot_bgcolor='white',
        xaxis1=dict(domain=[0.1, 0.3], range=[1.75*min(-true_counts.values),0]),
        xaxis2=dict(domain=[0.32, 0.39]),
        xaxis3=dict(domain=[0.39, 0.9]),
        yaxis1=dict(domain=[0, 0.5], showticklabels=False, autorange='reversed', side='right'),
        # yaxis2=dict(domain=[0.035, 0.45]),
        # yaxis2=dict(domain=[0.055, 0.43]),
        # yaxis2=dict(domain=[0.015, 0.47]),
        yaxis2=dict(domain=yaxis_domain),
        yaxis3=dict(domain=[0, 1]),
        showlegend=False
    )
    
    return fig