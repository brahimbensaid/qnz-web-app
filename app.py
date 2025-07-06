from flask import Flask, render_template, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

# Load the Excel file (static path for now)
FILE_PATH = 'static/qnz.xlsx'
df = pd.read_excel(FILE_PATH, sheet_name=0, header=5)

# Clean columns: remove unnamed and keep only useful ones
df = df.loc[:, ~df.columns.str.contains('^Unnamed', na=False)]

@app.route('/')
def index():
    data = df.to_dict(orient='records')
    columns = df.columns.tolist()
    return render_template('index.html', data=data, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)
