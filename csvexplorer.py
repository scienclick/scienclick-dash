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

width = '20%'
app.layout = html.Div([
    # ----------------------------------------------------upload section
    html.H5("0. Upload Files"),
    dcc.Upload(
        id='upload-data',
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
    html.Div(dte.DataTable(rows=[{}], id='table')),
    # ----------------------------------------------------Histogram section
    html.Br(),
    html.H5("2. Histogram Plot"),
    html.Div([dcc.Dropdown(id='2_histogram_dropdown_input',
                           multi=False,
                           placeholder='Select feature')],
             style={'width': width, 'display': 'inline-block'}),
    dcc.Graph(id='figure_hist_id_output'),
    # -----------------------------------------------------Plotting section continous
    html.H5("3. X Y, Continous Plotting"),

    html.Br(),
    # ----------------------3- x,y,z
    html.Div([
        # -------------------------------x Drop down
        html.Div([
            dcc.Dropdown(
                id='3_xaxis_id_input1', placeholder='x'
            )
        ],
            style={'width': width, 'display': 'inline-block'}),
        # -------------------------------y Drop down
        html.Div([
            dcc.Dropdown(
                id='3_yaxis_id_input2', placeholder='y'
            )
        ], style={'width': width, 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(
                id='3_zaxis_id_input3', placeholder='Continous z'
            )
        ], style={'width': width, 'display': 'inline-block'})
    ]),
    # ----------------------3- log, Normal
    html.Div([
        # -------------------------------x Drop down
        html.Div([
            dcc.Dropdown(
                id='3_xaxis_Log_input', options=[{'label': 'Automatic', 'value': '-'},
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
                id='3_yaxis_Log_input', options=[{'label': 'Automatic', 'value': '-'},
                    {'label': 'Linear', 'value': 'linear'},
                    {'label': 'Log', 'value': 'log'},
                    {'label': 'Date', 'value': 'date'},
                    {'label': 'Catagory', 'value': 'category'},
                ], value="-"
            )
        ], style={'width': width, 'display': 'inline-block'}),

    ]),
    # -------------------------------Graph section
    dcc.Graph(id='3_figure_id_output'),
    # -------------------------------------------------------
    # -----------------------------------------------------Plotting section Discerete
    html.H5("4. X Y, Discrete Plotting"),

    html.Br(),
    # ----------------------4- x,y,z
    html.Div([
        # -------------------------------x Drop down
        html.Div([
            dcc.Dropdown(
                id='4_xaxis_id_input1', placeholder='x'
            )
        ],
            style={'width': width, 'display': 'inline-block'}),
        # -------------------------------y Drop down
        html.Div([
            dcc.Dropdown(
                id='4_yaxis_id_input2', placeholder='y'
            )
        ], style={'width': width, 'display': 'inline-block'}),
        html.Div([
            dcc.Dropdown(
                id='4_zaxis_id_input3', placeholder='Discrete z'
            )
        ], style={'width': width, 'display': 'inline-block'})
    ]),
    # ----------------------4- log, Normal
    html.Div([
        # -------------------------------x Drop down
        html.Div([
            dcc.Dropdown(
                id='4_xaxis_Log_input', options=[{'label': 'Automatic', 'value': '-'},
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
                id='4_yaxis_Log_input', options=[
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
    dcc.Graph(id='4_figure_id_output'),
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
@app.callback(Output('table', 'rows'),
              [Input('upload-data', 'contents'),
               Input('upload-data', 'filename')])
def update_output(contents, filename):
    if contents is not None:
        df = parse_contents(contents, filename)
        if df is not None:
            return df.to_dict('records')
        else:
            return [{}]
    else:
        return [{}]


# callback update options of histogram dropdown
@app.callback(Output('2_histogram_dropdown_input', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of x1 dropdown
@app.callback(Output('3_xaxis_id_input1', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded

    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of x2 dropdown
@app.callback(Output('4_xaxis_id_input1', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded

    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of y1 dropdown
@app.callback(Output('3_yaxis_id_input2', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of y1 dropdown
@app.callback(Output('4_yaxis_id_input2', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of continous z1 dropdown
@app.callback(Output('3_zaxis_id_input3', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


@app.callback(Output('4_zaxis_id_input3', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# plotting Histogram
@app.callback(
    Output(component_id='figure_hist_id_output', component_property='figure'),
    [Input('table', 'rows'),
     Input('2_histogram_dropdown_input', 'value'), ]
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


@app.callback(
    Output(component_id='3_figure_id_output', component_property='figure'),
    [Input('table', 'rows'),
     Input('3_xaxis_id_input1', 'value'),
     Input('3_yaxis_id_input2', 'value'),
     Input('3_zaxis_id_input3', 'value'),
     Input('3_xaxis_Log_input', 'value'),
     Input('3_yaxis_Log_input', 'value')
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
            mode='markers' )
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


@app.callback(
    Output(component_id='4_figure_id_output', component_property='figure'),
    [Input('table', 'rows'),
     Input('4_xaxis_id_input1', 'value'),
     Input('4_yaxis_id_input2', 'value'),
     Input('4_zaxis_id_input3', 'value'),
     Input('4_xaxis_Log_input', 'value'),
     Input('4_yaxis_Log_input', 'value')
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


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)

