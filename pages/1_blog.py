import streamlit as st


st.set_page_config(page_title="Food Recommendation",page_icon=":shallow_pan_of_food:",layout="wide")
blog="""
    <style>
    :root {
    --box-x-padding: 2rem;
    --box-y-padding: 2rem;
    }
    @media (min-width: 40em) {
    :root {
        --box-y-padding: 4rem;
    }
    }
    @media (min-width: 60em) {
    :root {
        --box-x-padding: 3rem;
        --box-y-padding: 6rem;
    }
    }
    @media (min-width: 40em) {
    section {
        display: grid;
        grid-template-rows: repeat(3, auto);
        grid-template-columns: 4fr 4fr 5fr;
        grid-template-areas: '. . title' 'img img content' 'img img .';
        max-width: 1000px;
        margin-right: auto;
        margin-left: auto;
    }
    section::after {
        content: '';
        grid-column: 2/-1;
        grid-row: 1/3;
        position: relative;
        z-index: -1;
        background: #fff;
        box-shadow: 0 0.2em 1em rgba(61,48,41,0.2);
    }
    h1 {
        grid-area: title;
        padding-top: var(--box-y-padding);
        padding-left: var(--box-x-padding);
    }
    .content {
        grid-area: content;
        padding-bottom: var(--box-y-padding);
        padding-left: var(--box-x-padding);
        padding-right: var(--box-x-padding);
    }
    .img {
        grid-area: img;
    }
    }
    @import url("https://fonts.googleapis.com/css?family=Montserrat:400,400i,700");
    html {
    font-family: Montserrat, sans-serif;
    font-size: 15px;
    background-color: #f5f5f5;
    }
    body {
    padding: 1em;
    }
    h1 {
    font-size: 4em;
    margin: 0 0 1rem;
    font-family: serif;
    position: relative;
    }
    h1::after {
    content: '';
    position: absolute;
    width: 6rem;
    background-color: #ccc;
    height: 2px;
    top: 0;
    left: 0;
    }
    @media (min-width: 40em) {
    h1::after {
        left: var(--box-x-padding);
        top: var(--box-y-padding);
    }
    }
    .content {
    color: #4d4d4d;
    margin-bottom: var(--box-y-padding);
    }
    @media (min-width: 40em) {
    .content {
        margin-bottom: 0;
    }
    }
    p {
    margin-top: 0;
    margin-bottom: var(--box-y-padding);
    line-height: 1.5;
    }
    .content a {
    text-decoration: none;
    border: 1px solid #b3b3b3;
    border-radius: 1em;
    padding: 1em 2em;
    text-transform: uppercase;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.05em;
    color: inherit;
    display: inline-block;
    background-color: #fff;
    }
    .img {
    position: relative;
    }
    .img a {
    position: absolute;
    left: 0;
    bottom: 0;
    }
    img {
    max-width: 100%;
    vertical-align: middle;
    box-shadow: 0 0.2em 1.2em rgba(61,48,41,0.1);
    }
    .attribution {
    position: absolute;
    bottom: 0;
    right: 0;
    background-color: #ea4c89;
    color: #fff;
    padding: 0.5em 1em;
    }
    .devclr {
    color: red;
    }

    </style>
    
    <body>
    <section>
    <h1>Food</h1>
    <div class="content">
        <p>Welcome to our food recommendations website, where culinary adventures await! Whether you're a seasoned foodie or simply seeking new flavors to tantalize your taste buds, we're here to guide you on a mouthwatering journey through the diverse and delectable world of cuisine.<br><span class="devclr">Developed for a Friend ❤️</span>.</p><a href="">Learn more</a>
    </div>
    <div class="img"><img src="https://spaceshuttle-sbm-1-d2725437.deta.app/cdn/2tuan1273rfv.jpg"/><a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px;" href="#" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Anders Jildén"><span style="display:inline-block;padding:2px 3px;"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-1px;fill:white;" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M20.8 18.1c0 2.7-2.2 4.8-4.8 4.8s-4.8-2.1-4.8-4.8c0-2.7 2.2-4.8 4.8-4.8 2.7.1 4.8 2.2 4.8 4.8zm11.2-7.4v14.9c0 2.3-1.9 4.3-4.3 4.3h-23.4c-2.4 0-4.3-1.9-4.3-4.3v-15c0-2.3 1.9-4.3 4.3-4.3h3.7l.8-2.3c.4-1.1 1.7-2 2.9-2h8.6c1.2 0 2.5.9 2.9 2l.8 2.4h3.7c2.4 0 4.3 1.9 4.3 4.3zm-8.6 7.5c0-4.1-3.3-7.5-7.5-7.5-4.1 0-7.5 3.4-7.5 7.5s3.3 7.5 7.5 7.5c4.2-.1 7.5-3.4 7.5-7.5z"></path></svg></span><span style="display:inline-block;padding:2px 3px;">Akshay Rao</span></a></div>
    </section>
    
    </body>
    
"""
st.markdown(blog,unsafe_allow_html=True)
