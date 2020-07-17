def buscar_setor(matriz,x):
    x = []
    for i in matriz:
        if (i[2] == x):
            novo = i.copy()
            novo.remove(x)
            x.apppend(novo)
    return x

def aposentadoria(deposito,taxa,idade_inicial,idade_final):
    tempo_total = (idade_final) - (idade_inicial)
    taxa_01 = taxa/100
    valor_acumulado = deposito * ((1 + taxa_01)**tempo_total)
    return valor_acumulado
    
