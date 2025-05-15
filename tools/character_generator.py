import random
import streamlit as st

# Fonction de lancer de dés (e.g. '1d6')
def roll_dice(dice_str: str) -> int:
    count, sides = map(int, dice_str.lower().split('d'))
    return sum(random.randint(1, sides) for _ in range(count))

# Listes de base\ n# (… tous vos noms, races, classes, métiers, phrases, loot, etc.)
# Voir le code complet que vous avez déjà validé.

# Génération du personnage
def generate_character() -> dict:
    # … implémentation complète …
    pass

# Interface Streamlit
def run() -> None:
    st.title("Générateur de personnage RPG")
    if st.button("Générer un personnage"):
        char = generate_character()
        # Affichage de chaque attribut
        st.subheader(f"{char['Nom']}")
        st.markdown(f"**Race :** {char['Race']}")
        st.markdown(f"**Classe :** {char['Classe']}")
        st.markdown(f"**Métier :** {char['Métier']}")
        st.markdown(f"**Physique :** {char['Physique']}")
        st.markdown(f"**Mental :** {char['Mental']}")
        st.markdown(f"**Arme :** {char['Arme']}")
        st.markdown(f"**Armure :** {char['Armure']}")
        st.markdown(f"**Magie :** {char['Magie']}")
        st.markdown("**Loot :**")
        for item in char['Loot']:
            st.write(f"- {item}")