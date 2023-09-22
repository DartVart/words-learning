import streamlit as st

st.title('90-Seconds Method')
st.subheader('Of learning words')

st.markdown('I learned about this method from the [Энциклоп (Entsiclop)](https://www.youtube.com/watch?v=Q8_rLOrt49o&t=2s&ab_channel=%D0%AD%D0%BD%D1%86%D0%B8%D0%BA%D0%BB%D0%BE%D0%BF) video.')

st.header('Method')

st.markdown("1. Let's say you need to learn a word in a foreign language. You start by finding **a sentence with that word**, I myself use https://context.reverso.net for this.")
st.markdown("2. Then **for a week**, you read that sentence **aloud 2-3 times each day**, concentrating well on the new word. You need to concentrate **really well**! Not repeating it out loud mechanically! It takes about 10 seconds for 2-3 readings. Total for the week — 70 seconds.")
st.markdown("3. Then, **a week later**, you read that sentence again 2-3 times (+ 10 seconds).")
st.markdown("4. Finally, **after 2 weeks**, you last read this sentence 2-3 times (+ 10 seconds).")
st.markdown("5. Congratulations, that word is very well remembered! And it took 90 seconds!")
st.markdown("*P.S. It usually still takes me longer than 10 seconds and I do more reps until I realize I've been focused enough.*")

st.header("Then what's the point of this app?")

st.markdown("This app will let you automatically create sentences in your notes that you need to repeat 😊")
st.markdown('It also uses another cool thing for this — [notion](https://www.notion.so/). You create a calendar page in notion and this app adds notes called "Words learning" for each day. The notes will have sentences that you need to repeat today.')
st.markdown("To do this, you will need to enter sentence and choose which day the word study will start on.")
st.markdown("*P.S. Don't forget to add token and database ID from notion! **It's not very secure**, but the settings are saved in the url, so you can keep the link with you and quickly go there without reenter settings.*")
