class Empregado:
    def __init__(self,nome,salario):  #sem dicionario aqui
        self.nome    = nome
        self.salario = salario
    def set_nome(self,novoNome):  #set é metodo que ALTERA o valor do parametro, logo, precisa ter um novo parametro dentro dos ()
        self.nome = novoNome
    def set_salario(self,novoValor):
        self.salario = novoValor

class Gerente(Empregado):  #entre () é a superclasse
    def __init__(self,bonificacao,nome,salario):
        Empregado.__init__(self,nome,salario)   #se chamar direto precisa do self
        #super().__init__(nome,salario)
        self.bonificacao = bonificacao #atributo exclusivo do gerente
    def get_salario(self):  #get só mostra o valor do self.salario (return), nao altera
        return self.salario

class Vendedor(Empregado):
    def __init__(self,comissao,nome,salario):
        super().__init__(nome,salario)  #nao importa se o self.comissao vem antes ou depois do super
        self.comissao = comissao
    def get_salario(self):
        return self.salario

class GerenteVendas(Gerente,Vendedor):
    def __init__(self,nome,salario,bonificacao,comissao,**D): #nome e salario de Empregado| bonificacao do Gerente | comissao do Vendedor| DICIONARIO para fazer as listas gerentes e vendedores
        Gerente.__init__(self,bonificacao,nome,salario)
        super().__init__(comissao,nome,salario)
        self.gerentes = []  #LISTA
        if 'gerentes' in D:     # ve se a lista gerentes foi inserida no dicionario pelo usuario - SEMPRE ESSES PASSOS!
            for x in D['gerentes']:
                self.gerentes.append(x)
        self.vendedores = []
        if 'vendedores' in D:
            for x in D['vendedores']:
                self.vendedores.append(x)
    def get_gerentes(self):
        return self.gerentes
    def add_gerente(self,novoGerente):
        if novoGerente not in self.gerentes: #verifica se esse novoGerente já nao está na lista self.gerentes
            self.gerentes.append(novoGerente)
    def get_vendedores(self):
        return self.vendedores
    def add_vendedor(self,novoVendedor):
        if novoVendedor not in self.vendedores:
            self.vendedores.append(novoVendedor)

gen1 = Gerente(50,'Luiz de Souza',1500) #ordem = bonificacao,nome,salario
gen2 = Gerente(200,'Marcelo Prado',1500)
ven1 = Vendedor(300,'Mario Borges',1500) #comissao,nome,salario
ven2 = Vendedor(50,'Carlos Cornélio',1500)

#b)
somaGen = gen1.salario + gen1.bonificacao + gen2.get_salario() + gen2.bonificacao

somaVen = ven1.salario + ven1.comissao + ven2.salario + ven2.comissao

print(f'A diferença entre as classe é de R$', abs(somaGen-somaVen))
#print(f'A diferença entre as classe é de R${abs(somaGen-somaVen)}')

#c) e d):
gv1 = GerenteVendas('Rove',1500,150,50,gerentes=[gen1],vendedores=[ven2]) #declara as listas gerentes e vendedores com []
gv2 = GerenteVendas('Arnaldo',1500,150,50,gerentes=[gen2],vendedores=[ven1])

#e)

gerVend = [gv1,gv2] #pode colocar um unico for para todos os gv
for gv in gerVend: #gv vai assumir no 1º for gv1 e tudo que ta associado a ele e depois gv2
    somag = 0
    for g in gv.gerentes:
        somag += g.get_salario() + g.bonificacao
    somav = 0
    for v in gv.vendedores:
        somav += v.salario + v.comissao
    quantos = len(gv.get_gerentes()) + len(gv.get_vendedores()) #quantidade de ger e vend
    media = (somag+somav) / quantos
    valorGV = gv.salario + gv.bonificacao + gv.comissao

    print(f'A diferença entre o recebido pelo GV e a media dos supervisionados é {abs(valorGV-media)}')










