import math
from .storage import add_area, list_all, update, delete

def inserir_tomate(comprimento: float, largura: float) -> float:
    area = comprimento * largura
    add_area("tomate", area)
    return area

def inserir_soja(raio: float) -> float:
    area = math.pi * (raio ** 2)
    add_area("soja", area)
    return area

def listar():
    return list_all()

def atualizar(cultura: str, idx: int, novo_valor: float):
    update(cultura, idx, novo_valor)

def deletar(cultura: str, idx: int):
    delete(cultura, idx)