import ply.lex as lex
import tkinter as tk
from tkinter import filedialog

errors = []


reserved = {
    'se': 'SE',
    'senao': 'SENAO',
    'enquanto': 'ENQUANTO',
    'leia': 'LEIA',
    'escreva': 'ESCREVA',
    'para': 'PARA',
    'funk': 'FUNK',
    'retorna': 'RETORNA',
    'ifsuldeminas': 'IFSULDEMINAS',
    'inicio': 'INICIO',
    'compiladores': 'COMPILADORES',
    'fim': 'FIM',
    'int': 'INT',
    'real': 'REAL',
    'bool': 'BOOLEANO',
    'texto': 'TEXTO',
}

# Define os nomes dos tokens
tokens = [
    'VAR',
    'TIPO',
    'INTEIRO',
    'REAL',
    'CADEIA_CAR',
    'PARA',
    'SE',
    'SENAO',
    'ENQUANTO',
    'ESCREVA',
    'LEIA',
    'ABRE_COLCH',
    'FECHA_COLCH',
    'ABRE_CHAV',
    'FECHA_CHAV',
    'VIRG',
    'PONTO_VIRG',
    'ABRE_PAR',
    'FECHA_PAR',
    'OPER_RELA',
    'OPER_MAT',
    'ITERADORES',
    'NEGACAO',
    'OPER_LOG',
    'FUNK',
    'NOME_FUNK',
    'RETORNO',
    'STR_INCOMPLETA',
    'VAR_ERRO',
    'NUM_ERRO',
]+ list(reserved.values())

# Expressões regulares para cada token
t_VAR = r'([a-zA-Z_]+)\d*\w*'
t_INTEIRO = r'([+-])?\d+'
t_REAL = r'(([+-])?\d+)[.]\d+'
t_CADEIA_CAR = r'"[^"]*"'
t_ABRE_COLCH = r'\['
t_FECHA_COLCH = r'\]'
t_ABRE_CHAV = r'{'
t_FECHA_CHAV = r'}'
t_VIRG = r','
t_PONTO_VIRG = r';'
t_ABRE_PAR = r'\('
t_FECHA_PAR = r'\)'
t_OPER_RELA = r'(=|==|!=|<=|>=|<|>)'
t_OPER_MAT = r'(\+|\-|\*|\/|\%)'
t_ITERADORES = r'(ate|passo)'
t_NEGACAO = r'!'
t_OPER_LOG = r'(&&|\|\|)'
t_NOME_FUNK = r'[a-zA-Z_]\w*[ ][(].*?[)]'
t_STR_INCOMPLETA = r'"[^"]*'
t_VAR_ERRO = r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
t_NUM_ERRO= r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'

# Ignora espaços em branco e tabulações
t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')  # verifica se é uma palavra reservada
    return t

# Ignora comentários
def t_COMMENT(t):
    r'\/\/\#.*'
    pass


def analyze_text():
    global errors
    input_string = text_input.get('1.0', tk.END)
    if errors:
        errors = []
    tokenize(input_string)
    
# Tratamento de erros
def t_error(t):
    last_newline_index = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
    line = t.lexer.lineno
    column = t.lexpos - last_newline_index
    error_message = f"Linha {line}, Coluna {column}: Caracter Invalido {t.value[0]!r}"
    errors.append(error_message)
    t.lexer.skip(1)
 



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Cria o analisador léxico
lexer = lex.lex()



# Define a função para exibir os tokens
def tokenize(input_string):
    output_string = ''
    lexer.input(input_string)
    num_lines = input_string.count('\n')
    for token in lexer:
        output_string += 'Token: {}, valor: {}, linha: {}, coluna: {}\n'.format(token.type, token.value, token.lineno, token.lexpos - input_string.rfind("\n", 0, token.lexpos))

        if token.type == "STR_INCOMPLETA":
            error_message = f"String Mal formada {token.value!r}"
            errors.append(error_message)
        if token.type == "VAR_ERRO":
            error_message = f"Variavel Mal formada {token.value!r}"
            errors.append(error_message)
        if token.type == "NUM_ERRO":
            error_message = f"Número Mal formada {token.value!r}"
            errors.append(error_message)
        if token.type == "INTEIRO":
            max = (len(str(token.value)))
            if (max < 200):
                error_message = f"Entrada maior que a suportada"
                errors.append(error_message)
                
    output_string += f'\nNúmero de linhas: {num_lines}'
    error_message = lexer.token()
    text_output.configure(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.insert('1.0', output_string)
    if errors:
        text_output.insert(tk.END, "\n\nErros encontrados:\n")
        for error in errors:
            text_output.insert(tk.END, error + "\n")
    text_output.configure(state='disabled')
    lexer.lineno = 1
    print(errors)
    


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
text_output = tk.Text(root, state='disable')
text_output.pack()

# Inicia a interface gráfica
root.mainloop()