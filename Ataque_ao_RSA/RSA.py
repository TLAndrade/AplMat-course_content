import numpy


############################################################################
#        FUNÇÕES PARA A EXECUÇÃO DO ALGORITMO RSA                          #
############################################################################


def dict_codificador():
    preCodificador = {"A" : "101",
                  "B" : "102",
                  "C" : "103",
                  "D" : "104",
                  "E" : "105",
                  "F" : "106",
                  "G" : "107",
                  "H" : "108",
                  "I" : "109", 
                  "J" : "110",
                  "K" : "111",
                  "L" : "112",
                  "M" : "113",
                  "N" : "114",
                  "O" : "115",
                  "P" : "116",
                  "Q" : "117",
                  "R" : "118",
                  "S" : "119", 
                  "T" : "120",
                  "U" : "121",
                  "V" : "122",
                  "W" : "123",
                  "X" : "124",
                  "Y" : "125",
                  "Z" : "126",
                  "0" : "127",
                  "1" : "128",
                  "2" : "129",
                  "3" : "130",
                  "4" : "131",
                  "5" : "132",
                  "6" : "133",
                  "7" : "134",
                  "8" : "135",
                  "9" : "136",
                  "a" : "137",
                  "b" : "138",
                  "c" : "139",
                  "d" : "140",
                  "e" : "141",
                  "f" : "142",
                  "g" : "143",
                  "h" : "144",
                  "i" : "145",
                  "j" : "146",
                  "k" : "147",
                  "l" : "148",
                  "m" : "149",
                  "n" : "150",
                  "o" : "151",
                  "p" : "152",
                  "q" : "153",
                  "r" : "154",
                  "s" : "155",
                  "t" : "156",
                  "u" : "157",
                  "v" : "158",
                  "w" : "159",
                  "x" : "160",
                  "y" : "161",
                  "z" : "162",
                  "." : "163",
                  "," : "164",
                  ":" : "165",
                  ";" : "166",
                  "<" : "167",
                  ">" : "168",
                  "?" : "169",
                  "/" : "170",
                  "°" : "171",
                  "º" : "172",
                  "{" : "173",
                  "}" : "174",
                  "[" : "175",
                  "]" : "176",
                  "ª" : "177",
                  "´" : "178",
                  "`" : "179",
                  "^" : "180",
                  "~" : "181",
                  "(" : "182",
                  ")" : "183",
                  "*" : "184",
                  "&" : "185",
                  "¨" : "186",
                  "%" : "187",
                  "$" : "188",
                  "#" : "189",
                  "@" : "190",
                  "!" : "191",
                  '"' : "192",
                  "\\" : "193",
                  "|" : "194",
                  "'" : "195",
                  "¹" : "196",
                  "²" : "197",
                  "³" : "198",
                  "£" : "199",
                  "¢" : "201",
                  "¬" : "202",
                  "-" : "203",
                  "_" : "204",
                  "+" : "205",
                  "=" : "206",
                  "§" : "207",
                  "ç" : "208",
                  "á" : "209",
                  "à" : "210",
                  "â" : "211",
                  "ã" : "212",
                  "é" : "213",
                  "è" : "214",
                  "ê" : "215",
                  "í" : "216",
                  "ì" : "217",
                  "î" : "218",
                  "ó" : "219",
                  "ò" : "220",
                  "ô" : "221",
                  "õ" : "222",
                  "ú" : "223",
                  "ù" : "224",
                  "û" : "225",
                  "Á" : "226",
                  "À" : "227",
                  "Â" : "228",
                  "Ã" : "229",
                  "É" : "230",
                  "È" : "231",
                  "Ê" : "232",
                  "Í" : "233",
                  "Ì" : "234",
                  "Î" : "235",
                  "Ó" : "236",
                  "Ò" : "237",
                  "Ô" : "238",
                  "Õ" : "239",
                  "Ú" : "240",
                  "Ù" : "241",
                  "Û" : "242",
                  " " : "999"}
    key = list(preCodificador.values())
    values = list(preCodificador.keys())
    posDecodificador = dict(zip(key,values))
    return preCodificador,posDecodificador


