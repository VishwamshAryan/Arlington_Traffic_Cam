# Arlington Traffic Cameras Dashboard
This interactive dashboard visualizes real-time traffic camera data for Arlington, built using the Preswald framework.

# What It Does
* Loads structured traffic camera data from a CSV file
* Cleans and prepares geospatial data (latitude and longitude)
* Displays the full camera dataset in a sortable table
* Renders an interactive **Mapbox map** showing camera locations
* Built using **Preswald's 4-step implementation**:
  1. Load the dataset using `connect()` and `get_df()`
  2. Optional SQL-like filtering with `query()`
  3. Interactive UI components: `text()`, `table()`
  4. Data visualization with `plotly()`

# Dataset

**Source**: `data/Traffic_Cameras.csv`  
**Columns Used**:
* `Camera Site`
* `Camera EncoderB2`
* `Latitude`, `Longitude`
* `port`
* `STATUS`

---

# How to Run

Make sure you have Preswald (https://preswald.com) installed.

```bash
# From the project folder
preswald serve
