import streamlit as st
import json

# Carica i dati dal file JSON
with open('scheda.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('dieta.json', 'r', encoding='utf-8') as f:
    data_dieta = json.load(f)

def metti_spazio(markdown):
    return st.markdown(f"""
                       &nbsp;&nbsp;&nbsp;&nbsp;
                       &nbsp;&nbsp;&nbsp;&nbsp;
                       &nbsp;&nbsp;&nbsp;&nbsp;
                       -- {markdown}""")

# Funzione per mostrare gli esercizi di un giorno
def mostra_esercizi(giorno):
    st.markdown(f"## **{giorno}**")
    st.divider()
    for gruppo, esercizi in data['giorni'][giorno].items():
        st.markdown(f"## *{gruppo}*")
        for esercizio in esercizi:
            st.markdown(f"- **{esercizio['esercizio']}**")
            markdown_esercizi = f"**{esercizio['serie']}** serie da **{esercizio['ripetizioni']}** ripetizioni"
            metti_spazio(markdown_esercizi)
            if 'link' in esercizio and esercizio['link']:
                with st.expander("Mostra tutorial"):
                    st.video(esercizio['link'])
    st.divider()

# Funzione per mostrare le opzioni di un pasto
def mostra_pasto(pasto):
    for opzione, dettagli in data_dieta['dieta_settimanale'][pasto].items():
        st.markdown(f"### {opzione.capitalize()}")
        for item in dettagli['pasto']:
            st.markdown(f"- {item}")

# Titolo dell'app
st.title("GYM")

# Crea due tab
tab1, tab2 = st.tabs(["Scheda di Allenamento", "Dieta"])

# Tab della scheda di allenamento
with tab1:
    st.header("Scheda di Allenamento")
    coppie_giorni = {
        "Lunedì/Martedì": ["Lunedì"],
        "Mercoledì/Giovedì": ["Mercoledì"],
        "Venerdì/Sabato": ["Venerdì"]
    }
    scelta_coppia = st.selectbox("Seleziona la coppia di giorni", list(coppie_giorni.keys()))
    giorni_selezionati = coppie_giorni[scelta_coppia]
    
    for giorno in giorni_selezionati:
        if giorno in data['giorni']:
            mostra_esercizi(giorno)
        else:
            st.write(f"Nessun dato disponibile per {giorno}")

# Tab della dieta
with tab2:
    st.header("Dieta")
    pasti = list(data_dieta['dieta_settimanale'].keys())
    scelta_pasto = st.selectbox("Seleziona un pasto", pasti)
    
    if scelta_pasto:
        mostra_pasto(scelta_pasto)