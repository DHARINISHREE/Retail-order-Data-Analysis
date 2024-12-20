import streamlit as st
from data_query import *
st.markdown(
    """
    <style>
        .block-container {
            padding-left: 10px;
            padding-right: 10px;
            padding-top: 1.5rem;
            padding-bottom: 1rem;
        }
        .st-emotion-cache-yw8pof{
        max-width: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar menu
st.sidebar.title("Menu")
if st.sidebar.button("Query 1"):
    st.header("Top 10 highest revenue generating products")
    st.table(query1())
if st.sidebar.button("Query 2"):
    st.header("Top 5 cities with the highest profit margins")
    st.table(query2())
if st.sidebar.button("Query 3"):
    st.header("The total discount for each category")
    st.table(query3())
if st.sidebar.button("Query 4"):
    st.header("The average sale price per product category")
    st.table(query4())
if st.sidebar.button("Query 5"):
    st.header("The region with the highest average sale price")
    st.table(query5())
if st.sidebar.button("Query 6"):
    st.header("The total profit per category")
    st.table(query6())
if st.sidebar.button("Query 7"):
    st.header("The top 3 segments with the highest quantity of orders")
    st.table(query7())
if st.sidebar.button("Query 8"):
    st.header("The average discount percentage given per region")
    st.table(query8())
if st.sidebar.button("Query 9"):
    st.header("The product category with the highest total profit")
    st.table(query9())
if st.sidebar.button("Query 10"):
    st.header("The total revenue generated per year")
    st.table(query10())
if st.sidebar.button("Query 11"):
    st.header("The products that generate the highest revenue based on sale prices")
    st.table(query11())
if st.sidebar.button("Query 12"):
    st.header("Compare year-over-year sales to identify growth or decline in certain months")
    st.table(query12())
if st.sidebar.button("Query 13"):
    st.header(" Use functions like GROUP BY, HAVING, ROW_NUMBER(), and CASE WHEN to categorize and rank products by their revenue, profit margin, etc")
    st.table(query13())
if st.sidebar.button("Query 14"):
    st.header("Query sales data by region to identify which areas are performing best")
    st.table(query14())
if st.sidebar.button("Query 15"):
    st.header("Identify products with discounts greater than 20% and calculate the impact of discounts on sales")
    st.table(query15())

# My Query
if st.sidebar.button("My Query 1"):
    st.header("Top 5 revenue generating product")
    st.table(myquery1())
if st.sidebar.button("My Query 2"):
    st.header("Top 10 revenue generating products by region")
    st.table(myquery2())
if st.sidebar.button("My Query 3"):
    st.header("Total sales by month and year")
    st.table(myquery3())
if st.sidebar.button("My Query 4"):
    st.header("The highest revenue generating category in month wise")
    st.table(myquery4())
if st.sidebar.button("My Query 5"):
    st.header("Highest selling product in each year")
    st.table(myquery5())
if st.sidebar.button("My Query 6"):
    st.header("Highest sales month for each categories")
    st.table(myquery6())
if st.sidebar.button("My Query 7"):
    st.header("Total discount per year.")
    st.table(myquery7())
if st.sidebar.button("My Query 8"):
    st.header("Total Profit Margin in Country Wise.")
    st.table(myquery8())
if st.sidebar.button("My Query 9"):
    st.header("Total Cost Price in State Wise.")
    st.table(myquery9())
if st.sidebar.button("My Query 10"):
    st.header("Top 10 Revenue in Postel Code Wise")
    st.table(myquery10())












