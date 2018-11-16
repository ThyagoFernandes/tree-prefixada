class tree:
	def __init__(self,r):
		self.raiz = r
		self.nos = [r]
	def inserir_palavra(self, palavra):
		no_atual = 0
		for ch in palavra:
			print(palavra+" "+str(self.nos[no_atual])+ " "+ str(self.nos[no_atual].filhos))
			if(ch in self.nos[no_atual].filhos.keys()):
				no_atual = self.nos[no_atual].filhos[ch]
			else:
				no = node(ch,no_atual)
				no.pai = no_atual
				self.nos[no_atual].setfilho(ch,len(self.nos))
				no_atual = len(self.nos)
				self.nos.append(no)

		print(self.nos)
	def encontrar_palavra(self,palavra):
		no_atual = 0	
		for ch in palavra:
			if(ch in self.nos[no_atual].filhos.keys()):
				print("achei "+ ch + " em "+ str(self.nos[no_atual] ))
				no_atual = self.nos[no_atual].filhos[ch]
			else:
				return False
		return True

	def remover(self,palavra):
		no_atual = 0
		cont  = 1	
		for ch in palavra:		
			if(ch in self.nos[no_atual].filhos.keys()):
				no_atual = self.nos[no_atual].filhos[ch]
		print(str(self.nos[no_atual])+str(self.nos[no_atual].efolha()))
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
		print(str(self.filhos)+"fff")
	
	def efolha(self):
		print(str(self.valor) + str(len(self.filhos)))
		return len(self.filhos) == 0
	def __repr__(self):
		return str(self.valor)

raiz  = node(0,None)
arv= tree(raiz)
arv.inserir_palavra("lu")
arv.inserir_palavra("luf")
arv.inserir_palavra("nami")
arv.inserir_palavra("luffy")
arv.inserir_palavra("zoro")
arv.inserir_palavra("lombard")
print(arv.encontrar_palavra("lombard"))
arv.remover("nami")
print(arv.nos)




