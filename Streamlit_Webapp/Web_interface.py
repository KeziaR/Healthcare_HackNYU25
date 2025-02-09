import streamlit as st
import requests as rq
from google import genai
import streamlit.components.v1 as components
<<<<<<< HEAD
=======


#import config 



# st.title("TitleName")

# client = genai.Client(api_key=config.INFO)

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="who is kylie jenner",
# )

# print(response.text)

# st.html(body)



>>>>>>> 7cd17d1 (added css to web interface)


    
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


