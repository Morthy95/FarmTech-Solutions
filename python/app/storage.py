# Armazena os dados em memória
dados = {
    "tomate": [],
    "soja": []
}

def add_area(cultura: str, area: float):
    cultura = cultura.lower()
    if cultura not in dados:
        raise ValueError("Cultura não listada (use 'tomate' ou 'soja').")
    dados[cultura].append(area)

def list_all():
    return {k: v[:] for k, v in dados.items()}  # retorna cópia

def update(cultura: str, idx: int, novo_valor: float):
    dados[cultura][idx] = novo_valor

def delete(cultura: str, idx: int):
    dados[cultura].pop(idx)