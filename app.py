import streamlit as st

from notion import add_sentence


def read_values():
    url_params = st.experimental_get_query_params()
    return {
        "token": url_params["token"][0] if "token" in url_params else None,
        "database_id": url_params["database_id"][0] if "database_id" in url_params else None,
    }


def save_values():
    st.experimental_set_query_params(
        token=st.session_state.token,
        database_id=st.session_state.database_id,
    )


st.title('90 Seconds Method')
st.subheader('Of learning words')

expander = st.expander('Notion settings')

values = read_values()

token = expander.text_input('Token', key="token", value=values["token"] or "", on_change=save_values)
database_id = expander.text_input(
    'Database ID', key="database_id", value=values["database_id"] or "", on_change=save_values
)

st.write()

sentence = st.text_input('Enter a sentence with the word to memorize. Highlight the word with ** on both sides.')
date = st.date_input('Enter first date to memorize')

if st.button("Write"):
    res = add_sentence(sentence, date, database_id, token)
    if res.status_code == 200:
        st.success(f'Your sentence "{sentence}" has been written!')
    else:
        st.error('Something went wrong')
