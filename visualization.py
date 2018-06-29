from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
import bokeh.colors


def map_color(min_val, max_val, current_val):
    if current_val < 0:
        redness = float(current_val) / min_val
        return bokeh.colors.HSL(0, 1.0, 1.0-redness/2).to_rgb()
    else:
        blueness = float(current_val) / max_val
        return bokeh.colors.HSL(255,1.0, 1.0-blueness/2).to_rgb()


def barchart(x_axis, y_axis, title="", ouput_file="data.html"):
    output_file(ouput_file)

    data = {'x': x_axis, 'y': y_axis}

    source = ColumnDataSource(data)

    p = figure(x_range=x_axis, plot_height=500, plot_width=800, toolbar_location=None, title=title)

    min_val = min(y_axis)
    max_val = max(y_axis)
    colors = [map_color(min_val, max_val, y) for y in y_axis]

    p.vbar(x='x', top='y', width=0.9, source=source,
           line_color='white', fill_color=factor_cmap('x', palette=colors, factors=x_axis))

    show(p)
