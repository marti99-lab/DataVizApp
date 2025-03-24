from nicegui import ui
import pandas as pd
import os
import plotly.express as px

UPLOAD_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# State holder for the uploaded DataFrame
df_state = {'df': None}


def handle_upload(file):
    file_path = os.path.join(UPLOAD_FOLDER, file.name)
    file.save(file_path)
    try:
        df = pd.read_csv(file_path)
        df_state['df'] = df
        show_preview(df)
    except Exception as e:
        ui.notify(f'Failed to read CSV: {e}', color='negative')


def show_preview(df: pd.DataFrame):
    ui.label('✅ File uploaded successfully!')
    ui.table(columns=[{'name': col, 'label': col, 'field': col} for col in df.columns], rows=df.to_dict("records"), row_key="index")
    if len(df.columns) >= 2:
        show_chart_controls(df)


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


ui.label("📊 DataVizApp – Upload your CSV to visualize data")
ui.upload(on_upload=handle_upload, label="Upload CSV File")

ui.run(title='DataVizApp')