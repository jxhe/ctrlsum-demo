import streamlit as st
from datasets import load_dataset

@st.cache
def load_data(fname):
    return load_dataset('json', data_files=fname)['train']

st.set_page_config(
    page_title="CTRLsum demo",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    )

st.title('CTRLsum @Salesforce')
cnndm_entity_data = load_data('entity_control/entity.jsonl')

option = st.sidebar.selectbox(
    'dataset',
     ['CNNDM'],
     index=0)

if option == 'CNNDM':
    option_ctrl = st.sidebar.selectbox(
        'mode',
        ['entity control'],
        index=0)

if option_ctrl == 'entity control':
    # st.write('Ar')
    id_ = 0
    st.text_area('Article', cnndm_entity_data[id_]['article'], height=400)
    entity_id = st.selectbox(
        'entity',
        list(range(len(cnndm_entity_data[id_]['entity']))),
        format_func=lambda x: cnndm_entity_data[id_]['entity'][x],
        index=0)
    st.text_area('Generation', cnndm_entity_data[id_]['hypo'][entity_id])
