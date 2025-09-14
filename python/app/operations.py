import math
from .storage import add_area, list_all, update, delete
import csv
import os
from app.storage import dados

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
    
def exportar_csv(filepath: str = "data/plantio.csv") -> None:
    """Exporta os dados das culturas para um arquivo CSV."""
    
    # Garante que a pasta existe
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["cultura", "area"])  # Cabeçalho

        for cultura, areas in dados.items():
            for area in areas:
                writer.writerow([cultura, area])

    print(f"✅ Dados exportados com sucesso para {filepath}")