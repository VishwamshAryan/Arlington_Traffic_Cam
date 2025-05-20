# Step 1: Load the dataset
from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()
df = get_df("Traffic_Cameras")

# Drop extra/empty column and rows with missing coordinates
if "column6" in df.columns:
    df = df.drop(columns=["column6"])
df = df.dropna(subset=["Latitude", "Longitude"])
df["Latitude"] = df["Latitude"].astype(float)
df["Longitude"] = df["Longitude"].astype(float)

# Step 2: Query or manipulate the data
# (No filtering — showing full dataset for now)

# Step 3: Build interactive UI
text("# Arlington Traffic Cameras Dashboard")
text("This dashboard shows all available traffic camera data.")
table(df, title="All Traffic Cameras")

# Step 4: Create a visualization
fig = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    hover_name="Camera EncoderB2",
    hover_data=["Camera Site", "STATUS", "port"],
    color="STATUS",
    zoom=11,
    height=500
)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

plotly(fig)
