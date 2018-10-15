import base64
import io

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dte
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

app = dash.Dash()
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True
server=app.server

# <editor-fold desc="variables">
width = '20%'
_0_upload_data = '0_upload-data'
_0_table = '0_table'
_2_dropdown_input_multi = '2_dropdown_input_multi'
_2_graph_box = '_2_graph_box'
_3_dropdown_input1 = '_3_dropdown_input1'
_3_dropdown_input2 = '_3_dropdown_input2'
_3_graph_histogram = '_3_graph_histogram2'
_4_dropdown_x = '_4_dropdown_x'
_4_dropdown_y = '_4_dropdown_y'
_4_dropdown_z = '_4_dropdown_z'
_4_dropdown_x_type = '_4_dropdown_x_type'
_4_dropdown_y_type = '_4_dropdown_y_type'
_4_graph = '4_figure_id_output'
_5_dropdown_x = '_5_dropdown_x'
_5_dropdown_y = '_5_dropdown_y'
_5_dropdown_z = '_5_dropdown_z'
_5_dropdown_x_type = '_5_dropdown_x_type'
_5_dropdown_y_type = '_5_dropdown_y_type'
_5_graph = '_5_graph'
_6_dropdown_x = '_6_dropdown_x'
_6_dropdown_multi_y = '_6_dropdown_multi_y'
_6_dropdown_x_type = '_6_dropdown_x_type'
_6_dropdown_y_type = '_6_dropdown_y_type'
_6_graph = '_6_graph'
_7_dropdown_x = '7_dropdown_x'
_7_dropdown_y = '7_dropdown_y'
_7_dropdown_x_type = '_7_dropdown_x_type'
_7_dropdown_y_type = '_7_dropdown_y_type'
_7_dropdown_input_multi = '7_dropdown_input_multi'
_7_dropdown_clustering_method = '7_dropdown_clustering_method'
_7_dropdown_cluster_numbers = '_7_dropdown_cluster_numbers'
_7_graph = '_7_graph'

urls = {
    'statistics': '/scienclick/datastatistics',
    'explorer': '/scienclick/dataexplorer',
    'dataclustering': '/scienclick/clustering',
    'ML': '/scienclick/ML',
    'CNN': '/scienclick/CNN',
    'words': '/scienclick/words'}
