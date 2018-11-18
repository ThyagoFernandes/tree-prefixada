class tree:
	def __init__(self,r):
		self.raiz = r
		self.nos = [r]
	def inserir_palavra(self, palavra):
		no_atual = 0
		palavra = palavra.lower()
		for ch in palavra:
			if(ch in self.nos[no_atual].filhos.keys()):
				no_atual = self.nos[no_atual].filhos[ch]
			else:
				no = node(ch,no_atual)
				self.nos[no_atual].setfilho(ch,len(self.nos))
				no_atual = len(self.nos)
				self.nos.append(no)
		self.nos[no_atual].ehultimo_ch = True

	def encontrar_palavra(self,palavra):
		no_atual = 0
		palavra = palavra.lower()
		for ch in palavra:
			if(ch in self.nos[no_atual].filhos.keys()):
				no_atual = self.nos[no_atual].filhos[ch]
			else:
				return False
		if(self.nos[no_atual].ehultimo_ch  == False):
		    return False
		return True

	def remover(self,palavra):
		no_atual = 0
		palavra = palavra.lower()
		for ch in palavra:		
			if(ch in self.nos[no_atual].filhos.keys()):
				no_atual = self.nos[no_atual].filhos[ch]
		print(self.nos)
		if(self.nos[no_atual].efolha() == False):
		    if(self.nos[no_atual].ehultimo_ch ):
		        self.nos[no_atual].ehultimo_ch = False
		        print("removendo "+ palavra)
		        return None
		    else:
		        print("palavra "+ palavra+" nao encontrada")
		        return None
		print("removendo "+ palavra)      
		while(self.nos[no_atual].efolha()):
			aux = self.nos[no_atual].pai
			self.nos[self.nos[no_atual].pai].removefilho(self.nos[no_atual])
			del self.nos[no_atual]
			no_atual = aux


	def __repr__(self):
		return "Test()"
	def __str__(self):
		return "arvore " + str(self.raiz.valor)


class node:

	def __init__(self,valor,pai):
		self.valor = valor
		self.pai = pai
		self.filhos = dict()
		self.ehultimo_ch = False
	@property	
	def pai(self):
		return self._pai
	@pai.setter
	def pai(self,no):
		self._pai = no
	@property
	def valor(self):
		return self._valor
	@valor.setter
	def valor(self,valor):
		self._valor = valor
	def setfilho(self,ch, index):
		self.filhos[ch] = index

	def removefilho(self,no):
		self.filhos.pop(no.valor)
	
	def efolha(self):
		return len(self.filhos) == 0
	def __repr__(self):
		return str(self.valor)

raiz  = node(0,None)
arv= tree(raiz)
arv.inserir_palavra("lu")
arv.inserir_palavra("Luf")
arv.inserir_palavra("nami")
arv.inserir_palavra("luffy")
arv.inserir_palavra("zoro")
arv.inserir_palavra("lombard")
print("encontrado "+str(arv.encontrar_palavra("lu")))
arv.remover("lombard")
arv.remover("lu")
print("encontrado "+str(arv.encontrar_palavra("lu")))
print(arv.nos)

