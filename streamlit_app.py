import streamlit as st
import pandas

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.multiselect("pick some fruits",list(my_fruit_list.index))

st.dataframe(my_fruit_list)
