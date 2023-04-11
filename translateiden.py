import pandas as pd
import streamlit as st
# Load the Indonesian-English dictionary
dictionary = pd.read_csv("ind_eng_dict.csv")
def translate(word):
    if "Indonesian" not in dictionary.columns:
        return "Kolom 'Indonesian' tidak ditemukan dalam kamus."
    translation = dictionary[dictionary["Indonesian"] == word]["English"]
    if len(translation) > 0:
        return translation.values[0]
    else:
        return "Kata tidak ditemukan dalam kamus."

# Set up the Streamlit app
st.title("Kamus Bahasa Indonesia-Inggris")
word = st.text_input("Masukkan kata dalam bahasa Indonesia:")
if st.button("Terjemahkan"):
    translation = translate(word)
    st.write("Arti kata dalam bahasa Inggris:")
    st.write(translation)
