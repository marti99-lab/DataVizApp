from nicegui import ui
import pandas as pd
import plotly.express as px
from typing import Callable

def ChartViewer(df: pd.DataFrame, on_rendered: Callable = None) -> None:
    """
    Renders UI controls for chart selection and displays the chart.
    """
    x_axis = ui.select(df.columns.tolist(), label='X-Axis')
    y_axis = ui.select(df.columns.tolist(), label='Y-Axis')
    chart_type = ui.select(['Bar', 'Line', 'Pie'], label='Chart Type')

    def on_render():
        if not x_axis.value or not y_axis.value or not chart_type.value:
            ui.notify("Please select all options before rendering.", color="warning")
            return
        _render(df, x_axis.value, y_axis.value, chart_type.value, on_rendered)

    ui.button('Render Chart', on_click=on_render)


def _render(df: pd.DataFrame, x: str, y: str, chart: str, callback: Callable):
    try:
        if chart == 'Bar':
            fig = px.bar(df, x=x, y=y)
        elif chart == 'Line':
            fig = px.line(df, x=x, y=y)
        elif chart == 'Pie':
            fig = px.pie(df, names=x, values=y)
        else:
            ui.notify('Unknown chart type.', color='warning')
            return
        ui.plotly(fig)
        if callback:
            callback()
    except Exception as e:
        ui.notify(f'Failed to render chart: {e}', color='negative')


