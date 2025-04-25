# 📌 Project Progress Tracker

This is a Streamlit-based dashboard application for tracking project progress using activity-level data from a CSV file.

## 📂 Data Format

The app expects a CSV file named `project_activities.csv` with the following columns:

- `Project Name`: Name of the project
- `Status`: Status of the activity (e.g., Done, Not Done)
- `Responsible`: Person or team responsible
- `Folder Name`: Folder or grouping the activity belongs to
- `Activity Name`: Specific task name
- `Activity Type`: Type of activity (e.g., Development, Testing, Review)

## 🚀 Features

- Filter data by any column (e.g., Responsible, Project Name, etc.)
- Visualize the distribution of activity status across different types
- See overall completion via a pie chart
- Identify projects with the most incomplete activities

## 🛠️ How to Run

1. Install dependencies:
    ```bash
    pip install streamlit pandas altair
    ```

2. Place your CSV file in the same folder as `app.py` and name it `project_activities.csv`.

3. Launch the app:
    ```bash
    streamlit run app.py
    ```

## 📊 Sample Output

- Bar chart of activity types vs status
- Pie chart of overall progress
- Top 10 projects with most incomplete activities

---

Made with ❤️ using [Streamlit](https://streamlit.io)
