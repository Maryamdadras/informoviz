# InforMoViz

***Infor***mation of ***Mo***vies ***Vis***ualisation project based on personal Letterboxd data.
This project is a data visualization portfolio piece that explores my personal movie watching, rating, and review patterns collected from Letterboxd. It features multiple charts that tells a story about how I engage with films.

---

## 📁 Key Project Files

* **`Main Review Habit.html`**: The final, interactive dual-axis visualization. You can open this file in any web browser to hover over the data and explore the review patterns.
* **`main_cleaned.csv`**: The complete, cleaned dataset used for this analysis, featuring the combined Letterboxd diary entries, reviews, and the enriched TMDB API metadata (Genres and Countries).
* **`informoviz.ipynb`**: The main Jupyter Notebook containing the entire data pipeline, from the initial data merging and API enrichment to the final interactive visualizations.

---

## 📊 Overview of The Project

For this project, I analyzed my personal data from Letterboxd, which is a social platform for film lovers and I started using it from 2020 actively. The platform allows users to log the movies they watch in a "diary," rate them on a 0.5 to 5.0 star scale, and write written reviews. My raw data export initially consisted of two separate, basic CSV files. The first was my diary log, which tracked basic attributes (Watched Date, Name, Year, and Rating). The second was a reviews file, which contained similar metadata but included the actual Review text.

To create a comprehensive dataset, I first merged these two files based on their common columns. However, to enable a much deeper visual analysis of my habits, I needed more context. I used the TMDB API to enrich the dataset, fetching missing metadata for every single movie and adding two crucial new columns to my final CSV: Genre and Country.

When I exported my data, I realized I did not remember much about the reviews I had written. I have a personal theory about my reviewing habits: I only leave a review when a movie provokes a strong reaction. Also on the other hand, when I truly love a movie and give it a high rating, the score speaks for itself and there is no need for a written review. I wanted to use Data Sense-Making to test this theory and uncover the hidden patterns in my viewing and reviewing habits.

I started by exploring the broader context of my data mapping out my most-watched genres and seasonal viewing habits. Through an iterative design process and by analyzing the results through trials, I learned to avoid visual clutter, and trying for cleaner visuals like Treemaps and Calendar Heatmaps to make my viewing patterns easily readable.

When I finally moved to analyzing my reviews, I was curious about the relationship between the star rating, the total number of reviews, and the character count. During my first visualization attempt, I noticed a massive outlier, which was a quoted review for the movie "Hello FatherDog" that I hadn't originally written and it was basically a copy-pasted review. As I wanted my analysis to be only a representation of my own writing, I made the decision to clean the data and eliminate this anomaly.

By putting both "average character count" and "total number of reviews" on the same scale, I created a dual-axis chart. As a design decision, I chose a Purple-Green contrast palette (#af8dc3 and #7fbf7b). Because these variables measure two entirely different things, using distinct, contrasting hues ensures they remain visually separated. Furthermore, Purple/Green is a colorblind-safe combination, ensuring the visualization remains accessible while allowing the line trend to preattentively "pop out" against the softer bars.

The final chart proved partially my initial theory and gave me more interesting details. It revealed that I write the highest volume of reviews for movies in the "average to high" range (3.0–3.5 stars), while I write very few for highly-rated movies (4.5–5.0 stars). Furthermore, an anomaly appeared at the bottom of the scale that I write significantly more reviews for 0.5-star movies than for those rated 1.0 or 1.5 stars.

This indicates that my motivation to write a review is driven by strong emotions, which is either deep disappointment or a desire to process "average to high" experiences, rather than a linear relationship with the rating. The review lengths also showed interesting facts to make me realize that I write longer texts when I need to justify why a movie was "not quite perfect" (missing out on a 4- or 5-star rating) or to explain exactly why a film was a total failure (the 0.5-star reviews).

While this visualization successfully revealed my reviewing patterns, the dataset has limitations. It lacks the contextual data needed to connect my movie-watching habits with my state of mind or busy life periods (such as immigrating, studying, or working full-time). Additionally, I cannot account for external factors that control my review writing, such as finishing a movie late at night and simply forgetting to log a review. Despite these limitations, this project successfully transformed raw diary entries into a clear reflection of my personal behavior.

---

> **🌐 Want to see the bigger picture?** > If you are interested in a more general overview of my all-time Letterboxd statistics and viewing habits, you can also check out [my general Letterboxd Dashboard Website here](https://maryamdadras.github.io/informoviz/).

---

## 👥 Author

**Maryam Dadrasrazi** - Data Enthusiast | Visual Storyteller | Film Lover

---

## 📄 License

This is a personal project, feel free to fork and use for your own data storytelling projects!
