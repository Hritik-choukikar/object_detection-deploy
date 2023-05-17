import main

import streamlit as st


import streamlit as st
import pandas as pd
from io import StringIO



uploaded_file = st.file_uploader("Upload Image")
image = Image.open(uploaded_file)
st.image(image, caption='Input', use_column_width=True)
img_array = np.array(image)
img=image(img_array)



model=load_model()



results=model(img)




num_people = 0
for i in range(len(results['detection_classes'][0])):
    if results['detection_classes'][0][i] == 1:
        # 1 is the class ID for people
        # if results['detection_scores'][0][i] > 0.3:  # Only count detections with high confidence
      num_people += 1

st.write(num_people)