# </editor-fold>
app.layout = html.Div([
    # Banner display
    html.Div([
        html.H2(
            'Scienclick: data unleashed',
            id='title'
        ),
        html.Img(
            # src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe-inverted.png"
        )
    ],
        className="banner"
    ),

    # Body

    # <editor-fold desc="0,1- upload section">
    # ----------------------------------------------------upload section
    html.H5("0. Upload Files"),
    dcc.Upload(
        id=_0_upload_data,
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False),

    html.Br(),
    # -------------------------------table results section
    html.Br(),
    html.H5("1. Updated Table"),
    html.Div(dte.DataTable(
        rows=[{}],
        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id=_0_table)),
    # </editor-fold>
    # <editor-fold desc="2- Box plot">
    # -----------------------------------------------------Plotting section Continous multi
    html.H5("2. Box Plot"),
    html.Details([
        html.Summary('plot parameters'),
        html.Div([
            # ----------------------6- x,y,z
            html.Div([
                # -------------------------------y Drop down
                html.Div([
                    dcc.Dropdown(
                        id=_2_dropdown_input_multi, placeholder='Continous feature', multi=True
                    )
                ], style={'width': width, 'display': 'inline-block'}),

            ]),
            # -------------------------------Graph section
            dcc.Graph(id=_2_graph_box)],
        )
    ]),

    html.Br(),
    # </editor-fold>
    # <editor-fold desc="3- Histogram Section">
    # ----------------------------------------------------Histogram section

    html.H5("3. Histogram Plot"),
    html.Details([
        html.Summary('histogram parameters'),
        html.Div([
            html.Div([dcc.Dropdown(id=_3_dropdown_input1,
                                   multi=False,
                                   placeholder='Select feature')],
                     style={'width': width, 'display': 'inline-block'}),
            html.Div([dcc.Dropdown(id=_3_dropdown_input2,
                                   multi=False,
                                   placeholder='Split by')],
                     style={'width': width, 'display': 'inline-block'}),
            dcc.Graph(id=_3_graph_histogram)])
    ]),
    # </editor-fold>
    # <editor-fold desc="4- Plotting section continous">
    # -----------------------------------------------------Plotting section continous
    html.Br(),
    html.H5("4. X Y, Continous Plotting"),
    html.Details([
        html.Summary('plot parameters'),
        html.Div([
            # -------------------------------x Drop down
            html.Div([
                dcc.Dropdown(
                    id=_4_dropdown_x, placeholder='x'
                )
            ],
                style={'width': width, 'display': 'inline-block'}),
            # -------------------------------y Drop down
            html.Div([
                dcc.Dropdown(
                    id=_4_dropdown_y, placeholder='y'
                )
            ], style={'width': width, 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id=_4_dropdown_z, placeholder='Continous z'
                )
            ], style={'width': width, 'display': 'inline-block'})
        ]),
        # ----------------------3- log, Normal
        html.Div([
            # -------------------------------x Drop down
            html.Div([
                dcc.Dropdown(
                    id=_4_dropdown_x_type, options=[{'label': 'Automatic', 'value': '-'},
                                                    {'label': 'Linear', 'value': 'linear'},
                                                    {'label': 'Log', 'value': 'log'},
                                                    {'label': 'Date', 'value': 'date'},
                                                    {'label': 'Catagory', 'value': 'category'},
                                                    ], value="-"
                )
            ],
                style={'width': width, 'display': 'inline-block'}),
            # -------------------------------y Drop down
            html.Div([
                dcc.Dropdown(
                    id=_4_dropdown_y_type, options=[{'label': 'Automatic', 'value': '-'},
                                                    {'label': 'Linear', 'value': 'linear'},
                                                    {'label': 'Log', 'value': 'log'},
                                                    {'label': 'Date', 'value': 'date'},
                                                    {'label': 'Catagory', 'value': 'category'},
                                                    ], value="-"
                )
            ], style={'width': width, 'display': 'inline-block'}),

        ]),
        # -------------------------------Graph section
        dcc.Graph(id=_4_graph),
    ]),
    html.Br(),
    # ----------------------4- x,y,z

    # </editor-fold>
    # <editor-fold desc="5- Plotting section Discerete">
    # -----------------------------------------------------Plotting section Discerete
    html.H5("4. X Y, Discrete Plotting"),
    # ----------------------5- x,y,z
    html.Details([
        html.Summary('plot parameters'),
        html.Div([
            # -------------------------------x Drop down
            html.Div([
                dcc.Dropdown(
                    id=_5_dropdown_x, placeholder='x'
                )
            ],
                style={'width': width, 'display': 'inline-block'}),
            # -------------------------------y Drop down
            html.Div([
                dcc.Dropdown(
                    id=_5_dropdown_y, placeholder='y'
                )
            ], style={'width': width, 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id=_5_dropdown_z, placeholder='Discrete z'
                )
            ], style={'width': width, 'display': 'inline-block'})
        ]),
        # ----------------------5- log, Normal
        html.Div([
            # -------------------------------x Drop down
            html.Div([
                dcc.Dropdown(
                    id=_5_dropdown_x_type, options=[{'label': 'Automatic', 'value': '-'},
                                                    {'label': 'Linear', 'value': 'linear'},
                                                    {'label': 'Log', 'value': 'log'},
                                                    {'label': 'Date', 'value': 'date'},
                                                    {'label': 'Catagory', 'value': 'category'},
                                                    ], value="-"
                )
            ],
                style={'width': width, 'display': 'inline-block'}),
            # -------------------------------y Drop down
            html.Div([
                dcc.Dropdown(
                    id=_5_dropdown_y_type, options=[
                        {'label': 'Automatic', 'value': '-'},
                        {'label': 'Linear', 'value': 'linear'},
                        {'label': 'Log', 'value': 'log'},
                        {'label': 'Date', 'value': 'date'},
                        {'label': 'Catagory', 'value': 'category'},
                    ], value="-"
                )
            ], style={'width': width, 'display': 'inline-block'}),

        ]),
        # -------------------------------Graph section
        dcc.Graph(id=_5_graph),
    ]),
    html.Br(),
    # </editor-fold>
    # <editor-fold desc="6- Plotting section continous multi">
    # -----------------------------------------------------Plotting section Continous multi
    html.H5("6. X Y, Continous multi y Plotting"),
    html.Details([
        html.Summary('plot parameters'),
        html.Div([
            # ----------------------6- x,y,z
            html.Div([
                # -------------------------------x Drop down
                html.Div([
                    dcc.Dropdown(
                        id=_6_dropdown_x, placeholder='x'
                    )
                ],
                    style={'width': width, 'display': 'inline-block'}),
                # -------------------------------y Drop down
                html.Div([
                    dcc.Dropdown(
                        id=_6_dropdown_multi_y, placeholder='y', multi=True
                    )
                ], style={'width': width, 'display': 'inline-block'}),

            ]),
            # ----------------------6- log, Normal
            html.Div([
                # -------------------------------x Drop down
                html.Div([
                    dcc.Dropdown(
                        id=_6_dropdown_x_type, options=[{'label': 'Automatic', 'value': '-'},
                                                        {'label': 'Linear', 'value': 'linear'},
                                                        {'label': 'Log', 'value': 'log'},
                                                        {'label': 'Date', 'value': 'date'},
                                                        {'label': 'Catagory', 'value': 'category'},
                                                        ], value="-"
                    )
                ],
                    style={'width': width, 'display': 'inline-block'}),
                # -------------------------------y Drop down
                html.Div([
                    dcc.Dropdown(
                        id=_6_dropdown_y_type, options=[
                            {'label': 'Automatic', 'value': '-'},
                            {'label': 'Linear', 'value': 'linear'},
                            {'label': 'Log', 'value': 'log'},
                            {'label': 'Date', 'value': 'date'},
                            {'label': 'Catagory', 'value': 'category'},
                        ], value="-"
                    )
                ], style={'width': width, 'display': 'inline-block'}),

            ]),
            # -------------------------------Graph section
            dcc.Graph(id=_6_graph)],
        )
    ]),

    html.Br(),
    # </editor-fold>
    # <editor-fold desc="7- Plotting section Discerete">
    # -----------------------------------------------------Plotting section Discerete
    html.H5("7. Clustering"),
    # ----------------------7- x,y
    html.Details([
        html.Summary('plot parameters'),
        html.Div([
            # -------------------------------x Drop down
            html.Div([
                dcc.Dropdown(
                    id=_7_dropdown_x, placeholder='x to display the results'
                )
            ],
                style={'width': width, 'display': 'inline-block'}),
            # -------------------------------y Drop down
            html.Div([
                dcc.Dropdown(
                    id=_7_dropdown_y, placeholder='y to display the results'
                )
            ], style={'width': width, 'display': 'inline-block'}),
        ]),
        # ----------------------7- log, Normal
        html.Div([
            # -------------------------------x Drop down
            html.Div([
                dcc.Dropdown(
                    id=_7_dropdown_x_type, options=[{'label': 'Automatic', 'value': '-'},
                                                    {'label': 'Linear', 'value': 'linear'},
                                                    {'label': 'Log', 'value': 'log'},
                                                    {'label': 'Date', 'value': 'date'},
                                                    {'label': 'Catagory', 'value': 'category'},
                                                    ], value="-"
                )
            ],
                style={'width': width, 'display': 'inline-block'}),
            # -------------------------------y Drop down
            html.Div([
                dcc.Dropdown(
                    id=_7_dropdown_y_type, options=[
                        {'label': 'Automatic', 'value': '-'},
                        {'label': 'Linear', 'value': 'linear'},
                        {'label': 'Log', 'value': 'log'},
                        {'label': 'Date', 'value': 'date'},
                        {'label': 'Catagory', 'value': 'category'},
                    ], value="-"
                )
            ], style={'width': width, 'display': 'inline-block'}),

        ]),
        # ----------------------7- clustering params
        html.Div([
            # -------------------------------x multy
            html.Div([
                dcc.Dropdown(
                    id=_7_dropdown_input_multi, placeholder='features to be used for clustering',
                    multi=True
                )
            ], style={'width': width, 'display': 'inline-block'}),
            # -------------------------------y Drop down
            html.Div([
                dcc.Dropdown(
                    id=_7_dropdown_clustering_method, placeholder='methods',
                    options=[{'label': 'K-means', 'value': 'kmeans'},
                             {'label': 'GMM', 'value': 'gmm'},
                             {'label': 'Agglomerative Complete', 'value': 'aggc'},
                             {'label': 'Agglomerative Average', 'value': 'agga'},
                             ]
                )
            ], style={'width': width, 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id=_7_dropdown_cluster_numbers, placeholder='number of clusters',
                    options=[{'label': '2', 'value': '2'},
                             {'label': '3', 'value': '3'},
                             {'label': '4', 'value': '4'},
                             {'label': '5', 'value': '5'},

                             ]
                )
            ], style={'width': width, 'display': 'inline-block'})
        ]),
        # -------------------------------Graph section
        dcc.Graph(id=_7_graph),
    ]),
    html.Br(),
    # </editor-fold>

])
# <editor-fold desc="methods">
# file upload function
def cluster(df, method, clusternum):
    #df contains the columns that needs to be used in clustering
    scaled_data=df
    if method == "gmm":
        return GaussianMixture(n_components=clusternum).fit(scaled_data).predict(scaled_data)
    elif method == "kmeans":
        return KMeans(n_clusters=clusternum).fit(scaled_data).predict(scaled_data)
    elif method == "aggc":
        return AgglomerativeClustering(n_clusters=clusternum, linkage="complete").fit_predict(scaled_data)
    elif method == "agga":
        return AgglomerativeClustering(n_clusters=clusternum, linkage="average").fit_predict(scaled_data)
    else:
        return


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return None

    return df

