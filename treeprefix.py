class tree:
	def __init__(self,r,alfabeto):
		self.raiz = r
		self.nos = [r]
		self.alfabeto = alfabeto
	def inserir_palavra(self, palavra):
		no_atual = 0
		palavra = palavra.lower() 
		print("")
		print("palavra a ser inserida "+ palavra)
		print("")
		for c in palavra:
			if(c not in self.alfabeto ):
				print("a palavra "+palavra+" possui caracteres que nao esta no alfabeto "+ self.alfabeto)
				print("")
				return None

		for ch in palavra:
			if(self.nos[no_atual].filhos[ch] is not None):
				print("no atual "+ str(self.nos[no_atual])+" ha filho "+ch+" logo "+ ch+ " eh o no atual")
				no_atual = self.nos[no_atual].filhos[ch]
			else:
				print("no atual "+ str(self.nos[no_atual])+" nao ha filho "+ch)
				print("criando o no "+ ch+" setando o seu pai como "+ str(self.nos[no_atual]))
				no = node(ch,no_atual,self.alfabeto)
				self.nos[no_atual].setfilho(ch,len(self.nos))
				no_atual = len(self.nos)
				self.nos.append(no)
		self.nos[no_atual].ehultimo_ch = True
		print("inserido com sucesso\n")

	def encontrar_palavra(self,palavra):
		no_atual = 0
		palavra = palavra.lower()
		for ch in palavra:
			if(ch in self.alfabeto):
				print("no ataul "+str(self.nos[no_atual])+" proximo no "+ch)
				if(self.nos[no_atual].filhos[ch] is not None):
					no_atual = self.nos[no_atual].filhos[ch]
				else:
					print("o no atual "+str(self.nos[no_atual])+" nao possui filho "+ ch )
					print("palavra "+palavra+" nao encontrada")
					return False
			else:
				print("essa palavra possui caracteres fora do alfabeto (-->"+ch+"<--)")
				return False

		if(self.nos[no_atual].ehultimo_ch  == False):
			print("palavra "+palavra+" nao encontrada pois "+str(self.nos[no_atual])+ " nao eh terminal")
			return False
		print("palavra "+palavra+" encontrada")
		return True

	def remover(self,palavra):
		no_atual = 0
		palavra = palavra.lower()
		for ch in palavra:
			print("no ataul "+str(self.nos[no_atual])+" proximo no "+ch)
			if(ch in self.alfabeto):		
				if(self.nos[no_atual].filhos[ch] is not None):
					no_atual = self.nos[no_atual].filhos[ch]
			else:
				print("essa palavra possui caracteres fora do alfabeto (-->"+ch+"<--), logo ele nunca estara nesta arvore")
				return False	
		if(self.nos[no_atual].efolha() == False):
		    if(self.nos[no_atual].ehultimo_ch ):
		        self.nos[no_atual].ehultimo_ch = False
		        print("removendo "+ palavra)
		        return None
		    else:
		        print("palavra "+ palavra+" nao encontrada, logo nao pode ser removida")
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

	def __init__(self,valor,pai, alfabeto):
		self.valor = valor
		self.pai = pai
		self.alfabeto = alfabeto
		self.filhos = dict()
		self.ehultimo_ch = False
		self.criar_filhos()
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
		self.filhos[no.valor] = None
	def criar_filhos(self):
		for ch in self.alfabeto :
			self.filhos[ch] = None
	
	def efolha(self):
		for ch in self.alfabeto :
			#print("o caractere"+ch+" esta? "+str(self.filhos[ch] is None))
			if(self.filhos[ch] is not None):
				return False
		return True	
	def __repr__(self):
		return str(self.valor)
