import streamlit as st
import pandas as pd

# Load CSS file
def load_css(file):
    with open(file, 'r',encoding='utf-8') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Load HTML file
def load_html(file):
    with open(file, 'r',encoding='utf-8') as f:
        html = f.read()
    st.markdown(html, unsafe_allow_html=True)

load_css('style.css')
load_html('index.html')

url = "https://drive.google.com/uc?export=download&id=1CUdTboaKiqRFQT5inZvLRguUIzr0pVKK"
p = pd.read_csv(url, low_memory=False)

# Score function
def score_row(row):
    count = 0
    if pd.notna(row['moid_ld']):
        if row['moid_ld'] < 0.05:
            count += 50
        elif row['moid_ld'] < 0.1:
            count += 30
        elif row['moid_ld'] < 0.3:
            count += 10
    if pd.notna(row['moid_ld']) and pd.notna(row['diameter']) and row['moid_ld'] < 0.3:
        if row['diameter'] > 1:
            count += 40
        elif row['diameter'] > 0.14:
            count += 20
    if row['neo'] == 'Y':
        count += 20
    if row['pha'] == 'Y':
        count += 30
    return count

# Load and score data
@st.cache_data
def load_data():
    p = pd.read_csv('d.csv', low_memory=False)
    p['score'] = p.apply(score_row, axis=1)
    p = p.sort_values('score', ascending=False)
    return p

p = load_data()

# Display
st.subheader("🚨 Top 10 Most Dangerous Asteroids")
c = p[['full_name', 'moid_ld', 'diameter', 'neo', 'pha', 'score']].head(10)
st.dataframe(c)
