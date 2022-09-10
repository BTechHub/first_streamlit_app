import streamlit as st
import pandas

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list=my_fruit_list.set_index("Fruit")
my_fruit_selected=st.multiselect("pick some fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_selected.loc[my_fruit_selected]



st.dataframe(fruits_to_show)