def vars():
    #definindo as chaves de codificação
    p = input("Digite o valor de p: \n")
    p = int(p)
    q = input("Digite o valor de q: \n")
    q = int(q)
    e = input("Digite o valor de e: \n")
    n = int(p)*int(q)
    e = int(e)
    print('\033[1m' + '\n Então a chave de codificação é ')
    print('\033[1m' + 'n :',n)
    print('\033[1m' + 'e :',e)
    return(p,q,e,n)

#PreCodificando a Mensagem
def preCodficador(mensagem):
    mensagemPreCod = ""
    for i in mensagem:
        mensagemPreCod += preCodificador[i]
    return(mensagemPreCod)
        
    
#Quebrando a mensagem em blocos
def separaBlocos(mensagemPreCod,n):
    blocos = []
    digitos_n = len(str(n))
    bloco_inicio = 0
    bloco_fim = 0
    while bloco_fim < len(mensagemPreCod):
        aux = numpy.random.randint(1,digitos_n+1)
        bloco_fim = min(bloco_fim+aux, len(mensagemPreCod)-1)
        while int(mensagemPreCod[bloco_inicio:bloco_fim+1]) >= n:
            bloco_fim = bloco_inicio
            aux = numpy.random.randint(1,digitos_n+1)
            bloco_fim = min(bloco_fim+aux, len(mensagemPreCod)-1)
        if mensagemPreCod[bloco_fim] == "0":
            if mensagemPreCod[bloco_fim-1] == "0":
                if mensagemPreCod[bloco_inicio:bloco_fim-2] != "":
                    blocos.append(mensagemPreCod[bloco_inicio:bloco_fim-2])
                    blocos.append(mensagemPreCod[bloco_fim-2:bloco_fim+1])
                else:
                    blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+1])
                bloco_inicio = bloco_fim+1
            elif bloco_fim+1 < len(mensagemPreCod):
                if mensagemPreCod[bloco_fim+1] == "0":
                    if mensagemPreCod[bloco_inicio:bloco_fim-1] != "":
                        blocos.append(mensagemPreCod[bloco_inicio:bloco_fim-1])
                        blocos.append(mensagemPreCod[bloco_fim-1:bloco_fim+2])
                    else:
                        blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+2])
                    bloco_inicio = bloco_fim+2
                else:
                    if mensagemPreCod[bloco_inicio:bloco_fim-1] != "":
                        blocos.append(mensagemPreCod[bloco_inicio:bloco_fim-1])
                        blocos.append(mensagemPreCod[bloco_fim-1:bloco_fim+1])
                    else:
                        blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+1])
                    bloco_inicio = bloco_fim+1
            else:
                if mensagemPreCod[bloco_inicio:bloco_fim-1] != "":
                    blocos.append(mensagemPreCod[bloco_inicio:bloco_fim-1])
                    blocos.append(mensagemPreCod[bloco_fim-1:bloco_fim+1])
                else:
                    blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+1])
                bloco_inicio = bloco_fim+1
        elif bloco_fim+2 < len(mensagemPreCod):
            if mensagemPreCod[bloco_fim+2] == "0":
                if mensagemPreCod[bloco_fim+1] == "0":
                    if mensagemPreCod[bloco_inicio:bloco_fim] != "":
                        blocos.append(mensagemPreCod[bloco_inicio:bloco_fim])
                        blocos.append(mensagemPreCod[bloco_fim:bloco_fim+3])
                    else:
                        blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+3])
                    bloco_inicio = bloco_fim+3
                else:
                    blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+1])
                    bloco_inicio = bloco_fim+1
            else:
                if mensagemPreCod[bloco_fim+1] == "0":
                    if mensagemPreCod[bloco_inicio:bloco_fim] != "":
                        blocos.append(mensagemPreCod[bloco_inicio:bloco_fim])
                        blocos.append(mensagemPreCod[bloco_fim:bloco_fim+2])
                    else:
                        blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+2])
                    bloco_inicio = bloco_fim+2
                else:
                    blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+1])
                    bloco_inicio = bloco_fim+1
        elif bloco_fim + 1 < len(mensagemPreCod):
            if mensagemPreCod[bloco_fim+1] == "0":
                if mensagemPreCod[bloco_inicio:bloco_fim] != "":
                    blocos.append(mensagemPreCod[bloco_inicio:bloco_fim])
                    blocos.append(mensagemPreCod[bloco_fim:bloco_fim+2])
                else:
                    blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+2])
                bloco_inicio = bloco_fim+2
            else:
                blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+1])
                bloco_inicio = bloco_fim+1
        else:
            blocos.append(mensagemPreCod[bloco_inicio:bloco_fim+1])
            bloco_inicio = bloco_fim+1
        bloco_fim = bloco_inicio
    return(blocos)
    
    
