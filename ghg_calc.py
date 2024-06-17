import streamlit as st
import base64

st.set_page_config(
    page_title="Emissão CO2",
    page_icon="🌳"
)

@st.cache_data()
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("pdipaper5.png")
img2 = get_img_as_base64("pdiside.png")

page_bg_img = f"""
<style>
header, footer {{
    visibility: hidden !important;
}}

#MainMenu {{
    visibility: visible !important;
    color: #F44D00;
}}

[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:fundoesg4k/png;base64,{img}");
    background-size: cover; 
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:esgfundo1/png;base64,{img2}");
    background-position: center; 
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

.stTextInput>div>div>input[type="text"] {{
    background-color: #C5D6ED; 
    color: #000; 
    border-radius: 7px; 
    border: 2px solid #000010; 
    padding: 5px; 
    width: 500;
}}

@media (max-width: 360px) {{
    [data-testid="stAppViewContainer"] > .main, [data-testid="stSidebar"] > div:first-child {{
        background-size: auto;
    }}
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.image("Logopdi.png", width=250)

def main():
    st.title("Calculadora de Compensação de GHG")

    st.header("Insira as emissões da sua empresa")
    co2 = st.number_input("Quantidade de CO2 (em toneladas):", min_value=0.0, step=0.1)
    bioco2 = st.number_input("Quantidade de bioCO2 (em toneladas):", min_value=0.0, step=0.1)

    if co2 > 0 or bioco2 > 0:
        total_co2 = co2 + bioco2

        # Estimativa revisada: uma árvore pode absorver cerca de 21,77 kg de CO2 por ano
        co2_per_tree = 21.77 / 1000  # Converter para toneladas
        trees_needed = total_co2 / co2_per_tree

        st.subheader("Resultados")
        st.write(f"Emissões totais de CO2: {total_co2:.2f} toneladas")
        st.write(f"Você precisará plantar aproximadamente {trees_needed:.0f} árvores para compensar essas emissões.")

if __name__ == "__main__":
    main()
    
st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por [PedroFS](https://linktr.ee/Pedrofsf)")
