from treeprefix import*
alfa = "abcdefghijklmnopqrstuvxyz"
raiz  = node(0,None,alfa)
print("insercao de palavras")
arv= tree(raiz,alfa)
arv.inserir_palavra("amorosamente")
arv.inserir_palavra("amor")
arv.inserir_palavra("amido")
arv.inserir_palavra("kamel0")
arv.inserir_palavra("lombo")
arv.inserir_palavra("lombard")
print("o vetor que contem o no "+ str(arv.nos))
arv.encontrar_palavra("luffy")
arv.encontrar_palavra("lombo")
arv.remover("lombar")
arv.encontrar_palavra("amor")
arv.remover("amor")
arv.encontrar_palavra("amido")
arv.remover("amido")
arv.encontrar_palavra("amido")
arv.encontrar_palavra("amor")
print("o vetor que contem o no "+ str(arv.nos))


