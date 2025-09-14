# FarmTech Solutions — FIAP  

Aplicação em **Python** e **R** para apoiar a Agricultura Digital com duas culturas: **Tomate** e **Soja**.  

---

## Objetivos  
- Calcular área de plantio por cultura.  
- Calcular manejo de insumos (dose por metro, ruas de plantio, litros totais).  
- Manipular dados em vetores e operar via menu no Python.  
- Exportar dados em CSV para análise em R.  
- Em R: calcular média, desvio padrão, mínimo e máximo.  
- (Extra) Usar API meteorológica pública para mostrar o clima.  

---

## Culturas e Geometria  
- Tomate → talhão retangular (área = comprimento × largura)  
- Soja → talhão circular (área = π × raio²)  

---

## Tecnologias  
- Python 3.10+  
- R 4.3+ (pacotes httr, jsonlite)  
- Git/GitHub  

---

## Estrutura do Projeto  
- `/python` → código Python (main.py)  
- `/r` → código R (analise.R)  
- `/docs` → resumo.pdf e video.txt  
- `README.md`  

---

## Workflow de Branches  
- **main** → versão estável, pronta para entrega.  
- **dev** → integração antes de mandar pra main.  
- **feature/...** → branches de funcionalidades (ex.: `feature/python-menu`).  

### Convenção de commits  
- `feat:` → nova funcionalidade  
- `fix:` → correção  
- `docs:` → documentação  
- `chore:` → configuração/manutenção  

Exemplo:  
