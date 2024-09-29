import numpy as np
import pandas as pd
import plotly.graph_objects as go
# from st_speckmol import speck_plot
import glob

import streamlit as st
from streamlit_option_menu import option_menu
import py3Dmol
from stmol import showmol

st.set_page_config(
    page_title="My Web App",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
    <style>
        .st-emotion-cache-79elbk{
            display: none;
        }
        .justified-text {
        text-align: justify;
        font-size: 18px; /* Adjust size as needed */
        line-height: 1.6; /* Line height for better readability */
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    page_selected = option_menu(None, 
        options=["Introduction", 'Histone Changes', '---'], 
        icons=['house', '0-square'], default_index=0)

if page_selected == "Introduction":
    st.title('NSD1')
    # NSD1
    col1, col2 = st.columns(2)
    with col1:
        cartoon_style = {"cartoon": {
                    "color": "spectrum",
                    "thickness": 0.4,
                    "spin_on": True
                }}
        sphere_style = {'sphere':{}}

        if 'view' not in st.session_state:
            st.session_state.view = py3Dmol.view(query="pdb:2naa", width=500, height=500)
            st.session_state.view.setStyle(cartoon_style)
            st.session_state.view.spin(True)

        if 'current_style' not in st.session_state:
            st.session_state.current_style = 'cartoon'

        def change_mol_style():
            if st.session_state.current_style == 'cartoon':
                st.session_state.view.setStyle(sphere_style)
                st.session_state.current_style = 'sphere'
            else:
                st.session_state.view.setStyle(cartoon_style)
                st.session_state.current_style = 'cartoon'

        showmol(st.session_state.view, height=600, width=800)
        st.button(label="Change Style", on_click=change_mol_style)

    with col2:
        text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 
            Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. 
            Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. 
            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 
            Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. 
            Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. 
            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 
            Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. 
            Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. 
            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 
            Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. 
            Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. 
            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 
            Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. 
            Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. 
            Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
            """
        st.markdown(f'<div class="justified-text">{text}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="justified-text">{text}</div>', unsafe_allow_html=True)
    st.title('NSD1')


if page_selected == "Histone Changes":
    exec(open('pages/histone.changes.genes.py').read())