# </editor-fold>
# <editor-fold desc="call backs">
# callback table creation
# <editor-fold desc="section 0,1 upload">
@app.callback(Output(_0_table, 'rows'),
              [Input(_0_upload_data, 'contents'),
               Input(_0_upload_data, 'filename')])
def update_output(contents, filename):
    if contents is not None:
        df = parse_contents(contents, filename)
        if df is not None:
            return df.to_dict('records')
        else:
            return [{}]
    else:
        return [{}]


# </editor-fold>

# <editor-fold desc="section 2; boxPlot">
# callback update options of histogram dropdown
@app.callback(Output(_2_dropdown_input_multi, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(dff.describe().columns)]


@app.callback(
    Output(component_id=_2_graph_box, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_2_dropdown_input_multi, 'value'), ]
)
def update_output_div2(table, features, ):
    dff = pd.DataFrame(table)

    traces = []
    for y in dff[features]:
        traces.append(go.Box(x=dff[y], name=str(y)))
    figure = {
        'data': traces,
        'layout': {
            'title': 'Box Plot'
            # ,'barmode':'stack'
            , 'xaxis': dict(
                title='Box Plot',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'

                )
            )
            , 'yaxis': dict(
                title='frequency',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )

        },
    }
    return figure


# </editor-fold>

