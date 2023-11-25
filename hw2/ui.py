import streamlit as st
from summarizer import summarize


def main():
    st.title('Сокращение текста')

    user_input = st.text_area('Введите текст для сокращения', height=200)

    if st.button('Сократить'):
        result = summarize(user_input)

        st.subheader('Сокращённый текст')
        st.write(result)


if __name__ == '__main__':
    main()
