# 🌱 FarmTech Solutions

Projeto acadêmico FIAP – Aplicação em **Python** e **R** para Agricultura Digital (Tomate e Soja).

---

## 📌 Funcionalidades

### Python
- Inserir dados de plantio (área em m² para Tomate ou Soja)
- Listar dados cadastrados
- Atualizar dados por índice
- Deletar dados por índice
- Exportar relatório CSV com timestamp automático (`data/plantio-AAAAMMDD-HHMM.csv`)
- Calcular insumos (ex.: fertilizantes, herbicidas, etc.) com base em dose por m²
- **Consultar clima** 🌤️ (API OpenWeather integrada via script R)

### R
- Estatísticas básicas por cultura a partir do CSV exportado pelo Python:
  - Média
  - Desvio padrão
  - Mínimo
  - Máximo
- Geração de relatórios estatísticos (`r/relatorio-AAAAMMDD-HHMM.csv`)
- Consulta de clima em tempo real via API OpenWeather (`r/clima.R`)

---

## ⚙️ Pré-requisitos

- **Python 3.10+**
  - Bibliotecas nativas
- **R 4.2+**
  - Pacotes: `httr`, `jsonlite`

---

## ▶️ Como rodar

### Python
```bash
# Executar menu principal
python python/main.py
