import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pickle

st.title('Comparing changes of different histone marks with gene expression changes...!')

def load_pickle(file):
    with open(file, 'rb') as f:
        obj = pickle.load(f)
    return obj

st.write("""
    This is an analysis on how changes in abundance on logFC in different histone marks can affect the logFC of genes.
    """)

histone_abundances = load_pickle('data/streamlit_data/histone_abundances.pkl')
histone_abundances_PRC2 = load_pickle('data/streamlit_data/histone_abundances_PRC2.pkl')

col1, col2 = st.columns([1, 4])

if 'camera' not in st.session_state:
    st.session_state['camera'] = dict(eye=dict(x=1.25, y=1.25, z=1.25))  # Default camera position

with col1:
    # Adjust the size of the marker with the slider
    marker_size = st.slider('Dot size', min_value=1.0, max_value=6.0, value=4.0, step=0.1)

color_min, color_max = -4.5, 4.5
scatter_all_genes = go.Scatter3d(
    x=histone_abundances['change_K27me3'],
    y=histone_abundances['change_K36me2'],
    z=histone_abundances['change_K36me3'],
    mode='markers',
    marker=dict(
        size=marker_size,
        color=histone_abundances['LFC'],  # color by z-value
        colorscale='Picnic',         # Choose a colormap
        colorbar=dict(title='Log2FC'),  # Add color legend
        showscale=True,
        cmin=color_min, cmax=color_max
    )
)

scatter_PRC2 = go.Scatter3d(
    x=histone_abundances_PRC2['change_K27me3'],
    y=histone_abundances_PRC2['change_K36me2'],
    z=histone_abundances_PRC2['change_K36me3'],
    mode='markers',
    marker=dict(
        size=marker_size,
        color='black',
    )
)

# fig = go.Figure(data=[
#     scatter_all_genes
# ])


# Initialize session state to keep track of which plot to show
if 'show_PRC2' not in st.session_state:
    st.session_state['show_PRC2'] = False

def toggle_PRC2():
    st.session_state['show_PRC2'] = not st.session_state['show_PRC2']


if st.session_state['show_PRC2']:
    # Show the plot with PRC2 targets
    fig = go.Figure(data=[scatter_all_genes, scatter_PRC2])
else:
    # Show the plot without PRC2 targets
    fig = go.Figure(data=[scatter_all_genes])

# Customize the plot
fig.update_layout(
    title='Histone Mark Abundances',
    scene=dict(
        xaxis_title='H3K27me3 LFC',
        yaxis_title='H3K36me2 LFC',
        zaxis_title='H3K36me3 LFC'
    ),
    autosize=False,
    width=800,
    height=600
)

with col2:
    st.plotly_chart(fig, use_container_width=True)

if st.session_state['show_PRC2']:
    st.button('Hide PRC2 targets', on_click=toggle_PRC2)
else:
    st.button('Show PRC2 targets', on_click=toggle_PRC2)


#############################

st.title('Abundance in histone marks changes in abundance on logFC in different histone marks with gene expression changes')


color_min, color_max = -2, 4.33
scatter_all_genes = go.Scatter3d(
    x=histone_abundances['WT_K27me3'],
    y=histone_abundances['WT_K36me2'],
    z=histone_abundances['WT_K36me3'],
    mode='markers',
    marker=dict(
        size=3,
        color=np.log10(histone_abundances['tpm_Parental']),  # color by z-value
        colorscale='Picnic',         # Choose a colormap
        colorbar=dict(title='log10(tpm_Parental)'),  # Add color legend
        showscale=True,
        cmin=color_min, cmax=color_max
    )
)

scatter_PRC2 = go.Scatter3d(
    x=histone_abundances_PRC2['WT_K27me3'],
    y=histone_abundances_PRC2['WT_K36me2'],
    z=histone_abundances_PRC2['WT_K36me3'],
    mode='markers',
    marker=dict(
        size=3,
        color='black',
    )
)

fig = go.Figure(data=[
    scatter_all_genes
])



# Customize the plot
fig.update_layout(
    title='3D Scatter Plot',
    scene=dict(
        xaxis_title='WT_K27me3',
        yaxis_title='WT_K36me2',
        zaxis_title='WT_K36me3'
    ),
    autosize=False,
    width=800,
    height=600
)

st.plotly_chart(fig, use_container_width=True)

#############################################


scatter_all_genes = go.Scatter3d(
    x=histone_abundances['NSD1KO_K27me3'],
    y=histone_abundances['NSD1KO_K36me2'],
    z=histone_abundances['NSD1KO_K36me3'],
    mode='markers',
    marker=dict(
        size=3,
        color=np.log10(histone_abundances['tpm_NSD1KO']),  # color by z-value
        colorscale='Picnic',         # Choose a colormap
        colorbar=dict(title='log10(tpm_NSD1KO)'),  # Add color legend
        showscale=True,
        cmin=color_min, cmax=color_max
    )
)

scatter_PRC2 = go.Scatter3d(
    x=histone_abundances_PRC2['NSD1KO_K27me3'],
    y=histone_abundances_PRC2['NSD1KO_K36me2'],
    z=histone_abundances_PRC2['NSD1KO_K36me3'],
    mode='markers',
    marker=dict(
        size=3,
        color='black',
    )
)

fig = go.Figure(data=[
    scatter_all_genes
])

# Customize the plot
fig.update_layout(
    title='3D Scatter Plot',
    scene=dict(
        xaxis_title='NSD1KO_K27me3',
        yaxis_title='NSD1KO_K36me2',
        zaxis_title='NSD1KO_K36me3'
    ),
    autosize=False,
    width=800,
    height=600
)

st.plotly_chart(fig, use_container_width=True)
