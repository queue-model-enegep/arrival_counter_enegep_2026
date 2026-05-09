from datetime import datetime, timedelta

import streamlit as st
import pandas as pd

st.set_page_config(layout='centered')

    

# Adjusting the dimensions of the button.
st.markdown("""
    <style>
    div.stButton > button {
        height: 80px;  /* Tall buttons for fat fingers */
        font-weight: bold;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Initializing the data container.
if not 'df' in st.session_state:
    df = pd.DataFrame({
        'Tempo_chegada': []
    })
    st.session_state.df = df

st.title('Contador de chegadas')

# Adding the buttons.
with st.container(border=True):
    for i in range(1, 11):
        st.button(
            label=f'+{i}',
            width='stretch',
            type='primary',
            key=f'b{i}'
        )

# Extracting the data after each button press.
for i in range(1, 11):
    if st.session_state[f'b{i}']:
        new_row = pd.DataFrame({'Tempo_chegada': i*[(datetime.now() - timedelta(hours=3)).strftime("%H:%M:%S")]})
        st.session_state.df = pd.concat([st.session_state.df, new_row])
        st.toast(
            body='salvo!',
            duration=1,
            icon='✅'
        )

# Download button for the data collected.
csv = st.session_state.df.to_csv(index=False).encode('utf-8')
st.download_button(
    "📥Baixar",
    csv,
    f"contagem.csv",
    "text/csv",
    use_container_width=True
)

        
        

    
