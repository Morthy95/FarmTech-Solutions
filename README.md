# 🌱 FarmTech Solutions

Projeto acadêmico FIAP – Aplicação em Python e R para Agricultura Digital (Tomate e Soja).  
Objetivo: desenvolver uma solução que auxilia no cálculo de áreas, manejo de insumos, análise estatística e consulta climática.

---

## 🚀 Funcionalidades

- **Python**
  - Inserir áreas de cultivo (Tomate → Retângulo, Soja → Círculo)
  - Listar registros com índices
  - Atualizar registros por índice
  - Deletar registros por índice
  - Exportar dados para CSV
  - Calcular insumos (produto x dose aplicada por m²)
  - Consultar clima (API OpenWeatherMap)

- **R**
  - Leitura do CSV exportado pelo Python
  - Cálculo de estatísticas: média, desvio padrão, mínimo, máximo
  - Exportação de relatórios estatísticos
  - Consulta climática via API (mesma chave utilizada pelo Python)

---

## 📦 Pré-requisitos

- **Python 3.11+**
  - Não requer bibliotecas externas

- **R 4.3+**
  - Pacotes: `httr`, `jsonlite`

Instalar pacotes no R (caso necessário):

```R
  install.packages("httr")
  install.packages("jsonlite")
```

▶️ Como rodar
```
  py python/main.py
```

R - Estatísticas
```
  Rscript r/analise.R
```
  R - Clima
  ```
  Rscript r/clima.R "Sao Paulo"
```
  _Ou via menu do Python (opção 7 - Consultar clima)._

📂 Estrutura de pastas
```
FarmTech-Solutions/
│
├── python/
│   ├── app/           # módulos de lógica (menu, operações, storage)
│   ├── data/          # relatórios exportados em CSV
│   └── main.py        # menu principal
│
├── r/
│   ├── analise.R      # análise estatística
│   ├── clima.R        # consulta de clima via API
│   └── relatorio_*    # relatórios estatísticos
│
└── README.md
```
📊 Exemplo de Saída

```
Estatísticas por Cultura (R)
===== Estatísticas por cultura =====
  cultura media desvio minimo maximo n
1    soja 58.64  50.79   12.57   113.1 3
2  tomate 36.67  12.01   25.00    49.0 3
```
Clima (Python ou R)
```
=== Consulta Climática ===
Digite a cidade: Sao Paulo

🌡️ Temperatura: 22.3 ºC
😊 Sensação: 23.1 ºC
💧 Umidade: 78 %
💨 Vento: 3.4 m/s
☁️ Condição: nublado
```
Gabriel Peter Ferreira
Grupo: FarmTech Solutions

FIAP – Inteligência Artificial / Agricultura Digital

📹 Demonstração em Vídeo
Link do vídeo (não listado no YouTube):
👉 link_aqui

