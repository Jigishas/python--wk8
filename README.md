# CORD-19 COVID-19 Research Papers Analysis

This project provides an interactive analysis of the CORD-19 (COVID-19 Open Research Dataset) metadata. It includes data exploration scripts, visualizations, and a Streamlit web app for interactive exploration of research papers related to COVID-19.

## Features

- **Data Exploration**: Load and explore the metadata CSV file with publication details.
- **Interactive Visualizations**: 
  - Publications by year
  - Top journals publishing COVID-19 research
  - Word cloud of paper titles
  - Distribution of papers by source
- **Filtering**: Filter data by publication year range.
- **Sample Data Display**: View sample paper details.

## Files

- `metadata.csv`: The CORD-19 metadata dataset containing information about research papers (titles, authors, abstracts, publication dates, etc.).
- `explore_metadata.py`: Python script to load and explore the metadata CSV, displaying shape, sample rows, data types, and missing values.
- `streamlit_app.py`: Streamlit application for interactive data visualization and exploration.
- `cord19_analysis.ipynb`: Jupyter notebook for additional data analysis and exploration.

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3.7+ installed.
3. Install the required dependencies:

   ```
   pip install streamlit pandas matplotlib wordcloud
   ```

## Usage

### Running the Streamlit App

To launch the interactive web app:

```
streamlit run streamlit_app.py
```

This will open a web browser with the app, allowing you to explore the data interactively.

### Exploring Metadata

To run the metadata exploration script:

```
python explore_metadata.py
```

This will print basic statistics about the metadata dataset.

### Jupyter Notebook

Open `cord19_analysis.ipynb` in Jupyter Notebook or JupyterLab for additional analysis and visualizations.

## Data Source

The metadata is from the CORD-19 dataset, which is a collection of research papers related to COVID-19. The dataset includes metadata such as titles, abstracts, authors, publication dates, and sources.

## Requirements

- Python 3.7+
- streamlit
- pandas
- matplotlib
- wordcloud

## Contributing

Feel free to contribute by adding new features, improving visualizations, or enhancing the analysis.

## License

This project is for educational and research purposes. Please refer to the original CORD-19 dataset license for data usage terms.
