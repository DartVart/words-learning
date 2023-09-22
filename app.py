import streamlit as st

from utils.notion import add_sentence
from utils.text_processing import split_to_sentences


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
expander.subheader('How to get token?')
expander.markdown('Go to https://www.notion.so/my-integrations and create a new integration. There you will find a Internal Integration Secret that will be your token.')
expander.markdown('Do not forgot to add connection to your page! In the notion page with the calendar go to ••• ➔ Connections ➔ Add connection ➔ Find your integration and add it.')
expander.markdown("""---""")
database_id = expander.text_input(
    'Database ID', key="database_id", value=values["database_id"] or "", on_change=save_values
)
expander.subheader('How to get database ID?')
expander.markdown('1. Go to your notion page with the calendar and check the url. The url should be something like https://www.notion.so/thienqc/f1077c8a72444493bd8c7ffe5b79aa92?v=833710c1e5604896af93616995f9b26f.')
expander.write('2. The database ID from example is :red[f1077c8a72444493bd8c7ffe5b79aa92].')

text = st.text_area('Enter sentences with the words to memorize. Highlight the word with ** on both sides. The sentences will be split automatically and may be separated by punctuation and line breaks.')
date = st.date_input('Enter first date to memorize')

if st.button("Write"):
    sentences = split_to_sentences(text)
    slots = [st.empty() for _ in sentences]
    for i, sentence in enumerate(sentences):
        is_success = add_sentence(sentence, date, database_id, token)
        slot = slots[-(i + 1)]
        if is_success:
            slot.success(f'Your sentence "{sentence}" has been written!')
        else:
            slot.error(f'Something went wrong when I write "{sentence}"!')
