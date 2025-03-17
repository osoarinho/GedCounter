# Código desenvolvido por:
# Lucas Soares dos Santos (@adevcalledlucas no Instagram)
# Destinado à Prefeitura Municipal de Angra dos Reis
# Código aberto - Uso livre
# Criado com dedicação para agilizar uma das etapas da fiscalização de GED por meio de automação.

import os
import pandas as pd
from PyPDF2 import PdfReader
import re
import tkinter as tk
from tkinter import filedialog
import subprocess
import sys

def abrir_terminal():

    if sys.stdout is None:
        subprocess.Popen(["cmd", "/K", f'python "{sys.argv[0]}"'], creationflags=subprocess.CREATE_NEW_CONSOLE)
        sys.exit()

def contar_paginas(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        paginas = len(reader.pages)
        print(f"📄 {pdf_path}: {paginas} páginas")
        return paginas
    except Exception as e:
        print(f"⚠️ Erro ao contar páginas em {pdf_path}: {e}")
        return 0

def listar_pdfs(dia_path):
    pdfs = [os.path.join(root, file)
            for root, _, files in os.walk(dia_path)
            for file in files if file.lower().endswith(".pdf")]
    return pdfs

def processar_pasta(mes_path):
    dados = []
    padrao_data = re.compile(r".*(\d{1,2}[-_/]\d{1,2}[-_/]\d{2,4}).*")

    print("\n🔄 Iniciando o processamento...\n")

    for dia in sorted(os.listdir(mes_path)):
        if not padrao_data.match(dia):
            continue

        dia_path = os.path.join(mes_path, dia)
        if os.path.isdir(dia_path):
            total_paginas = 0
            pdfs = listar_pdfs(dia_path)
            total_arquivos = len(pdfs)

            print(f"📂 Processando o dia: {dia}")
            for pdf_path in pdfs:
                total_paginas += contar_paginas(pdf_path)

            paginas_reais = total_paginas - total_arquivos
            print(f"✅ Dia {dia}: {total_paginas} páginas - {total_arquivos} arquivos - {paginas_reais} páginas reais")
            dados.append([dia, total_paginas, total_arquivos, paginas_reais])

    return pd.DataFrame(dados, columns=["Dia", "Páginas Totais", "Arquivos PDF", "Páginas Encontradas"])

def main():
    try:
        abrir_terminal()

        print("🔹 Iniciando o programa...")


        root = tk.Tk()
        root.withdraw()
        print("🔹 Selecione a pasta...")


        mes_path = filedialog.askdirectory(title="Selecione a pasta que deseja processar")


        if not mes_path:
            print("\n⚠️ Nenhuma pasta selecionada. O programa foi encerrado.")
            input("\n🔚 Pressione Enter para sair...")
            return

        print(f"\n📂 Pasta selecionada: {mes_path}")

        output_excel = os.path.join(mes_path, "Relatorio_Conferido.xlsx")


        print("🔹 Iniciando o processamento da pasta...")
        df_encontrado = processar_pasta(mes_path)


        df_encontrado.to_excel(output_excel, index=False)


        print(f"\n✅ Relatório gerado com sucesso em: {output_excel}")

    except Exception as e:
        print(f"\n🚨 Ocorreu um erro: {e}")

    finally:

        print("\n📢 Desenvolvido por Lucas Soares dos Santos (@adevcalledlucas no Instagram)")
        input("\n🔚 Pressione Enter para sair...")

if __name__ == "__main__":
    main()
