import base64
import io
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dte
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = dash.Dash()
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True
server=app.server

# <editor-fold desc="variables">
width = '20%'
_0_upload_data = '0_upload-data'
_0_table = '0_table'
_2_dropdown_input = '_2_dropdown_input'
_2_graph_histogram = '_2_graph_histogram'
_3_dropdown_x = '_3_dropdown_x'
_3_dropdown_y = '_3_dropdown_y'
_3_dropdown_z = '_3_dropdown_z'
_3_dropdown_x_type = '_3_dropdown_x_type'
_3_dropdown_y_type = '_3_dropdown_y_type'
_3_graph = '3_figure_id_output'
_4_dropdown_x = '_4_dropdown_x'
_4_dropdown_y = '_4_dropdown_y'
_4_dropdown_z = '_4_dropdown_z'
_4_dropdown_x_type = '_4_dropdown_x_type'
_4_dropdown_y_type = '_4_dropdown_y_type'
_4_graph = '_4_graph'
_5_dropdown_x = '_5_dropdown_x'
_5_dropdown_multi_y = '_5_dropdown_multi_y'
_5_dropdown_x_type = '_5_dropdown_x_type'
_5_dropdown_y_type = '_5_dropdown_y_type'
_5_graph = '_5_graph'
# </editor-fold>
app.layout = html.Div([

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
    html.Div(dte.DataTable(rows=[{}], id=_0_table)),
    # </editor-fold>
    # <editor-fold desc="2- Histogram Section">
    # ----------------------------------------------------Histogram section
    html.Br(),
    html.H5("2. Histogram Plot"),
    html.Div([dcc.Dropdown(id=_2_dropdown_input,
                           multi=False,
                           placeholder='Select feature')],
             style={'width': width, 'display': 'inline-block'}),
    dcc.Graph(id=_2_graph_histogram),
    # </editor-fold>
    # <editor-fold desc="3- Plotting section continous">
    # -----------------------------------------------------Plotting section continous
    html.H5("3. X Y, Continous Plotting"),

    html.Br(),
    # ----------------------3- x,y,z
    html.Div([
        # -------------------------------x Drop down
        html.Div([
            dcc.Dropdown(
                id=_3_dropdown_x, placeholder='x'
            )
        ],
            style={'width': width, 'display': 'inline-block'}),
        # -------------------------------y Drop down
        html.Div([
            dcc.Dropdown(
                id=_3_dropdown_y, placeholder='y'
            )
        ], style={'width': width, 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(
                id=_3_dropdown_z, placeholder='Continous z'
            )
        ], style={'width': width, 'display': 'inline-block'})
    ]),
    # ----------------------3- log, Normal
    html.Div([
        # -------------------------------x Drop down
        html.Div([
            dcc.Dropdown(
                id=_3_dropdown_x_type, options=[{'label': 'Automatic', 'value': '-'},
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
                id=_3_dropdown_y_type, options=[{'label': 'Automatic', 'value': '-'},
                                                {'label': 'Linear', 'value': 'linear'},
                                                {'label': 'Log', 'value': 'log'},
                                                {'label': 'Date', 'value': 'date'},
                                                {'label': 'Catagory', 'value': 'category'},
                                                ], value="-"
            )
        ], style={'width': width, 'display': 'inline-block'}),

    ]),
    # -------------------------------Graph section
    dcc.Graph(id=_3_graph),
    # </editor-fold>
    # <editor-fold desc="4- Plotting section Discerete">
    # -----------------------------------------------------Plotting section Discerete
    html.H5("4. X Y, Discrete Plotting"),

    html.Br(),
    # ----------------------4- x,y,z
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
                id=_4_dropdown_z, placeholder='Discrete z'
            )
        ], style={'width': width, 'display': 'inline-block'})
    ]),
    # ----------------------4- log, Normal
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
                id=_4_dropdown_y_type, options=[
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
    dcc.Graph(id=_4_graph),
    # </editor-fold>
    # <editor-fold desc="5- Plotting section continous multi">
    # -----------------------------------------------------Plotting section Continous multi
    html.H5("5. X Y, Continous multi y Plotting"),

    html.Br(),
    # ----------------------5- x,y,z
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
                id=_5_dropdown_multi_y, placeholder='y', multi=True
            )
        ], style={'width': width, 'display': 'inline-block'}),

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
    # </editor-fold>
    # -------------------------------------------------------

    # html.P(html.Div(id='output-id', children='salam'))
])
# <editor-fold desc="methods">
# file upload function
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


# <editor-fold desc="section 2; histogram">
# callback update options of histogram dropdown
@app.callback(Output(_2_dropdown_input, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# plotting Histogram
@app.callback(
    Output(component_id=_2_graph_histogram, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_2_dropdown_input, 'value'), ]
)
def update_output_div2(table, feature):
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

# <editor-fold desc="section 3; continous x,y,z">
# callback update options of x1 dropdown
@app.callback(Output(_3_dropdown_x, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded

    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of y1 dropdown
@app.callback(Output(_3_dropdown_y, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of continous z1 dropdown
@app.callback(Output(_3_dropdown_z, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


@app.callback(
    Output(component_id=_3_graph, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_3_dropdown_x, 'value'),
     Input(_3_dropdown_y, 'value'),
     Input(_3_dropdown_z, 'value'),
     Input(_3_dropdown_x_type, 'value'),
     Input(_3_dropdown_y_type, 'value')
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


# <editor-fold desc="section 4; Discerete x,y,z"">
# callback update options of x2 dropdown
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
                name=class_
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


# <editor-fold desc="section 5; x,y, multi y continous">
@app.callback(Output(_5_dropdown_x, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded

    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


@app.callback(Output(_5_dropdown_multi_y, 'options'),
              [Input(_0_table, 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


@app.callback(
    Output(component_id=_5_graph, component_property='figure'),
    [Input(_0_table, 'rows'),
     Input(_5_dropdown_x, 'value'),
     Input(_5_dropdown_multi_y, 'value'),
     Input(_5_dropdown_x_type, 'value'),
     Input(_5_dropdown_y_type, 'value')
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

# </editor-fold>



app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)

