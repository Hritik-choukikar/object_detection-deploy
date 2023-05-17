 
import stream
import streamlit as st


if __name__ == "__main__":
  uploaded_file = st.file_uploader("Upload Image")
  image = Image.open(uploaded_file)
 
  st.image(image, caption='Input', use_column_width=True)

