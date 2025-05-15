import streamlit as st

# ⚠️ Doit être la toute première commande
st.set_page_config(page_title="JDR RPG Generator", layout="wide")

from tools.character_generator import run as character_generator_run

st.sidebar.title("🧰 Outils RPG")
choice = st.sidebar.selectbox(
    "Choisissez un outil",
    ["Générateur de personnage RPG"],
    index=0
)

if choice == "Générateur de personnage RPG":
    character_generator_run()
else:
    st.write("Sélectionnez un outil dans la barre latérale.")