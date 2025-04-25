import pandas as pd
import streamlit as st
import altair as alt

@st.cache_data(show_spinner="Loading data...")
def load_data():
    df = pd.read_csv("project_activities.csv")
    return df

df = load_data()

st.title("📌 Project Progress Tracker")

# Filter section
st.subheader("🔍 Optional Filter")
columns = df.columns.tolist()
selected_column = st.selectbox("Filter by column (optional)", [""] + columns)

filtered_df = df.copy()
if selected_column:
    unique_values = df[selected_column].dropna().unique()
    selected_value = st.selectbox(f"Select value for '{selected_column}'", [""] + sorted(unique_values.astype(str).tolist()))
    if selected_value:
        filtered_df = df[df[selected_column].astype(str) == selected_value]

# 🟦 Activity Type vs Status
st.subheader("📊 Status per Activity Type")

top_chart_data = (
    filtered_df.groupby(["Activity Type", "Status"])
    .size()
    .reset_index(name="Count")
)

chart_top = alt.Chart(top_chart_data).mark_bar().encode(
    x=alt.X('Activity Type:N', title="Activity Type"),
    y=alt.Y('Count:Q', title="Count"),
    color='Status:N',
    tooltip=['Activity Type', 'Status', 'Count']
).properties(width=700, height=400)

st.altair_chart(chart_top, use_container_width=True)

# Two columns for additional visualizations
col1, col2 = st.columns(2)

# 🥧 Done vs Not Done
with col1:
    st.markdown("### 🥧 Overall Status Breakdown")

    status_counts = filtered_df["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]

    pie_chart = alt.Chart(status_counts).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="Count", type="quantitative"),
        color=alt.Color(field="Status", type="nominal"),
        tooltip=["Status:N", "Count:Q"]
    ).properties(width=300, height=300)

    st.altair_chart(pie_chart, use_container_width=True)

# 🚨 Projects with most 'Not Done'
with col2:
    st.markdown("### 🚨 Projects with Most 'Not Done' Activities")

    not_done_data = (
        filtered_df[filtered_df["Status"] == "Not Done"]
        .groupby("Project Name")
        .size()
        .reset_index(name="Not Done Count")
        .sort_values(by="Not Done Count", ascending=False)
        .head(10)
    )

    bar_not_done = alt.Chart(not_done_data).mark_bar().encode(
        x=alt.X("Not Done Count:Q", title="Count"),
        y=alt.Y("Project Name:N", sort='-x', title="Project"),
        tooltip=["Project Name", "Not Done Count"]
    ).properties(width=300, height=300)

    st.altair_chart(bar_not_done, use_container_width=True)
