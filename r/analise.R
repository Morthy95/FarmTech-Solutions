# r/analise.R
# Leitura do CSV gerado pelo Python e estatísticas básicas por cultura

# --- 0) Detectar o arquivo de entrada mais recente
files <- Sys.glob("data/plantio-*.csv")  # pega todos os plantio-*.csv
if (length(files) == 0) {
  stop("Nenhum CSV encontrado em python/data/. Rode o Python e use a opção 5 (Gerar relatório CSV).")
}

csv_in <- files[which.max(file.info(files)$mtime)]  # escolhe o mais novo
cat("Lendo arquivo:", csv_in, "\n")

# Caminho de saída do relatório em R (com timestamp também, se quiser)
csv_out <- paste0("r/relatorio_estatisticas-",
                  format(Sys.time(), "%d%m%Y-%H%M"), ".csv")

# --- 1) Ler dados
dados <- read.csv(csv_in, stringsAsFactors = FALSE)

# --- 2) Sanitização simples
# garantir nomes esperados e tipos
names(dados) <- tolower(names(dados))
if (!all(c("cultura", "area") %in% names(dados))) {
  stop("CSV deve conter colunas: cultura, area")
}
dados$cultura <- tolower(trimws(dados$cultura))
dados$area <- as.numeric(dados$area)
dados <- dados[is.finite(dados$area) & dados$area > 0, ]

# --- 3) Estatísticas por cultura (base R)
estat <- aggregate(area ~ cultura, data = dados, FUN = function(x) c(
  media = mean(x),
  desvio = sd(x),
  minimo = min(x),
  maximo = max(x),
  n      = length(x)
))

# 'estat$area' veio como matriz; desdobra em colunas
estat_final <- data.frame(
  cultura = estat$cultura,
  media   = round(estat$area[, "media"], 2),
  desvio  = round(estat$area[, "desvio"], 2),
  minimo  = round(estat$area[, "minimo"], 2),
  maximo  = round(estat$area[, "maximo"], 2),
  n       = estat$area[, "n"]
)
# --- 4) Salvar e exibir
timestamp <- format(Sys.time(), "%d%m%Y-%H%M")   # gera ddMMyyyy-HHmm
csv_out <- paste0("r/relatorio-", timestamp, ".csv")

dir.create("r", showWarnings = FALSE)
write.csv(estat_final, csv_out, row.names = FALSE)

cat("\n===== Estatísticas por cultura =====\n")
print(estat_final)
cat("\n✅ Relatório salvo em:", csv_out, "\n")