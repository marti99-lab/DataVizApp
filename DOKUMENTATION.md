# Dataviz App Plan

## Goal
Create a modern, fully Python-based web application where users can either manually enter data or upload a CSV file. The data will then be visualized using different types of charts (e.g., bar, line, pie), with the ability to select axes and chart types.

---

## Technology: NiceGUI
- Pure Python frontend framework
- Supports component-based UI (buttons, dropdowns, tables, uploads)
- Integrates with Plotly / ECharts / Matplotlib for visualizations

---

## Project Structure (initial layout)

dataviz_app/
├── main.py              # Main logic to run the NiceGUI app
├── data/                # Stored uploaded CSV files
├── README.md            # Instructions for setting up and running the app
├── DOKUMENTATION.md     # Step-by-step development log
├── components/          # Custom UI components (e.g., ChartViewer, CSVUploader)
└── utils/parse_csv.py   # Helper functions for parsing and validating CSV files

---

## Planned UI Features
- 📁 Upload a CSV file (which will be saved and parsed)
- ✍️ Manual data input via form (optional in later stages)
- 🔽 Dropdowns for selecting X and Y axes from available columns
- 📊 Chart type selection: bar, line, pie
- 📈 Live chart rendering
- 💾 Save uploaded files in the `data/` folder for future use

---

## Next Steps
1. Create the local folder structure
2. Implement `main.py` with a basic NiceGUI app setup
3. Integrate file upload and preview the chart