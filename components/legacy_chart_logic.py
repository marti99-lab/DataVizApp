from nicegui import ui
import pandas as pd
import plotly.express as px

def show_chart_controls(df: pd.DataFrame):
    with ui.row():
        x_axis = ui.select(df.columns.tolist(), label='X-Axis')
        y_axis = ui.select(df.columns.tolist(), label='Y-Axis')
        chart_type = ui.select(['Bar', 'Line', 'Pie'], label='Chart Type')
        ui.button('Render Chart', on_click=lambda: render_chart(df, x_axis.value, y_axis.value, chart_type.value))


def render_chart(df: pd.DataFrame, x: str, y: str, chart: str):
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
    except Exception as e:
        ui.notify(f'Failed to render chart: {e}', color='negative')