# InforMoViz
Information Visualisation project based on my personal letterboxd data. 

**An Interactive Visualization of My Movie Review Habits**

This project is a data visualization portfolio piece that explores my personal movie rating and review patterns collected from Letterboxd. It features a dynamic, interactive chart built with Plotly that tells a story about how I engage with films across different rating scales.

## 📊 Project Overview

The central element of this project is an interactive visualization that combines **bar charts** and **scatter plots** to answer key questions about my reviewing habits.

### Key Insights from the Visualization:

- **Review Length vs. Rating:** The visualization clearly shows how the average length of my reviews changes depending on the star rating given.
- **Volume by Rating:** It displays the total number of reviews for each rating category, highlighting which rating levels I use most frequently.
- **Data-Driven Narrative:** By plotting both the average length and the total count on the same chart, the visualization reveals patterns such as whether I tend to write longer reviews for movies I rate highly or poorly.

## ⚙️ Technical Details

### Technology Stack:
- **Python 3.12**
- **Pandas**: For data manipulation and aggregation.
- **Plotly**: For interactive visualization.
- **Jupyter Notebook**: For code development and display.

### Dataset:
- The project uses a CSV dataset `main_enriched_full.csv` containing my Letterboxd movie review data.
- **Preprocessing Steps:**
  - Removal of the "Hello FatherDog" test entry.
  - Filtering to include only reviews with actual written content (non-null and non-empty).
  - Calculation of review length (character count) for each review.
  - Grouping data by rating to calculate averages and counts.

### Visualization Features:

- **Dual-Axis Chart**: Uses both bars (for average length) and a line (for total count) to provide multiple perspectives.
- **Interactive Hover Effects**: Hovering over data points displays detailed information.
- **Responsive Design**: The chart is designed to adapt to different screen sizes (optimized for web viewing).
- **Complete HTML Export**: The visualization is saved as a standalone HTML file (`My Review Habits.html`) that can be opened in any web browser.

## 🚀 How to Run the Code

1.  **Clone or Download** the repository.
2.  **Install Dependencies**:
    ```bash
    pip install pandas plotly jupyter
    ```
3.  **Open Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```
4.  **Run the Cells** in the `informoviz.ipynb` notebook.
    - Ensure the `Dataset/main_enriched_full.csv` file is present in the same directory.
    - The notebook will execute the data processing and generate the interactive chart.

5.  **View the Output**: The chart will display in the notebook, and the final visualization will be saved as `My Review Habits.html` in the project folder.

## 📁 Project Structure

```
InforMoViz/
├── Dataset/                # Contains the raw data
│   └── main_enriched_full.csv
├── informoviz.ipynb        # Jupyter Notebook with code and visualization
├── My Review Habits.html   # Generated interactive HTML file
└── README.md               # This file
```

## 👥 Author

**Maryam Dadrasrazi** - Data Enthusiast | Visual Storyteller | Film Lover

## 📄 License

This is a personal project, feel free to fork and use for your own data storytelling projects!
