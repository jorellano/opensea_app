import streamlit as st
import requests, json

endpoint = st.sidebar.selectbox("Endpoints", ['Assets', 'Events', 'Rarity'])
st.header(f"OpenSea NFT API Explorer - {endpoint}")

st.sidebar.subheader("Filters")

collection = st.sidebar.text_input("Collection")
owner = st.sidebar.text_input('Owner')


if endpoint =='Assets':
    params = {}
   
    if collection:
       params['collection'] = collection
    if owner:
        params['owner'] = owner
    r = requests.get("https://api.opensea.io/api/v1/assets", params=params)

    response = r.json()

    for asset in response["assets"]:
        if asset['image_url'].endswith('mp4'):
            st.video(asset['image_url'])
        else:
            st.image(asset['image_url'])
    st.write(r.json())