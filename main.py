from nicegui import ui
import pandas as pd
import os
import plotly.express as px

from utils.parse_csv import parse_csv
from components.chart_viewer import ChartViewer

UPLOAD_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# State holder for the uploaded DataFrame
df_state = {'df': None}


def handle_upload(file):
    file_path = os.path.join(UPLOAD_FOLDER, file.name)
    with open(file_path, 'wb') as f:
        f.write(file.content.read())  # Save uploaded file
    df = parse_csv(file_path)
    if df is not None:
        df_state['df'] = df
        show_preview(df)
    else:
        ui.notify('❌ Failed to read CSV: invalid format or corrupted file.', color='negative')


def show_preview(df: pd.DataFrame):
    ui.label('✅ File uploaded successfully!')
    ui.table(
        columns=[{'name': col, 'label': col, 'field': col} for col in df.columns],
        rows=df.to_dict("records"),
        row_key="index"
    )
    if len(df.columns) >= 2:
        ChartViewer(df)

ui.dark_mode()

with ui.column().classes('w-full items-center gap-4'):
    ui.label("📊 DataVizApp").classes('text-2xl font-bold text-blue-600')
    ui.label("Upload a CSV file to preview and visualize your data").classes('text-md text-gray-500')

    with ui.card().classes('p-6 w-full max-w-md'):
        ui.upload(on_upload=handle_upload, label="📁 Upload CSV File").classes('w-full')

ui.run(title='DataVizApp')