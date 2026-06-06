#projet 2 d'info 
#Imports 

import streamlit as st
import supabase as sb

st.set_page_config(page_title="Démineur", page_icon=None,  initial_sidebar_state="collapsed", menu_items=None)
st.session_state["usnm"] = "pas_de_nom"
st.title("Bienvenue sur le Démineur ")
st.subheader("Sur ce site internet vous aurez l'opportunitée de jouer au démineur et de comparer votre score avec vos amis", divider=True)


st.subheader("Insert ton nom de joueur et clique sur le bouton rouge pour lancer le jeu")
nom = st.text_input("Pseudo")
st.session_state["usnm"] = nom
changer_page = st.button("Allons déminer", use_container_width=True, type="primary")

if changer_page:
    st.switch_page('D:\demineur\pages\main_jeu.py')
