import streamlit as st 
st.title('ai Web Scrapper ')
url=st.text_input("Enter your website url:") #text input field 

if st.button("scrape site"):
    st.write('scraping the website')

