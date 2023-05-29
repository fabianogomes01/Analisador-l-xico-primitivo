import re

def lexical_analyzer(input_str):
    # Verifica se a entrada é composta apenas de caracteres permitidos
    if not re.match(r'^[a-zA-Z0-9_@\#\!\(\)\[\]\{\}\-\+\*\/\%\^\\\|\&\.\,\?\:\"\']+$', input_str):
        return "Entrada inválida: use apenas caracteres permitidos."

    # Divide a entrada em tokens separados por espaços em branco
    tokens = input_str.split()

    # Limita a lista de tokens aos 10 primeiros
    tokens = tokens[:10]

    # Verifica se a entrada excede o tamanho máximo permitido
    if len(tokens) != len(input_str.split()):
        return "Entrada inválida: a entrada não pode exceder 10 caracteres."

    # Verifica se a entrada contém palavras iniciadas com números
    if re.match(r'^\d\w*$', input_str):
        return "Entrada inválida: palavras iniciadas com números são reservadas pelo sistema."

    # Verifica se a entrada contém uma expressão matemática com x, y, z, t ou w
    if re.search(r'[xyztw][\+\-\*/\(\)\[\]\{\}@#\!\d_]*[xyztw]', input_str):
        return "A entrada contém uma expressão matemática."

    # A entrada é considerada válida se todas as condições acima forem falsas
    return "Entrada válida."

# Exemplo de uso:
input_str = input("Digite uma entrada: ")
result = lexical_analyzer(input_str)
print(result)
