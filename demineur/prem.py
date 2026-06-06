#projet 2 d'info 
#Imports 

import streamlit as st
import supabase as sb

st.set_page_config(page_title="Démineur", page_icon=None,  initial_sidebar_state="collapsed", menu_items=None)
st.session_state["usnm"] = "pas_de_nom"
st.title("Bienvenue sur le Démineur.")
st.subheader("Sur ce site internet, vous aurez l'opportunité de jouer au démineur et de comparer votre score avec vos amis.", divider=True)
st.subheader(" Le but du jeu est de découvrir toutes les cases libres sans faire exploser les mines, c'est-à-dire sans cliquer sur les cases qui les dissimulent. Lorsque le joueur clique sur une case libre comportant au moins une mine dans l'une de ses cases avoisinantes, un chiffre apparaît, indiquant ce nombre de mines.")

st.subheader("Insère ton nom de joueur et clique sur le bouton rouge pour lancer le jeu.")
nom = st.text_input("Pseudo")
st.session_state["usnm"] = nom
changer_page = st.button("Allons déminer", use_container_width=True, type="primary")

if changer_page:
    st.switch_page('pages/main_jeu.py')
