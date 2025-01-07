def process_queue_operations(input_str):
    queue = []  # Lista que funciona como fila
    result = []  # Lista para armazenar o resultado final

    for char in input_str:
        if char == '*':  # Operação de dequeue
            if queue:
                result.append(queue.pop(0))  # Remove o primeiro da fila
        else:  # Operação de enqueue
            queue.append(char)  # Adiciona o caractere à fila
    
    return ''.join(result)  # Junta o resultado como string

# Testes com os exemplos fornecidos
inputs = [
    "ola*** mundo",
    "c > python***",
    "rir***, o breve****** e verb******o *rir****"
]

for input_str in inputs:
    print(process_queue_operations(input_str))
