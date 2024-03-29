# Concept for a Graphical User Interface for SimCADO

``simcado_gui`` is a concept (not even a prototype) for a graphical user interface for 
[simcado](https://simcado.readthedocs.io/en/latest/index.html). 

At the moment, it is only able to simulate a single source (a star) under different conditions and plot the results. 

To use it you should have SimCADO installed 

``pip install simcado`` 

and [dash](https://dash.plot.ly/)

``pip install dash``

The interface should run in your browser under the address ``http://127.0.0.1:8050/``

![](images/simcado_gui_screenshot.png)





### Features wishlist

* Simulate different sources under different conditions (support adding sources?)
* Support different modes (including the full array)
* Ability to do some analysis on-screen (change scale, select colormaps, etc)
* Ability to download the results as fits file
* Your feature


### Other possibilities

``dash`` is certainly not the only framework to create interfaces with python code. Other possibilities to investigate include:

* [jupyter dashboard](https://jupyter-dashboards-layout.readthedocs.io/en/latest/)
* [nteract](https://nteract.io/)
* [bokeh](https://bokeh.pydata.org/en/latest/)
* others?


 








