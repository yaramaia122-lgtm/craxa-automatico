import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from tkinter import filedialog, messagebox
 
class GeradorCracha:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Gerador de Crachás - Aura Apoena")
        self.root.geometry("500x700")
        # Variáveis de controle
        self.caminho_foto = ""
        # Interface - Campos de Texto
        self.criar_campo("Nome Completo:", "entry_nome")
        self.criar_campo("CPF:", "entry_cpf")
        self.criar_campo("Empresa:", "entry_empresa")
        self.criar_campo("Gerência:", "entry_gerencia")
        self.criar_campo("Função:", "entry_funcao")
        self.criar_campo("Treinamentos (Ex: NR10: 01/01/2026, NR35: 02/02/2026):", "entry_nrs")
 
        # Botão para Foto
        self.btn_foto = ctk.CTkButton(self.root, text="Carregar Foto", command=self.selecionar_foto)
        self.btn_foto.pack(pady=10)
 
        # Botão Gerar
        self.btn_gerar = ctk.CTkButton(self.root, text="GERAR CRACHÁ", fg_color="green", command=self.processar_cracha)
        self.btn_gerar.pack(pady=20)
 
    def criar_campo(self, label_text, var_name):
        label = ctk.CTkLabel(self.root, text=label_text)
        label.pack(pady=(10, 0))
        entry = ctk.CTkEntry(self.root, width=300)
        entry.pack()
        setattr(self, var_name, entry)
 
    def selecionar_foto(self):
        self.caminho_foto = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png")])
        if self.caminho_foto:
            messagebox.showinfo("Sucesso", "Foto carregada!")
 
    def processar_cracha(self):
        # Aqui entra a lógica de desenho na imagem (Pillow)
        # 1. Abre o template 
        # 2. Escreve Nome, CPF, Empresa, Gerência, Função 
        # 3. Filtra os treinamentos digitados (só escreve se a data for futura)
        # 4. Salva o PNG
        messagebox.showinfo("Sucesso", "Crachá gerado na pasta /CRACHAS")
 
if __name__ == "__main__":
    app = GeradorCracha()
    app.root.mainloop()
