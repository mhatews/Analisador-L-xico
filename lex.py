import ply.lex as lex
import tkinter as tk
from tkinter import filedialog

# Define os nomes dos tokens
tokens = [
'tipo',
'inteiro',
'real',
'cadeia_car',
'para',
'se',
'senao',
'enquanto',
'escreva',
'leia'
]

# Define as expressões regulares para cada token
T_tipo = r'^(int|real|texto|bool)$'
T_inteiro = r'^[+-]?\d+$'
T_real = r'^-?\d+(\.\d+)?$'
T_cadeia_car = r'^".*"$'
T_para = r'^para$'
T_se = r'^se$'
T_senao = r'^senao$'
T_enquanto = r'^enquanto$'
T_escreva = r'^escreva$'
T_leia = r'^leia$'



# Define o tratamento de erros
def t_error(t):
    print(f"Erro: caracter inválido '{t.value[0]}'")
    t.lexer.skip(1)

# Cria o analisador léxico
lexer = lex.lex()

# Define a função para analisar o texto
def analyze_text():
    input_string = text_input.get('1.0', tk.END)
    tokenize(input_string)

# Define a função para exibir os tokens
def tokenize(input_string):
    output_string = ''
    lexer.input(input_string)
    for token in lexer:
        output_string += str(token) + '\n'
    text_output.configure(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.insert('1.0', output_string)
    text_output.configure(state='disabled')

# Define a função para abrir o arquivo
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as f:
            file_contents = f.read()
        text_input.delete('1.0', tk.END)
        text_input.insert('1.0', file_contents)
        analyze_text()

# Cria a janela principal da interface gráfica
root = tk.Tk()

# Cria um botão para abrir o arquivo
button_open = tk.Button(root, text='Abrir arquivo', command=open_file)
button_open.pack()

# Cria um campo para digitar o texto
text_input = tk.Text(root)
text_input.pack()

# Cria um botão para analisar o texto
button_analyze = tk.Button(root, text='Analisar', command=analyze_text)
button_analyze.pack()

# Cria um campo para exibir o resultado
text_output = tk.Text(root, state='disabled')
text_output.pack()

# Inicia a interface gráfica
root.mainloop()