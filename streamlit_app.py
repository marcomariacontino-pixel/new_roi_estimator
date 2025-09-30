"""
Una semplice applicazione Streamlit per stimare il ROI di un progetto AI marginale.

Questa app legge un piccolo dataset di esempio salvato in `progetti_ai.csv`, addestra un modello
RandomForestRegressor sulla variabile target ROI e permette a un utente di inserire almeno tre
caratteristiche (tra Durata in mesi, Budget in milioni, Dimensione del team, Tecnologia e Settore) per
ottenere una predizione del ROI ed una misura di affidabilità basata sulla varianza delle singole
predizioni degli alberi della foresta.

Per eseguire l'app, installare Streamlit e lanciare da shell:

    streamlit run streamlit_app.py

"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

st.title('Stima del ROI di un progetto AI')

@st.cache(allow_output_mutation=True)
# Carica il dataset
# Questa funzione viene memorizzata nella cache da Streamlit per evitare ricaricamenti ripetuti.
def load_data():
    return pd.read_csv('progetti_ai.csv')

data = load_data()

# Preprocessamento
X = data.drop('ROI', axis=1)
y = data['ROI']
X_enc = pd.get_dummies(X, columns=['Tecnologia', 'Settore'], drop_first=False)
feature_names = X_enc.columns.tolist()

# Training del modello
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_enc, y)

# Funzione di predizione

def predict_roi(new_features: dict):
    if len(new_features) < 3:
        raise ValueError('Devi specificare almeno 3 caratteristiche del progetto.')
    allowed_keys = ['Durata_mesi', 'Budget_ml', 'Team_size','Tecnologia','Settore']
    for k in new_features:
        if k not in allowed_keys:
            raise ValueError(f'Feature {k} non è valida. Scegli tra {allowed_keys}.')
    # Inizializza il campione con le mediane o modali
    sample = {}
    for col in ['Durata_mesi','Budget_ml','Team_size']:
        sample[col] = X[col].median()
    for col in ['Tecnologia','Settore']:
        sample[col] = X[col].mode()[0]
    sample.update(new_features)
    df_sample = pd.DataFrame([sample])
    df_sample_enc = pd.get_dummies(df_sample, columns=['Tecnologia','Settore'], drop_first=False)
    for col in feature_names:
        if col not in df_sample_enc.columns:
            df_sample_enc[col] = 0
    df_sample_enc = df_sample_enc[feature_names]
    preds = np.array([est.predict(df_sample_enc)[0] for est in rf.estimators_])
    mean_pred = preds.mean()
    std_pred = preds.std()
    rel_std_pct = (std_pred / mean_pred * 100) if mean_pred != 0 else float('nan')
    reliability = max(0.0, (1 - rel_std_pct/100)) * 100 if mean_pred != 0 else float('nan')
    return {'ROI_pred': mean_pred, 'Std': std_pred, 'Rel_std_percent': rel_std_pct, 'Reliability_percent': reliability}

# Barra laterale per gli input utente
st.sidebar.header('Inserisci le caratteristiche del progetto')
durata = st.sidebar.number_input('Durata (mesi)', min_value=0, value=0)
budget = st.sidebar.number_input('Budget (Mln euro)', min_value=0.0, value=0.0, format='%0.2f')
team = st.sidebar.number_input('Team size', min_value=0, value=0)
tec_options = [''] + list(data['Tecnologia'].unique())
sett_options = [''] + list(data['Settore'].unique())
tec = st.sidebar.selectbox('Tecnologia', options=tec_options)
sett = st.sidebar.selectbox('Settore', options=sett_options)

features = {}
if durata > 0:
    features['Durata_mesi'] = durata
if budget > 0.0:
    features['Budget_ml'] = budget
if team > 0:
    features['Team_size'] = team
if tec != '':
    features['Tecnologia'] = tec
if sett != '':
    features['Settore'] = sett

if st.sidebar.button('Calcola ROI'):
    if len(features) < 3:
        st.error('Devi specificare almeno 3 caratteristiche.')
    else:
        res = predict_roi(features)
        roi_val = res['ROI_pred']
        rel_val = res['Reliability_percent']
        std_val = res['Std']
        st.write(f"**ROI previsto:** {roi_val:.2f}")
        st.write(f"**Affidabilità:** {rel_val:.2f}%")
        st.write(f"**Deviazione standard:** {std_val:.2f}")
