#projet 2 d'info 
#Imports 
import clsmnt as cl
import streamlit as st
import supabase as sb

st.set_page_config(page_title="Démineur", page_icon=None,  initial_sidebar_state="collapsed", menu_items=None)
st.session_state["usnm"] = "pas_de_nom"
st.title("Bienvenue sur le Démineur.")
st.subheader("Sur ce site internet, vous aurez l'opportunité de jouer au démineur et de comparer votre score avec vos amis.", divider=True)
st.subheader("La règle du jeu est simple : le joueur sélectionne une case sur la grille, et cette case révèle un
nombre qui indique le nombre de mines se trouvant dans les cases adjacentes. En utilisant ces informations, le joueur doit déduire l'emplacement des mines et les marquer avec des drapeaux pour les éviter.")

st.subheader("Insère ton nom de joueur et clique sur le bouton rouge pour lancer le jeu.")
nom = st.text_input("Pseudo")
st.session_state["usnm"] = nom
changer_page = st.button("Allons déminer", use_container_width=True, type="primary")

if changer_page:
    st.switch_page('pages/main_jeu.py')
