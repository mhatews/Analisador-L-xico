error_list = [
    {
        "error": "STR_INCOMPLETA",
        "msg": "String mal formada " 
    },

    {
        "error": "VAR_ERRO",
        "msg": "Variavel mal formada " 
    },

    {
        "error": "NUM_ERRO",
        "msg": "Número mal formado " 
    },

    {
        "error": "INTEIRO",
        "msg": "Entrada maior que a suportada " 
    }
]

def get_error(type, value):

    for err in error_list:

        if type == err:

            error_message = err.msg

            return error_message
        
        else:

            continue