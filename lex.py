import ply.lex as lex
import tkinter as tk
from tkinter import filedialog

# Define os nomes dos tokens
tokens = [
    'TIPO',
    'INTEIRO',
    'REAL',
    'CADEIA_CAR',
    'PARA',
    'SE',
    'SENAO',
    'ENQUANTO',
    'ESCREVA',
    'LEIA'
]

# Expressões regulares para cada token
t_TIPO = r'int|real|texto|bool'
t_INTEIRO = r'([+-])?\d+'
t_REAL = r'-?\d+(.\d+)?'
t_CADEIA_CAR = r'".*?"'
t_PARA = r'para'
t_SE = r'se'
t_SENAO = r'senao'
t_ENQUANTO = r'enquanto'
t_ESCREVA = r'escreva'
t_LEIA = r'leia'

# Ignora espaços em branco e tabulações
t_ignore = ' \t'

# Ignora comentários
def t_COMMENT(t):
    r'\/\/.*'
    pass

# Tratamento de erros
def t_error(t):
    print("Caractere inválido '%s'" % t.value[0])
    t.lexer.skip(1)

# Cria o analisador léxico
lexer = lex.lex()

def analyze_text():
    input_string = text_input.get('1.0', tk.END)
    tokenize(input_string)

# Define a função para exibir os tokens
def tokenize(input_string):
    output_string = ''
    lexer.input(input_string)
    for token in lexer:
        output_string += 'Token: {}, valor: {}, linha: {}, coluna: {}\n'.format(token.type, token.value, token.lineno, token.lexpos - input_string.rfind("\n", 0, token.lexpos))
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
text_output = tk.Text(root, state='normal')
text_output.pack()

# Inicia a interface gráfica
root.mainloop()