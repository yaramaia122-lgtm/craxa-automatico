import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Gerador de Crachás - Aura Apoena")

st.title("🪪 Gerador de Crachás - Aura Apoena")

# Interface do Streamlit (Substitui o CustomTkinter)
nome = st.text_input("Nome Completo:")
cpf = st.text_input("CPF:")
empresa = st.text_input("Empresa:")
gerencia = st.text_input("Gerência:")
funcao = st.text_input("Função:")
nrs = st.text_area("Treinamentos (Ex: NR10: 01/01/2026):")

foto = st.file_uploader("Carregar Foto", type=["jpg", "png"])

if st.button("GERAR CRACHÁ"):
    if nome and foto:
        # Lógica de processamento com Pillow
        img = Image.open(foto)
        # ... aqui você insere sua lógica de desenho (ImageDraw) ...
        
        st.success(f"Crachá de {nome} gerado com sucesso!")
        
        # Exemplo de como mostrar/baixar o resultado no navegador
        st.image(img, caption="Prévia do Crachá", width=300)
        
        # Botão de download
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        st.download_button(
            label="Baixar Crachá",
            data=buf.getvalue(),
            file_name=f"cracha_{nome}.png",
            mime="image/png"
        )
    else:
        st.error("Por favor, preencha o nome e carregue uma foto.")
