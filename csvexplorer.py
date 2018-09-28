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

app.layout = html.Div([
    # ----------------------------------------------------upload section
    html.H5("Upload Files"),
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
    html.H5("Updated Table"),
    html.Div(dte.DataTable(rows=[{}], id='table')),
    # ----------------------------------------------------Histogram section
    html.Br(),
    html.H5("Histogram Plot"),
    dcc.Dropdown(id='histogram_dropdown_input',
                 multi=False,
                 placeholder='Select feature'),
    dcc.Graph(id='figure_hist_id_output'),
    # -----------------------------------------------------Plotting section
    html.H5("X Y, Plotting"),

    html.Br(),
    html.Div([
        # -------------------------------x Drop down
        html.Div([
            dcc.Dropdown(
                id='xaxis_id_input1',
            )
        ],
            style={'width': '48%', 'display': 'inline-block'}),
        # -------------------------------y Drop down
        html.Div([
            dcc.Dropdown(
                id='yaxis_id_input2'
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    # -------------------------------Graph section
    dcc.Graph(id='figure_id_output'),
    # -------------------------------------------------------
])
server=app.server

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
@app.callback(Output('histogram_dropdown_input', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty
    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of x dropdown
@app.callback(Output('xaxis_id_input1', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded

    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]


# callback update options of y dropdown
@app.callback(Output('yaxis_id_input2', 'options'),
              [Input('table', 'rows')])
def update_filter_column_options(tablerows):
    dff = pd.DataFrame(tablerows)  # <- problem! dff stays empty even though table was uploaded
    print("updating... dff empty?:", dff.empty)  # result is True, labels stay empty

    return [{'label': i, 'value': i} for i in sorted(list(dff))]




@app.callback(
    Output(component_id='figure_hist_id_output', component_property='figure'),
    [Input('table', 'rows'),
     Input('histogram_dropdown_input', 'value'), ]
)
def update_output_div2(table, feature):
    dff = pd.DataFrame(table)
    data = [go.Histogram(x=dff[feature])]
    figure={
        'data':data,
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
    Output(component_id='figure_id_output', component_property='figure'),
    [Input('table', 'rows'),
     Input('xaxis_id_input1', 'value'),
     Input('yaxis_id_input2', 'value'),  ]
)
def update_output_div2(table, featurex,featurey):
    dff = pd.DataFrame(table)
    trace = go.Scatter(
        x = dff[featurex],
        y = dff[featurey],
        mode = 'markers',

    )
    data = [trace]
    figure={
        'data':data,
        'layout': {
            'title': 'Dash Data Visualization'
            # ,'barmode':'stack'
            , 'xaxis': dict(
                title=featurex,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
            , 'yaxis': dict(
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

