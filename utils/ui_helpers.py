import streamlit as st
from PIL import Image
from pathlib import Path

def display_erd():
    """Display the ERD diagram."""
    erd_path = Path("data/SQLite3 Sakila Sample Database ERD.png")
    if erd_path.exists():
        erd_image = Image.open(erd_path)
        st.image(erd_image, caption="Sakila Database ERD", use_column_width=True)
    else:
        st.error(f"ERD diagram not found at {erd_path}")
