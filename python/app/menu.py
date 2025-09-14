from . import operations as op

def run_menu():
    while True:
        print("\n=== FarmTech Solutions (Python) ===")
        print("1) Inserir dados")
        print("2) Listar dados")
        print("3) Atualizar por índice")
        print("4) Deletar por índice")
        print("5) Gerar relatório CSV")
        print("0) Sair")
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1": inserir()
            case "2": listar()
            case "3": atualizar()
            case "4": deletar()
            case "5": op.exportar_csv()  # Nova opção para exportar CSV
            case "0":
                print("Saindo... até logo!")
                break
            case _: print("Opção inválida.")

def inserir():
    print("\n=== Inserir ===")
    cultura = input("1=Tomate | 2=Soja: ").strip()
    if cultura == "1":
        c = float(input("Comprimento (m): "))
        l = float(input("Largura (m): "))
        area = op.inserir_tomate(c, l)
        print(f"Área registrada (Tomate): {area:.2f} m²")
    elif cultura == "2":
        r = float(input("Raio (m): "))
        area = op.inserir_soja(r)
        print(f"Área registrada (Soja): {area:.2f} m²")
    else:
        print("Cultura não listada.")

def listar():
    print("\n=== Listar ===")
    dados = op.listar()

    print("Tomate:")
    for i, area in enumerate(dados['tomate']):
        print(f"  [{i}] {area:.2f} m²")

    print("Soja:")
    for i, area in enumerate(dados['soja']):
        print(f"  [{i}] {area:.2f} m²")
        
def atualizar():
    print("\n=== Atualizar ===")
    cultura = input("tomate/soja: ").strip().lower()
    if cultura not in ["tomate", "soja"]:
        print("⚠️ Cultura inválida.")
        return
    idx = int(input("Índice: "))
    novo = float(input("Novo valor de área (m²): "))
    try:
        op.atualizar(cultura, idx, novo)
        print("✅ Atualizado com sucesso.")
    except IndexError:
        print("⚠️ Índice inválido.")


def deletar():
    print("\n=== Deletar ===")
    cultura = input("tomate/soja: ").strip().lower()
    if cultura not in ["tomate", "soja"]:
        print("⚠️ Cultura inválida.")
        return
    idx = int(input("Índice: "))
    try:
        op.deletar(cultura, idx)
        print("✅ Deletado com sucesso.")
    except IndexError:
        print("⚠️ Índice inválido.")