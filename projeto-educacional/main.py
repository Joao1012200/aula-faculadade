import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time


# Questão com imagem
questao = {
    "imagem": r"C:\Users\vinny\PycharmProjects\PythonProject\projeto-educacional\questao.png",
    "opcoes": [
        {"texto": "Afirmação 01", "correta": True},
        {"texto": "Afirmação 02", "correta": True},
        {"texto": "Afirmação 04", "correta": False},
        {"texto": "Afirmação 08", "correta": False},
        {"texto": "Afirmação 16", "correta": False},
        {"texto": "Afirmação 32", "correta": False},
        {"texto": "Afirmação 64", "correta": True}
    ]
}

tempo_inicio = None


def verificar_resposta():
    global tempo_inicio
    selecionadas = []
    for i, var in enumerate(vars_opcoes):
        if var.get() == 1:
            selecionadas.append(i)

    correto = True
    for i, opcao in enumerate(questao["opcoes"]):
        if opcao["correta"] and i not in selecionadas:
            correto = False
        if not opcao["correta"] and i in selecionadas:
            correto = False

    # Calcula tempo gasto
    tempo_fim = time.time()
    tempo_total = tempo_fim - tempo_inicio

    if correto:
        messagebox.showinfo("Resultado", f"✅ Resposta correta!\nTempo gasto: {tempo_total:.2f} segundos")
    else:
        messagebox.showerror("Resultado", f"❌ Resposta incorreta.\nTempo gasto: {tempo_total:.2f} segundos")

# Criando janela
janela = tk.Tk()
janela.title("Quiz com Imagem")

# Mostrar imagem da questão
img = Image.open(questao["imagem"])
img = img.resize((600, 400))  # ajusta tamanho
foto = ImageTk.PhotoImage(img)

imagem_label = tk.Label(janela, image=foto)
imagem_label.pack(pady=10)

# Criar opções
vars_opcoes = []
for opcao in questao["opcoes"]:
    var = tk.IntVar()
    chk = tk.Checkbutton(janela, text=opcao["texto"], variable=var, wraplength=600, justify="left")
    chk.pack(anchor="w")
    vars_opcoes.append(var)

botao = tk.Button(janela, text="Confirmar", command=verificar_resposta)
botao.pack(pady=20)

tempo_inicio = time.time()

janela.mainloop()
