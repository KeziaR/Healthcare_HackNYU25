import streamlit as st
import requests as rq
from google import genai
import streamlit.components.v1 as components

    
web_app = """

<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
//May change later - depends on what we use

<title>This is the title</title>
//Title will be added later

<link rel="stylesheet" href="style.css" type="text/css"/>
<nav>
    <ul>

    </ul>
    
</nav>
//Add navigation bar later

</head>
<body>
<aside>

</aside>
//Chatbox goes here

</body>
//Should include mood tracker and other features

<footer>

</footer>
//Miscillaneous information

</html>
"""

components.html(web_app, height=800, scrolling=True)

