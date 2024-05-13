import os
import streamlit as st

from streamlit_eidos import st_eidos
from oceanum.eidos import Eidos, Node

os.environ["EIDOS_RENDERER"] = "https://render.eidos.oceanum.tech"

st.write("## Example EIDOS")


e = Eidos(
    id="eidos_test",
    name="EIDOS Test",
    title="Test",
    data=[],
    rootNode=Node(id="my-map", name="Root", nodeType="world", nodeSpec={}),
)

value = st_eidos(e, height=800, events=["click"])

st.write(value)