# Entrada: inteiros x, e, n
# Saída: P (o módulo de x^e por n, ou seja, o resto da divisão de x^e por n)
def algoritmoExponenciacao(x,e,n):
    A = x
    P = 1
    E = e
    while E != 0:
        if E%2 == 1:
            P = (A*P)%n
            E = (E-1)/2
        else:
            E = E/2
        A = (A**2)%n
    return P

#Codificando os blocos da lista b usando a chave de codificação (n,e)
def codificadorBlocos(b,e,n):
    b2 =[]
    for i in b:
        b2.append(algoritmoExponenciacao(int(i),e,n))
    return(b2)

#PreCodificando a Mensagem
def preCodficador(mensagem,preCodificador):
    mensagemPreCod = ""
    for i in mensagem:
        mensagemPreCod += preCodificador[i]
    return(mensagemPreCod)

def cripto_RSA(mensagem,preCodificador):
    #define a chave 
    p,q,e,n = vars()
    mensagemPreCod = preCodficador(mensagem,preCodificador)
    #Quebrando a mensagem original em blocos
    blocosPreCod = separaBlocos(mensagemPreCod,n)
    #Codificando os blocos
    blocosCod = codificadorBlocos(blocosPreCod,e,n)
    return(blocosCod,p,q,e,n)
    
############################################################################
#                    CODIFICAÇÃO/DECODIFICAÇÃO                             #
############################################################################
# Decodificando os blocos da lista b usando a chave de decodificação (d,n)


def algoritmoExponenciacao(x,e,n):
    A = x
    P = 1
    E = e
    while E != 0:
        if E%2 == 1:
            P = (A*P)%n
            E = (E-1)/2
        else:
            E = E/2
        A = (A**2)%n
    return P


#Passa no dicionário posDecodificador
def dict_decodificador(m,posDecodificador):
    mensagem = ""
    for i in m:
        try:
            mensagem += posDecodificador[str(i)]
        except:
            mensagem += "*"
    return mensagem

#Decodificando os blocos da lista b usando a chave de decodificação (d,n)
def decodificadorBlocos(m,d,n):
    b2 =[]
    for i in m:
        b2.append(str(algoritmoExponenciacao(int(i),d,n)))
    return(b2)

def decodificador(m,d,n,posDecodificador):
    b = decodificadorBlocos(m,d,n)
    separador = ""
    mensagemPosDecod = separador.join(b)
    mensagemDecod = ""
    for i in range(0,int(len(mensagemPosDecod)/3)):
        try:
            mensagemDecod += posDecodificador[mensagemPosDecod[int(3*i):int(3*i+3)]]
        except:
            mensagemDecod += "*"
    return mensagemDecod


############################################################################
#            FUNÇÕES AUXILIARES PARA O ATAQUE AO RSA                       #
############################################################################

#Algoritmo de Euclides Extendido
# Entradas:
#    a = (p-1)*(q-1)
#    e: expoente
# Saídas:
#    mdc(a,e)
#    x
#    y
#    a*x+e*y = 1

def EuclidesEstendido(a,e):
    mdc, x, y = EuclidesAuxiliar(a, e)
    if y < 0:
        y = a + y
        x = x - e
    return mdc, x, y

def EuclidesAuxiliar(a, e):  
    if a == 0 :   
        return e, 0, 1
    mdc, x1, y1 = EuclidesAuxiliar(e%a, a)  
    x = y1 - (e//a) * x1  
    y = x1  #valor de interesse
    return mdc, x, y 
        