# <editor-fold desc="section 3; histogram">
# callback update options of histogram dropdown
@app.callback(Output(_3_dropdown_input1, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(list(dff))]


@app.callback(Output(_3_dropdown_input2, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# # plotting Histogram
# @app.callback(
#     Output(component_id=_2_graph_histogram, component_property='figure'),
#     [Input(_0_table, 'rows'),
#      Input(_2_dropdown_input1, 'value'), ]
# )
# def update_output_div2(table, feature):
#     dff = pd.DataFrame(table)
#     data = [go.Histogram(x=dff[feature])]
#     figure = {
#         'data': data,
#         'layout': {
#             'title': 'Dash Data Visualization'
#             # ,'barmode':'stack'
#             , 'xaxis': dict(
#                 title=feature,
#                 titlefont=dict(
#                     family='Courier New, monospace',
#                     size=18,
#                     color='#7f7f7f'
#                 )
#             )
#             , 'yaxis': dict(
#                 title='frequency',
#                 titlefont=dict(
#                     family='Courier New, monospace',
#                     size=18,
#                     color='#7f7f7f'
#                 )
#             )
#
#         },
#     }
#     return figure
# plotting Histogram
@app.callback(
    Output(component_id=_3_graph_histogram, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_3_dropdown_input1, 'value'),
     Input(_3_dropdown_input2, 'value'), ]
)
def update_output_div2(table, feature, byfeature2):
    dff = pd.DataFrame(table)
    if byfeature2 is not None:
        traces = []
        for y in dff[byfeature2].unique():
            traces.append(go.Histogram(x=dff[feature][dff[byfeature2] == y], name=str(y)))
        figure = {
            'data': traces,
            'layout': {
                'title': 'Dash Data Visualization'
                # ,'barmode':'stack'
                , 'xaxis': dict(
                    title=feature,
                    titlefont=dict(
                        family='Courier New, monospace',
                        size=18,
                        color='#7f7f7f'
                    )
                )
                , 'yaxis': dict(
                    title='frequency',
                    titlefont=dict(
                        family='Courier New, monospace',
                        size=18,
                        color='#7f7f7f'
                    )
                )

            },
        }
        return figure
    else:
        dff = pd.DataFrame(table)
        data = [go.Histogram(x=dff[feature])]
        figure = {
            'data': data,
            'layout': {
                'title': 'Dash Data Visualization'
                # ,'barmode':'stack'
                , 'xaxis': dict(
                    title=feature,
                    titlefont=dict(
                        family='Courier New, monospace',
                        size=18,
                        color='#7f7f7f'
                    )
                )
                , 'yaxis': dict(
                    title='frequency',
                    titlefont=dict(
                        family='Courier New, monospace',
                        size=18,
                        color='#7f7f7f'
                    )
                )

            },
        }
        return figure


# </editor-fold>

# <editor-fold desc="section 4; continous x,y,z">
# callback update options of x1 dropdown
@app.callback(Output(_4_dropdown_x, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded

    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of y1 dropdown
@app.callback(Output(_4_dropdown_y, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of continous z1 dropdown
@app.callback(Output(_4_dropdown_z, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


@app.callback(
    Output(component_id=_4_graph, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_4_dropdown_x, 'value'),
     Input(_4_dropdown_y, 'value'),
     Input(_4_dropdown_z, 'value'),
     Input(_4_dropdown_x_type, 'value'),
     Input(_4_dropdown_y_type, 'value')
     ]
)
def update_output_div2(table, featurex, featurey, featurez, xtype, ytype):
    dff = pd.DataFrame(table)
    print(featurez)
    if not (featurez is None):
        trace = go.Scatter(
            x=dff[featurex],
            y=dff[featurey],
            mode='markers',
            marker=dict(
                size=12,
                color=dff[featurez],  # set color equal to a variable
                colorscale='Viridis',
                showscale=True
            )
        )
    else:
        trace = go.Scatter(
            x=dff[featurex],
            y=dff[featurey],
            mode='markers')
    data = [trace]
    figure = {
        'data': data,
        'layout': {
            'title': 'Dash Data Visualization'
            # ,'barmode':'stack'
            , 'xaxis': dict(
                type=xtype,
                title=featurex,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
            , 'yaxis': dict(
                type=ytype,
                title=featurey,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )

        },
    }
    return figure


# </editor-fold>


# <editor-fold desc="section 5; Discerete x,y,z"">
# callback update options of x2 dropdown
@app.callback(Output(_5_dropdown_x, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded

    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of y1 dropdown
@app.callback(Output(_5_dropdown_y, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


@app.callback(Output(_5_dropdown_z, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in
            sorted(dff.columns.difference(dff.describe().columns))]


@app.callback(
    Output(component_id=_5_graph, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_5_dropdown_x, 'value'),
     Input(_5_dropdown_y, 'value'),
     Input(_5_dropdown_z, 'value'),
     Input(_5_dropdown_x_type, 'value'),
     Input(_5_dropdown_y_type, 'value')
     ]
)
def update_output_div2(table, featurex, featurey, featurez, xtype, ytype):
    dff = pd.DataFrame(table)

    traces = []
    if not (featurez is None):
        for class_ in dff[featurez].unique():
            df_by_continent = dff[dff[featurez] == class_]
            traces.append(go.Scatter(
                x=df_by_continent[featurex],
                y=df_by_continent[featurey],
                mode='markers',
                opacity=0.7,
                marker={'size': 15},
                name=str(class_)
            ))


    else:
        traces.append(go.Scatter(
            x=dff[featurex],
            y=dff[featurey],
            mode='markers', ))
    data = traces
    figure = {
        'data': data,
        'layout': {
            'title': 'Dash Data Visualization'
            # ,'barmode':'stack'
            , 'xaxis': dict(
                type=xtype,
                title=featurex,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f',

                )
            )
            , 'yaxis': dict(
                type=ytype,
                title=featurey,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )

        },
    }
    return figure


# </editor-fold>


# <editor-fold desc="section 6; x,y, multi y continous">
@app.callback(Output(_6_dropdown_x, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded

    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


@app.callback(Output(_6_dropdown_multi_y, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(dff.describe().columns)]


@app.callback(
    Output(component_id=_6_graph, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_6_dropdown_x, 'value'),
     Input(_6_dropdown_multi_y, 'value'),
     Input(_6_dropdown_x_type, 'value'),
     Input(_6_dropdown_y_type, 'value')
     ]
)
def update_output_div2(table, featurex, listfeaturey, xtype, ytype):
    dff = pd.DataFrame(table)
    traces = []
    for y in listfeaturey:
        traces.append(go.Scatter(
            x=dff[featurex],
            y=dff[y],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=y
        ))

    data = traces
    figure = {
        'data': data,
        'layout': {
            'title': 'Dash Data Visualization'
            # ,'barmode':'stack'
            , 'xaxis': dict(
                type=xtype,
                title=featurex,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f',

                )
            )
            , 'yaxis': dict(
                type=ytype,
                title="",
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )

        },
    }
    return figure


# </editor-fold>

# <editor-fold desc="section 7: clustering">
@app.callback(Output(_7_dropdown_input_multi, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(dff.describe().columns)]


@app.callback(Output(_7_dropdown_x, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(dff.describe().columns)]


@app.callback(Output(_7_dropdown_y, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(dff.describe().columns)]



@app.callback(
    Output(component_id=_7_graph, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_7_dropdown_x, 'value'),
     Input(_7_dropdown_y, 'value'),
     Input(_7_dropdown_x_type, 'value'),
     Input(_7_dropdown_y_type, 'value'),
     Input(_7_dropdown_input_multi, 'value'),
     Input(_7_dropdown_clustering_method, 'value'),
     Input(_7_dropdown_cluster_numbers, 'value'),

     ]
)
def update_output_div2(table, x, y, xtype, ytype,multinput,method,cnum):
    dff = pd.DataFrame(table)
    dff_limited=dff[multinput]
    scaled_data=StandardScaler().fit(dff_limited).transform(dff_limited)

    z=cluster(scaled_data,method,int(cnum))



    trace = go.Scatter(
        x=dff[x],
        y=dff[y],
        mode='markers',
        marker=dict(
            size=12,
            color=z,  # set color equal to a variable
            colorscale='Viridis',
            showscale=True
        )
    )
    data = [trace]
    figure = {
        'data': data,
        'layout': {
            'title': 'Dash Data Visualization'
            # ,'barmode':'stack'
            , 'xaxis': dict(
                type=xtype,
                title=x,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f',

                )
            )
            , 'yaxis': dict(
                type=ytype,
                title=y,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )

        },
    }
    return figure

# </editor-fold>

# </editor-fold>


external_css = [
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",  # Normalize the CSS
    "https://fonts.googleapis.com/css?family=Open+Sans|Roboto"  # Fonts
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://cdn.rawgit.com/TahiriNadia/styles/faf8c1c3/stylesheet.css",
    "https://cdn.rawgit.com/TahiriNadia/styles/b1026938/custum-styles_phyloapp.css"
]
for css in external_css:
    app.css.append_css({"external_url": css})




app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)

