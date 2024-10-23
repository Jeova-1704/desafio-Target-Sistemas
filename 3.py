import json

def calcular_faturamento(dados):
    
    faturamento_diario = [float(valor) for dia in dados["faturamento"].values() for valor in dia if valor > 0]
    
    if not faturamento_diario:
        return {
            "menor_faturamento": 0,
            "maior_faturamento": 0,
            "media_faturamento": 0,
            "qtd_dias_faturamento_acima_media": 0
        }
    
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    media_faturamento = sum(faturamento_diario) / len(faturamento_diario)
    
    qtd_dias_faturamento_acima_media = len([valor for valor in faturamento_diario if valor > media_faturamento])
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "media_faturamento": media_faturamento,
        "qtd_dias_faturamento_acima_media": qtd_dias_faturamento_acima_media
    }
    
if __name__ == "__main__":
    with open("faturamento.json") as file:
        dados = json.load(file)
        
    resultado = calcular_faturamento(dados)
    
    print(resultado)
