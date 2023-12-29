# =========================================================================================================

# Emojis list: https://es.piliapp.com/emoji/list/ , https://emojipedia.org/objects

# Libraries

import streamlit as st
from streamlit_timeline import timeline
from constant import *

# Set page

st.set_page_config(page_title='Edwar Valenzuela Cortés CV',layout="wide",page_icon='🚀', )

# =========================================================================================================

# Sidebar

st.sidebar.image("Pedwar/profilepic.jpg")
st.sidebar.title("Business management student with a focus on data science")

st.sidebar.subheader("Contact data", divider="gray")
st.sidebar.write("📱  3146264885")
st.sidebar.write("📧 evalenzuelac@unal.edu.co")
st.sidebar.write("📍  Bogotá D.C")
st.sidebar.write("🔗 LinkedIn: www.linkedin.com/in/edwar-valenzuela")
st.sidebar.write("⚙️ Github: https://github.com/EdwarValDS")
st.sidebar.write("🗠 Tradingview profile: https://es.tradingview.com/u/StrategiesForEveryone/#published-scripts")

st.sidebar.subheader("Skills", divider="gray")
st.sidebar.write("✔️ Analytical and problem solving skills")
st.sidebar.write("✔️ Leadership and teamwork")
st.sidebar.write("✔️ Attention to detail")
st.sidebar.write("✔️ Assertive communication")

st.sidebar.subheader("Languages", divider="gray")
st.sidebar.write("✔️ English B2")
st.sidebar.write("✔️ Native Spanish")

st.sidebar.subheader("Reference", divider="gray")
st.sidebar.write("Carlos Osorio Ramírez")
st.sidebar.write("Professor and researcher at the National University of Colombia")
st.sidebar.write("📱  3002095239")

# =========================================================================================================

# Main page
st.title("Hello!, my name is Edwar Valenzuela Cortés. In this page you will know about my career and projects")
st.subheader("About me")
st.subheader("""Business management student passionate about data sciences and its strategic application in the business and economic world. With a strong management background and deep understanding of data science, I offer a unique combination of skills that drive data decision-making and data management.""")

# Timeline
st.subheader("My career", divider="gray")
with st.spinner(text="Building timeline"):
    with open('Pedwar/timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)


# Projects
st.subheader("Main projects", divider="gray")
c1, c2 = st.columns(2)

with c1:
    st.header("Viability of investment in Colombian sovereign bonds 2023")
    st.write("Since 2020, Colombia has faced economic challenges leading to increased inflation and interest rates. Consequently, Colombia's Public Debt Securities (TES) prices have decreased, making the fixed income market noteworthy. An assessment of investing in these debt instruments involves yield curve analysis, algorithmic trading techniques, and fundamental/technical analysis of the local fixed income market, along with temporal analysis for comparing the current situation with historical periods to determine investment viability in Colombian sovereign bonds.")
    st.image("Pedwar/bonossoberanos.jpg")
    st.write("Project link: https://github.com/EdwarValDS/Investment-viability-in-Colombian-sovereign-bonds")

with c2:
    st.header("Estimating food demand at the National University of Colombia")
    st.write("Determining food quantities in any restaurant significantly impacts profitability and operations. This report emphasizes the use of Machine Learning for decision-making regarding lunch demand at the National University of Colombia. It covers key project steps, including data preparation, analysis, predictive model development and evaluation, and final considerations. The goal is to provide utility in effectively managing restaurant quantities in the future, starting with the upcoming semester 2023-2.")
    st.image("Pedwar/restaurants.jpg")
    st.write("Project link: https://github.com/EdwarValDS/Estimating-food-demand-at-the-National-University-of-Colombia")

c3, c4 = st.columns(2)
with c3:
    st.header("Lorentzian Classification Strategy")
    st.write("This strategy, based on the Machine Learning model Lorentzian Classification by @jdehorty, aims to identify trending moves and provide favorable market entries. Backtested on US500 1H (July 19, 2022, to April 14, 2023, with 0.03% commissions), the strategy uses indicators such as 200 Ema, Supertrend, and Atr stop loss. Long and short signals are determined based on specific conditions, with risk management calculated using a percentage of the account. The script includes functions for backtesting with added or withdrawn money. It has shown success in various assets like BTCUSD, ETHUSD, BNBUSD, SPX, and BANKNIFTY. Users are advised to apply caution, use correct risk management, and consider changing parameters for backtesting. The strategy may have more losses than wins in trending markets, requiring patience and consistency.")
    st.image("Pedwar/lorentzian.jpg")
    st.write("Project link: https://es.tradingview.com/script/SfyBCHIJ/")

with c4:
    st.header("Apple Stock price weekly prediction model")
    st.write("News headlines about Apple Stock from Marketwatch page are useful for making weekly predictions. This project deals with extracting data from this website and processing the textual information with spacy through vectors as well as testing different classification models to predict whether the price of the asset will rise or fall weekly. The best model turns out to be the GradientBoostingClassifier, with a total precision of 60%, 55% for predicting drops and 63% for rises. ")
    st.image("Pedwar/apple.jpg")
    st.write("Project link: https://github.com/EdwarValDS/Apple-Stock-price-weekly-prediction-model")



# Knowledge
st.subheader("Knowledge", divider="gray")
def skill_tab():
    rows,cols = len(info['skills'])//4,4
    skills = iter(info['skills'])
    if len(info['skills'])%4!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(4)
        for index_ in range(4):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()

# Education 
st.subheader("Education", divider="gray")

st.write("🎓 Business Management. Feb 2021 - present")
st.write("At National University of Colombia: Sixth semester")

st.write("📈 Introduction to Algorithmic Trading.")
st.write("University of Andes Course: Knowledge about development of computational models for making investment decisions in financial markets")

st.write("📊 Statistical R")
st.write("Economic Sciences Informatics Unit Course: Knowledge of using statistics for data science and analytics problems")

st.write("🧾 Company valuation")
st.write("Economic Sciences Analysis Unit Course: Knowledge about fundamental analysis applied to companies for making long-term investment decisions")

st.write("🤖 Fundamentals of natural language processing")
st.write("Platzi Course: Knowledge about fundamental concepts in natural language processing")

st.write("🤖 Text classification algorithms")
st.write("Platzi Course: Knowledge about the use of text data for classification problems")

st.write("📊 International financial market")
st.write("Economic Sciences Analysis Unit Course: knowledge about the different international markets, assets and market participants")

st.write("📊 Professional machine learning")
st.write("Platzi Course: knowledge about different machine learning algorithms and the way to solve different types of problems")

# Certificates
st.subheader("Certificates")
a1, a2, a3, a4, a5, a6, a7 = st.columns(7)
with a1:
    st.image("Pedwar/algotrading.jpg")
with a2:
    st.image("Pedwar/statR.jpg")
with a3:
    st.image("Pedwar/valempresas.jpg")
with a4:
    st.image("Pedwar/nlpfundamentals.jpg")
with a5:
    st.image("Pedwar/textclassificationalgorithms.jpg")
with a6:
    st.image("Pedwar/internationalmarket.jpg")
with a7:
    st.image("Pedwar/professionalml.jpg")