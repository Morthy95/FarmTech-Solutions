import datetime
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
    
def exportar_csv(nome_base: str = "plantio") -> None:

    """Exporta os dados das culturas para um arquivo CSV com timestamp no nome."""
    timestamp = datetime.datetime.now().strftime("%d%m%Y-%H%M")
    filepath = f"data/{nome_base}-{timestamp}.csv"
    
    # Garante que a pasta existe
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["cultura", "area"])  # Cabeçalho

        for cultura, areas in dados.items():
            for area in areas:
                writer.writerow([cultura, area])

    print(f"✅ Dados exportados com sucesso para {filepath}")

def calcular_insumos(cultura: str, produto: str, dose_por_m2: float) -> float:
    """
    Calcula a quantidade total de insumo necessária para uma cultura.
    - cultura: 'tomate' ou 'soja'
    - produto: nome do insumo (ex: 'fertilizante X')
    - dose_por_m2: litros ou mL por metro quadrado
    """
   
    areas = dados.get(cultura, [])
    if not areas:
        print(f"⚠️ Nenhuma área cadastrada para {cultura}.")
        return 0.0

    total_area = sum(areas)
    total_insumo = total_area * dose_por_m2

    print(f"➡️ Cultura: {cultura}")
    print(f"➡️ Produto: {produto}")
    print(f"➡️ Área total: {total_area:.2f} m²")
    print(f"➡️ Dose aplicada: {dose_por_m2} L/m²")
    print(f"✅ Quantidade necessária: {total_insumo:.2f} L de {produto}")

    return total_insumo