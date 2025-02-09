import streamlit as st
import requests as rq
from google import genai
import streamlit.components.v1 as components




    
web_app = """

<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
//May change later - depends on what we use

<title>How Do I Feel Today? App</title>
//Working title

<link rel="stylesheet" href="style.css" type="text/css"/>
<nav>
    <ul>

    </ul>
    
</nav>
//Add navigation bar later

<h1>How Do I Feel Today?</h1>

</head>
<body>
<aside class="chatbox">

</aside>
//Chatbox goes here

</body>
<section class="moodtracker"></section>


<footer>

</footer>
Contributors:
<ul>
</ul>

</html>
"""

components.html(web_app, height=800, scrolling=True)


choice = st.radio('Background Type', ['Image', 'Gradient'])

if choice == 'Image':
    st.title('Image Background')
    st.markdown('Boop! :ghost:')

    image = './app/static/house-panther-nose.png'

    css = f'''
    <style>
        .stApp {{
            background-image: url({image});
            background-size: cover;

        }}
        .stApp > header {{
            background-color: transparent;
        }}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

else:
    st.title('Gradient Background')
    st.write('Look at the pretty shifting background')

    with open('./files/wave.css') as f:
        css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)