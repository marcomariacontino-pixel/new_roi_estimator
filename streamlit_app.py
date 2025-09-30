import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Page configuration
st.set_page_config(page_title="ROI Predictor", page_icon="🔮", layout="centered")

# Custom CSS for purple tones
st.markdown(
    """
    <style>
    .reportview-container .main .block-container{padding-top:2rem; padding-bottom:2rem;}
    .big-font {
        font-size:32px !important;
        color: #4B0082; /* Indigo/Purple tone */
        text-align: center;
    }
    .accenture-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Show logo if available
try:
    st.image("accenture_logo.png", width=200, use_column_width=False)
except Exception as e:
    # If logo missing, ignore.
    st.write("")

# Title
st.markdown("<h1 class='big-font'>Predictor del ROI per Progetti AI</h1>", unsafe_allow_html=True)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("progetti_ai.csv")
    return df

df = load_data()

# Let user adjust model complexity and other parameters (optional) or fixed model

# Feature and target selection
X = df[["Investimenti", "Durata", "Complessita", "Impatto"]]
y = df["ROI"]

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Sidebar for input parameters
st.sidebar.header("Parametri del Progetto")
investimenti = st.sidebar.slider("Investimenti (milioni EUR)", float(X["Investimenti"].min()), float(X["Investimenti"].max()), float(X["Investimenti"].mean()))
durata = st.sidebar.slider("Durata (mesi)", float(X["Durata"].min()), float(X["Durata"].max()), float(X["Durata"].mean()))
compl = st.sidebar.slider("Complessità Tecnica", float(X["Complessita"].min()), float(X["Complessita"].max()), float(X["Complessita"].mean()))
impatto = st.sidebar.slider("Impatto Potenziale", float(X["Impatto"].min()), float(X["Impatto"].max()), float(X["Impatto"].mean()))

# Make prediction
input_features = np.array([[investimenti, durata, compl, impatto]])
pred = model.predict(input_features)[0]

# Display prediction
st.subheader("Predizione del ROI")
st.write(f"Il ROI previsto è di **{pred:.2f}** milioni di EUR")

# Feature importance explanation
importances = model.feature_importances_
feat_names = ["Investimenti", "Durata", "Complessita", "Impatto"]
importance_df = pd.DataFrame({"Caratteristica": feat_names, "Importanza": importances})
importance_df = importance_df.sort_values(by="Importanza", ascending=True)

st.subheader("Fattori Che Influenzano la Predizione")
st.bar_chart(data=importance_df.set_index("Caratteristica"))

# Explanatory text: list in order
st.markdown("""
La predizione del modello è influenzata dai seguenti fattori, elencati dal più importante al meno importante:
""")
for idx in importance_df.sort_values(by="Importanza", ascending=False).index:
    name = importance_df.loc[idx, "Caratteristica"]
    val = importance_df.loc[idx, "Importanza"]
    st.write(f"- **{name}**: {val:.2%}")
