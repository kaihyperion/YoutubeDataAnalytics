import streamlit as st
import csv
import pandas as pd
import time
import altair as alt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import re


st.title('AMA YouTube Data Extraction')

data_load_state = st.text('Loading data...')
time.sleep(1.5)

#Read the CSV file
df = pd.read_csv('youtubeData.csv')

data_load_state.text('Successfully loaded data!')

# st.subheader('Raw data')
# st.write(df)

video = st.multiselect(
    "Choose video", list(df.columns),['title', 'likes','dislikes', 'publishedDate', 'views', 'comment']
)

if not video:
    st.error("Please select at least one column.")
else:
    data = df[video]
    if 'publishedDate' in video:
        data.sort_values(by=['publishedDate'], inplace=True)
        st.write("### Video Data Frame (sorted by published Date)", data)
    else:
        st.error("Please mark 'publishedDate'")
    

    # Likes Vs Published Date
    if 'likes' in video:
        st.subheader("# of Likes by Video Publish Date")
        likeChart = alt.Chart(data).mark_bar().encode(
            x = 'publishedDate:T',
            y = 'likes:Q'
        )
        st.altair_chart(likeChart, use_container_width=True)

        


    # Dislikes Vs Published Date
    if 'dislikes' in video:
        st.subheader("# of Dislikes by Published Date")
        dislikeChart = alt.Chart(data).mark_bar().encode(
            x = 'publishedDate:T',
            y = 'dislikes:Q'
        )
        st.altair_chart(dislikeChart, use_container_width=True)


    # View count Vs Published Date
    if 'views' in video:
        st.subheader("# of View Count by Published Date")
        viewChart = alt.Chart(data).mark_point().encode(
            x = 'publishedDate:T',
            y = 'views'
        )
        st.altair_chart(viewChart, use_container_width=True)

    # Comment Couunt Vs Published Date
    if 'comment' in video:
        st.subheader("# of Comment Count by Published Date")
        commentChart = alt.Chart(data).mark_point().encode(
            x = 'publishedDate:T',
            y = 'comment'
        )
        st.altair_chart(commentChart, use_container_width=True)
    # tmp = data
    # a = alt.Chart(data).mark_line().encode(
    #     x='publishedDate', y='likes'
    # )
    # st.altair_chart(a)

    # b = alt.Chart(tmp).mark_line().encode(
    #     x='publishedDate', y='dislikes'
    # )
    # st.altair_chart(b)

    # c = alt.Chart(data).mark_line().encode(
    #     x='publishedDate', y='comment'
    # )
    # st.altair_chart(c)
    # d = alt.Chart(data).mark_line().encode(
    #     x='publishedDate', y='views'
    # )
    # st.altair_chart(d)
    # progress_bar = st.sidebar.progress(0)
    # status_text = st.sidebar.empty()
   
    # st.subheader("PublishedDate is set as index")
    # ab=data.set_index('publishedDate')
    # ab


    # st.subheader("This is regular Line Chart")
    # last_rows = ab[['likes', 'dislikes']]
    # st.write("last row")
    # last_rows
    # chart = st.line_chart(last_rows)
    # time.sleep(1)
    

    # st.subheader("This is Ratio of dislike ratio by title")
    # chart = st.area_chart(last_rows)
    # # chart.add_rows(last_rows[-1, :].cumsum(axis=0))
    #sort by publisheddate in ascending order old to new
    
    # for i in range(0, len(data)):

    # data = data.T.reset_index()
    # data = pd.melt(data, id_vars=["index"]).rename(
    #     columns={"index":}
    # )

    # chart = (
    #     alt.Chart(data)
    #     .mark_area(opacity=0.3)
    #     .encode(
    #         x="asdf:T",
    #         y=alt.Y("lflflf:Q", stack=None),
    #         color="Region:N"
    #     )
    # )
    # st.altair_chart(chart, use_container_width=True)


    # st.subheader("View Count Vs Title Length")
    # sortedByView = data.sort_values(by=['likes'])
    # sortedByView = sortedByView.set_index('likes')
    # sortedByView
    # a = sortedByView.index
    # a
    
    # fig = make_subplots(rows = 3, cols=1)
    # fig.add_trace(go.Scatter(
    #     x = a
    # )
