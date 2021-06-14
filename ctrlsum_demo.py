import random
import SessionState
import streamlit as st
from datasets import load_dataset

import streamlit.components.v1 as components

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
cnndm_length_data = load_data('length_control/length.jsonl')
arxiv_contribution_data = load_data('contribution_control/contribution.jsonl')
bigpatent_purpose_data = load_data('purpose_control/purpose.jsonl')
newsqa_data = load_data('newsqa/newsqa.jsonl')

option_ctrl = st.sidebar.selectbox(
    'control aspect',
     ['entity control', 'length control', 
     'contribution summarization', 'patent purpose summarization',
     'question-guided control'],
     index=0)

if option_ctrl == 'entity control' or option_ctrl == 'length control':
    data_list = ['CNNDM']
elif option_ctrl == 'contribution summarization':
    data_list = ['arxiv']
elif option_ctrl == 'patent purpose summarization':
    data_list = ['BIGPATENT']
elif option_ctrl == 'question-guided control':
    data_list = ['newsQA']
else:
    raise ValueError(f'control mode {option_ctrl} not recognized')

option_data = st.sidebar.selectbox(
    'dataset',
    data_list,
    index=0)

ss = SessionState.get(ent_id=0, len_id=0, ctr_id=0, purpose_id=0, qa_id=0)
shuffle = st.sidebar.button('resample article')

if option_ctrl == 'entity control':
    if shuffle:
        ss.ent_id = random.choice(range(len(cnndm_entity_data)))

    # st.write(cnndm_entity_data[ss.ent_id]['article'])
    st.subheader('Source Article')
    # st.write(cnndm_entity_data[ss.ent_id]['article'])
    st.text_area('', cnndm_entity_data[ss.ent_id]['article'], height=400)

    st.subheader('Entity (Control Tokens)')
    col1, _, _ = st.beta_columns(3)
    with col1:
        entity_id = st.selectbox(
            '',
            list(range(len(cnndm_entity_data[ss.ent_id]['entity']))),
            format_func=lambda x: cnndm_entity_data[ss.ent_id]['entity'][x],
            index=0)

    st.subheader('Generation')
    st.write(cnndm_entity_data[ss.ent_id]['hypo'][entity_id])
elif option_ctrl == 'length control':
    if shuffle:
        ss.len_id = random.choice(range(len(cnndm_length_data)))

    st.subheader('Source Article')
    st.text_area('', cnndm_length_data[ss.len_id]['article'], height=400)
    st.subheader('Length Control')

    col1, _, _ = st.beta_columns(3)
    with col1:
        len_id = st.select_slider(
            '',
            list(range(len(cnndm_length_data[ss.len_id]['keyword']))),
            )

    st.subheader('Control Tokens')
    st.write(cnndm_length_data[ss.len_id]['keyword'][len_id])

    st.subheader('Generation')
    st.write(cnndm_length_data[ss.len_id]['hypo'][len_id])
elif option_ctrl == 'contribution summarization':
    if shuffle:
        ss.ctr_id = random.choice(range(len(arxiv_contribution_data)))

    st.subheader('Source Article')
    st.text_area('', arxiv_contribution_data[ss.ctr_id]['article'], height=400)

    st.subheader('Control Tokens (keywords and prompt)')
    st.write(arxiv_contribution_data[ss.ctr_id]['prompt'])

    st.subheader('Generation')
    st.write(arxiv_contribution_data[ss.ctr_id]['hypo']) 
elif option_ctrl == 'patent purpose summarization':
    if shuffle:
        ss.purpose_id = random.choice(range(len(bigpatent_purpose_data)))

    st.subheader('Source Article')
    st.text_area('', bigpatent_purpose_data[ss.purpose_id]['article'], height=400)

    st.subheader('Control Tokens (keywords and prompt)')
    st.write(bigpatent_purpose_data[ss.purpose_id]['prompt'])

    st.subheader('Generation')
    st.write(bigpatent_purpose_data[ss.purpose_id]['hypo'])  
elif option_ctrl == 'question-guided control':
    if shuffle:
        ss.qa_id = random.choice(range(len(newsqa_data)))

    st.subheader('Source Article')
    st.text_area('', newsqa_data[ss.qa_id]['article'], height=400)

    st.subheader('Control Tokens (keywords and prompt)')
    question_id = st.selectbox(
        '',
        list(range(len(newsqa_data[ss.qa_id]['Q']))),
        format_func=lambda x: newsqa_data[ss.qa_id]['Q'][x],
        index=0)


    st.subheader('Generation')
    st.write(newsqa_data[ss.qa_id]['A'][question_id])

    st.subheader('Gold Answer')
    st.write(newsqa_data[ss.qa_id]['GA'][question_id])
