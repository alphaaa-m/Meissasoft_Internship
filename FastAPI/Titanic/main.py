from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
import plotly.express as px
from plotly.io import to_html

# Load the Titanic dataset
df = sns.load_dataset('titanic')
survival_rate = df.groupby("class")["survived"].mean().reset_index()

# create FastAPI app
app = FastAPI(title='Titanic API')

@app.get("/")
async def root():
    return {"message": "Titanic API"}

@app.get("/survival_rate")
async def get_survival_rate():
    return survival_rate.to_dict(orient="records")

@app.get("/survival_rate_static_plot", response_class=HTMLResponse)
async def show_plot1():
# Create plot
    plt.figure(figsize=(6, 4))
    sns.barplot(x="class", y="survived", data=df)
    plt.title("Survival Rate by Class and Gender")
    plt.xlabel("Passenger Class")
    plt.ylabel("Survival Rate")
    plt.tight_layout()

    #convert plot to base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    # Return as an HTMLResponse with embedded image
    return HTMLResponse(content=f'<img src="data:image/png;base64,{image_base64}">')

@app.get("/survival_rate_interactive_plot", response_class=HTMLResponse)
async def show_plot2():
# Create an interactive bar plot with Plotly
    fig = px.bar(df, x='class', y='survived',color='sex' ,title='Survival Rate by Class with Plotly')

    # Convert the plot to HTML string
    plot_div = to_html(fig, full_html=False)

    # Return HTML page
    html_content = f"""
    <html>
        <head><title>Survival Rate (Plotly)</title></head>
        <body>
            <h2>Interactive Plot</h2>
            {plot_div}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
