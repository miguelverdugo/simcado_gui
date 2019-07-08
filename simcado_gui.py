#!/usr/bin/env python

"""simcado_gui.py a prototype gui for simcado using plot.ly dash"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go 
import plotly.plotly as py
import numpy as np

import simcado 


#prevconfig='YConfig'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#### Set up the Layout
app.layout = html.Div([
        html.Div(
                children=[html.H6(children='Spectral Type'),
                html.Div(dcc.Dropdown(id='spectype', 
                                      options=[{'label': 'A0I', 'value': 'A0I'},
                                               {'label': 'A0III', 'value': 'A0III'},
                                               {'label': 'A0IV', 'value': 'A0IV'},
                                               {'label': 'A0V', 'value': 'A0V'},
                                               {'label': 'A2I', 'value': 'A2I'},
                                               {'label': 'A2V', 'value': 'A2V'},
                                               {'label': 'A3III', 'value': 'A3III'},
                                               {'label': 'A3V', 'value': 'A3V'},
                                               {'label': 'A4IV', 'value': 'A4IV'},
                                               {'label': 'A5III', 'value': 'A5III'},
                                               {'label': 'A5V', 'value': 'A5V'},
                                               {'label': 'A7III', 'value': 'A7III'},
                                               {'label': 'A7V', 'value': 'A7V'},
                                               {'label': 'B0I', 'value': 'B0I'},
                                               {'label': 'B0V', 'value': 'B0V'},
                                               {'label': 'B1III', 'value': 'B1III'},
                                               {'label': 'B1I', 'value': 'B1I'},
                                               {'label': 'B1V', 'value': 'B1V'},
                                               {'label': 'B2II', 'value': 'B2II'},
                                               {'label': 'B2IV', 'value': 'B2IV'},
                                               {'label': 'B3I', 'value': 'B3I'},
                                               {'label': 'B3III', 'value': 'B3III'},
                                               {'label': 'B3V', 'value': 'B3V'},
                                               {'label': 'B5V', 'value': 'B5V'},
                                               {'label': 'B5I', 'value': 'B5I'},
                                               {'label': 'B5II', 'value': 'B5II'},
                                               {'label': 'B5III', 'value': 'B5III'},
                                               {'label': 'B6IV', 'value': 'B6IV'},
                                               {'label': 'B8I', 'value': 'B8I'},
                                               {'label': 'B8V', 'value': 'B8V'},
                                               {'label': 'B9III', 'value': 'B9III'},
                                               {'label': 'B9V', 'value': 'B9V'},
                                               {'label': 'F0IV', 'value': 'F0IV'},
                                               {'label': 'F0I', 'value': 'F0I'},
                                               {'label': 'F0II', 'value': 'F0II'},
                                               {'label': 'F0III', 'value': 'F0III'},
                                               {'label': 'F0V', 'value': 'F0V'},
                                               {'label': 'F2II', 'value': 'F2II'},
                                               {'label': 'F2III', 'value': 'F2III'},
                                               {'label': 'F2V', 'value': 'F2V'},
                                               {'label': 'F5I', 'value': 'F5I'},
                                               {'label': 'F5III', 'value': 'F5III'},
                                               {'label': 'F5IV', 'value': 'F5IV'},
                                               {'label': 'F5V', 'value': 'F5V'},
                                               {'label': 'F6V', 'value': 'F6V'},
                                               {'label': 'F8I', 'value': 'F8I'},
                                               {'label': 'F8IV', 'value': 'F8IV'},
                                               {'label': 'F8V', 'value': 'F8V'},
                                               {'label': 'G0I', 'value': 'G0I'},
                                               {'label': 'G0III', 'value': 'G0III'},
                                               {'label': 'G0IV', 'value': 'G0IV'},
                                               {'label': 'G0V', 'value': 'G0V'},
                                               {'label': 'G2I', 'value': 'G2I'},
                                               {'label': 'G2IV', 'value': 'G2IV'},
                                               {'label': 'G2V', 'value': 'G2V'},
                                               {'label': 'G5I', 'value': 'G5I'},
                                               {'label': 'G5II', 'value': 'G5II'},
                                               {'label': 'G5III', 'value': 'G5III'},
                                               {'label': 'G5IV', 'value': 'G5IV'},
                                               {'label': 'G5V', 'value': 'G5V'},
                                               {'label': 'G8I', 'value': 'G8I'},
                                               {'label': 'G8III', 'value': 'G8III'},
                                               {'label': 'G8IV', 'value': 'G8IV'},
                                               {'label': 'G8V', 'value': 'G8V'},
                                               {'label': 'K0II', 'value': 'K0II'},
                                               {'label': 'K0III', 'value': 'K0III'},
                                               {'label': 'K0IV', 'value': 'K0IV'},
                                               {'label': 'K0V', 'value': 'K0V'},
                                               {'label': 'K1III', 'value': 'K1III'},
                                               {'label': 'K1IV', 'value': 'K1IV'},
                                               {'label': 'K2I', 'value': 'K2I'},
                                               {'label': 'K2III', 'value': 'K2III'},
                                               {'label': 'K2V', 'value': 'K2V'},
                                               {'label': 'K3II', 'value': 'K3II'},
                                               {'label': 'K3I', 'value': 'K3I'},
                                               {'label': 'K3III', 'value': 'K3III'},
                                               {'label': 'K3IV', 'value': 'K3IV'},
                                               {'label': 'K3V', 'value': 'K3V'},
                                               {'label': 'K4I', 'value': 'K4I'},
                                               {'label': 'K4III', 'value': 'K4III'},
                                               {'label': 'K4V', 'value': 'K4V'},
                                               {'label': 'K5III', 'value': 'K5III'},
                                               {'label': 'K5V', 'value': 'K5V'},
                                               {'label': 'K7V', 'value': 'K7V'},
                                               {'label': 'M0III', 'value': 'M0III'},
                                               {'label': 'M0V', 'value': 'M0V'},
                                               {'label': 'M1III', 'value': 'M1III'},
                                               {'label': 'M1V', 'value': 'M1V'},
                                               {'label': 'M2I', 'value': 'M2I'},
                                               {'label': 'M2III', 'value': 'M2III'},
                                               {'label': 'M2P5V', 'value': 'M2P5V'},
                                               {'label': 'M2V', 'value': 'M2V'},
                                               {'label': 'M3II', 'value': 'M3II'},
                                               {'label': 'M3III', 'value': 'M3III'},
                                               {'label': 'M3V', 'value': 'M3V'},
                                               {'label': 'M4III', 'value': 'M4III'},
                                               {'label': 'M4V', 'value': 'M4V'},
                                               {'label': 'M5III', 'value': 'M5III'},
                                               {'label': 'M5V', 'value': 'M5V'},
                                               {'label': 'M6III', 'value': 'M6III'},
                                               {'label': 'M6V', 'value': 'M6V'},
                                               {'label': 'M7III', 'value': 'M7III'},
                                               {'label': 'M8III', 'value': 'M8III'},
                                               {'label': 'M9III', 'value': 'M9III'},
                                               {'label': 'O5V', 'value': 'O5V'},
                                               {'label': 'O8III', 'value': 'O8III'},
                                               {'label': 'O9V', 'value': 'O9V'}],
                                               value='A0V' )),
                html.H6(children='Source Magnitude'), 
                html.Div(dcc.Input(id='magnitude', type='number', 
                                   value=20, placeholder='Enter object magnitude')) , 
                html.H6(children='Exposure Time (s)'),
                html.Div(dcc.Input(id='exptime', type='number',
                                   value=10,  placeholder='Enter exposure time'))] ,
                style={'width': '40%', 'display': 'inline-block','vertical-align':'top','padding':'20px'}),
# Observation section                                   
        html.Div(                                                 
                children=[html.H6(children='PSF type'),
                html.Div(dcc.RadioItems(id='psf',
                                        options=[ {'label': 'SCAO', 'value': 'PSF_SCAO.fits'},
                                                 {'label': 'MCAO', 'value': 'PSF_MCAO.fits'},
                                                 {'label': 'LTAO', 'value': 'PSF_LTAO.fits'}  ],
                                        value='PSF_SCAO.fits' ) ) ,
                html.H6(children="Mode"),
                html.Div(dcc.RadioItems(id='mode', 
                                        options=[ {'label': 'wide', 'value': 'wide'},
                                                 {'label': 'zoom', 'value': 'zoom'} ],
                                                 value='wide' )),
        html.H6(children="Filter"),
        html.Div(dcc.Dropdown(id='filtername',
                              options=[ {'label': 'J', 'value': 'TC_filter_J.dat'},
                                       {'label': 'H', 'value': 'TC_filter_H.dat'},
                                       {'label': 'Ks', 'value': 'TC_filter_Ks.dat'}],
                                       value='TC_filter_Ks.dat' )),
        html.H6(),
        html.Hr(),
        html.Button('Run the simulation',    id='submit-button', n_clicks=0) ],
        style={'width': '40%', 'display': 'inline-block','vertical-align':'top','padding':'20px'}),
        
#        html.Div(id='output-container-button',
#             children='Enter a value and press submit')
        html.Div( [dcc.Graph(id='observed-image')])
        
        ] )
   
    
# This part should contain the graphics and tools to analyze it like colormaps and scale (log, linear, limtis, etc)
# Also save as fits file





#    html.Div(
#        children=[ html.Div( [ dcc.Graph(id='observed-image') ], 
#                      style={'width': '70%', 'display': 'inline-block','vertical-align':'top'})
#        ],
#    ), ],

#)





# this should get the values
@app.callback(Output('observed-image', 'figure'), 
              [Input('submit-button', 'n_clicks')], 
              [State('spectype', 'value'),
               State('magnitude', 'value'),
               State('exptime', 'value'),
               State('psf', 'value'),
               State('mode', 'value'),
               State('filtername', 'value') ] )
def update_figure(n_clicks, spectype,
                  magnitude,
                  exptime,
                  psf,
                  mode,
                  filtername):
    
    # Creating source
    if n_clicks>0:
        src = simcado.source.star(spectype, mag=magnitude, filter_name=filtername)
    
        hdu = simcado.run(src, detector_layout='small',
                      mode=mode, 
                      INST_FILTER_TC=filtername,
                      OBS_EXPTIME=exptime,
                      SCOPE_PSF_FILE=psf,
                      FPA_LINEARITY_CURVE=None)
        data = np.log10(hdu[0].data)
        zmin = np.log10(np.median(hdu[0].data))
        zmax = np.log10(np.max(hdu[0].data)/10 )
    else:
        data = np.ones(shape=(1024,1024))
        zmin = 1
        zmax = 1
        
    graph = []
    graph.append(go.Heatmap( z=data, colorscale='Viridis', zsmooth="best", zmin=zmin, zmax=zmax,
                            colorbar={"title": "log10(counts)"}))
    dispsize = 400
    
    mylayout = go.Layout(
             width = 800,
             height = 800,
             xaxis = {'title': 'X axis'},
             yaxis = {'title': 'Y axis'})
    
    returned_graph= { 'data': graph, 'layout': mylayout} 
    
    

   
    #returned_graph = py.iplot([graph], filename="figure")
    return returned_graph
    

#### Start the App

if __name__ == '__main__':
    app.run_server(debug=True)

# use import webbrowser to open automatically?





