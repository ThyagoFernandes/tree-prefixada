from treeprefix import*
alfa = "abcdefghijklmnopqrstuvxyz"
raiz  = node(0,None,alfa)
print("insercao de palavras")
arv= tree(raiz,alfa)
arv.inserir_palavra("amorosamente")
arv.inserir_palavra("amorosamente")
assert arv.encontrar_palavra("amorosamente") == True
arv.inserir_palavra("amor")
arv.inserir_palavra("amido")
assert arv.encontrar_palavra("amido") == True
arv.inserir_palavra("kamel0")
assert arv.encontrar_palavra("kamel0") == False
arv.inserir_palavra("lombo")
arv.inserir_palavra("lombard")
print("o vetor que contem o no "+ str(arv.nos))
assert arv.encontrar_palavra("luffy") == False
assert arv.encontrar_palavra("lombo") == True
assert arv.remover("lombar") == False
assert arv.encontrar_palavra("amor") == True
assert arv.remover("amor")
assert arv.encontrar_palavra("amido")  == True
assert arv.remover("amido") == True
assert arv.encontrar_palavra("amido") == False
assert arv.encontrar_palavra("amor") == False
print("o vetor que contem o no "+ str(arv.nos))


