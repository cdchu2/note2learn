import streamlit as st
import redis 
import matplotlib.pyplot as plt
from PIL import Image

# st.header('st.button')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')

r = redis.Redis(host='localhost', port=6379, db=0)

def app():
     # st.title('Welcome')
     # name = st.text_input('Name and Surname:')
     # age = st.number_input('Age:')
     # if st.button('Submit'):
     #      r.set('name', name)
     #      r.set('age', age)
     #      st.success('Data is stored successfully!')

     st.title('Redis Search')

     index = st.text_input('Index:')
     label = st.text_input('Label:')
     if st.button('Search'):
          doc_ = r.ft(index).search(label).docs
          url = [doc.url for i, doc in enumerate(doc_)]
          for i in url:
               img = Image.open(i)

               st.image(img)
if __name__ == '__main__':
     app()