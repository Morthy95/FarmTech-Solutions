# pacotes
if(!require(httr)) install.packages("httr", repos = "http://cran.rstudio.com/")
if(!require(jsonlite)) install.packages("jsonlite", repos = "http://cran.rstudio.com/")

library(httr)
library(jsonlite)

# sua chave da API
api_key <- "1c1f7f0c4397691d0fb61368dced9507"

# --- pegar cidade ---
args <- commandArgs(trailingOnly = TRUE)

if (length(args) > 0) {
  cidade <- args[1]
} else {
  cidade <- readline("Digite a cidade (ex.: Sao Paulo, Curitiba, Porto Alegre): ")
}

cidade <- trimws(cidade)

# --- montar URL ---
url <- paste0(
  "https://api.openweathermap.org/data/2.5/weather?q=",
  URLencode(cidade),
  "&appid=", api_key,
  "&units=metric&lang=pt_br"
)

# --- chamar API ---
res <- GET(url)

if (status_code(res) == 200) {
  dados <- content(res, as = "parsed", encoding = "UTF-8")
  
  cat("\n=== Clima em", cidade, "===\n")
  cat("🌡️ Temperatura:", dados$main$temp, "°C\n")
  cat("😊 Sensação:", dados$main$feels_like, "°C\n")
  cat("💧 Umidade:", dados$main$humidity, "%\n")
  cat("🌬️ Vento:", dados$wind$speed, "m/s\n")
  cat("☁️ Condição:", dados$weather[[1]]$description, "\n")
  
} else {
  cat("❌ Erro na requisição.\n")
  cat("HTTP status:", status_code(res), "\n")
  cat("URL chamada:", url, "\n")
  cat("Corpo retornado:\n", content(res, "text", encoding = "UTF-8"), "\n")
}
