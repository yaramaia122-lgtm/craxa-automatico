import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Configuração da Página
st.set_page_config(page_title="Gerador de Crachás Aura Apoena", layout="wide")

def gerar_imagem_cracha(dados, foto_upload):
    # Criar um fundo branco para o crachá (Tamanho A6 ou similar)
    largura, altura = 800, 1200
    imagem = Image.new('RGB', (largura, altura), color='white')
    draw = ImageDraw.Draw(imagem)
    
    # Tentar carregar uma fonte, senão usa a padrão
    try:
        fonte_titulo = ImageFont.truetype("arial.ttf", 40)
        fonte_texto = ImageFont.truetype("arial.ttf", 25)
    except:
        fonte_titulo = ImageFont.load_default()
        fonte_texto = ImageFont.load_default()

    # Desenhar Cabeçalho 
    draw.rectangle([0, 0, largura, 100], fill="#2c3e50")
    draw.text((20, 30), "AUTORIZAÇÕES E HABILITAÇÕES", fill="white", font=fonte_titulo)

    # Processar Foto do Colaborador
    if foto_upload:
        foto = Image.open(foto_upload).convert("RGBA")
        foto = foto.resize((200, 250))
        imagem.paste(foto, (50, 150), foto if foto.mode == 'RGBA' else None)

    # Dados Pessoais (Lado Direito da Foto) 
    draw.text((300, 150), f"NOME: {dados['nome']}", fill="black", font=fonte_texto)
    draw.text((300, 200), f"CPF: {dados['cpf']}", fill="black", font=fonte_texto)
    draw.text((300, 250), f"EMPRESA: {dados['empresa']}", fill="black", font=fonte_texto)
    draw.text((300, 300), f"FUNÇÃO: {dados['funcao']}", fill="black", font=fonte_texto)

    # Tabela de Equipamentos e Processos (Baseado no modelo )
    draw.rectangle([20, 450, 780, 490], fill="#ecf0f1")
    draw.text((30, 460), "EQUIPAMENTOS / PROCESSOS", fill="black", font=fonte_texto)
    draw.text((600, 460), "VALIDADE", fill="black", font=fonte_texto)

    y_offset = 500
    processos = [
        ("ASO", dados['aso']),
        ("Teste de Direção", dados['direcao']),
        ("NR10", dados['nr10']),
        ("NR35", dados['nr35']),
        ("Validade Geral", dados['validade_geral'])
    ]

    for label, valor in processos:
        draw.text((30, y_offset), label, fill="black", font=fonte_texto)
        draw.text((600, y_offset), valor, fill="black", font=fonte_texto)
        y_offset += 40

    return imagem

# --- INTERFACE DO USUÁRIO ---
st.title("🪪 Sistema Automatizado de Crachás")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dados do Colaborador")
    nome = st.text_input("Nome Completo")
    cpf = st.text_input("CPF")
    empresa = st.text_input("Nome da Empresa")
    funcao = st.text_input("Cargo/Função")
    foto = st.file_uploader("Foto do Colaborador", type=["jpg", "png"])

with col2:
    st.subheader("Validações e NRs ")
    aso = st.text_input("Validade ASO", "01/01/2026")
    direcao = st.text_input("Teste de Direção", "01/01/2026")
    nr10 = st.text_input("NR10", "01/01/2026")
    nr35 = st.text_input("NR35", "01/01/2026")
    validade_geral = st.text_input("Validade Geral", "01/01/2026")

if st.button("GERAR CRACHÁ AUTOMÁTICO"):
    if nome and foto:
        dados = {
            "nome": nome, "cpf": cpf, "empresa": empresa, 
            "funcao": funcao, "aso": aso, "direcao": direcao,
            "nr10": nr10, "nr35": nr35, "validade_geral": validade_geral
        }
        
        img_final = gerar_imagem_cracha(dados, foto)
        st.image(img_final, caption="Prévia do Crachá Gerado", use_container_width=True)
        
        # Preparar download
        buf = io.BytesIO()
        img_final.save(buf, format="PNG")
        st.download_button("Baixar Crachá (PNG)", buf.getvalue(), f"cracha_{nome}.png", "image/png")
    else:
        st.warning("Preencha o Nome e carregue uma Foto!")
