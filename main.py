import sys

# -*- coding: utf-8 -*-
class TrieNode:
    def __init__(self,idn=0,l=None):
        self.Letra=l
        self.idx=idn
        self.filhos=[]

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.next_idx=1
        self.dict=[]
        self.dict.append(['',0])
        self.max_int=0
    def search(self, word):
        current = self.root
        for char in word:
            busca = [x for x in current.filhos if x.Letra == char]
            if (len(busca) == 0):
                return current
            else:
                current = busca[0]
        return current

    def insert(self, word):
        curr=self.root
        for char in word:
            busca = [x for x in curr.filhos if x.Letra == char]
            if len(busca): curr=busca[0]
            else:
                to_ins=TrieNode(self.next_idx,char)
                curr.filhos.append(to_ins)
                self.next_idx+=1
                self.dict.append([char,curr.idx])
                if(curr.idx>self.max_int):self.max_int=curr.idx
                curr=self.root
#######################################################################################3
def read_recur(dicionario,idx):
    if dicionario[idx][0]=='': return ''
    else:return read_recur(dicionario,dicionario[idx][1]) + dicionario[idx][0]

def decompress(dicionario):
    txt=''
    for i in dicionario[1:]:
      temp=read_recur(dicionario,i[1])
      temp+=i[0]
      txt +=temp
    return txt
#################################################################################################

def to_bin(dicionario,out_file):
    for i in dicionario:
        if(i[0]!=''):
            char = i[0].encode('utf-16-be')
            num = i[1].to_bytes(2, byteorder='big')
            out_file.write(char)
            out_file.write(num)
#################################################################################################
def from_bin(in_file):
    dicionario = []
    dicionario.append(["",0])
    while True:
        # Lê um caractere de 4 bytes e um inteiro de 2 bytes do arquivo
        char_bytes = in_file.read(2)
        if not char_bytes:
            # Fim do arquivo
            break
        int_bytes = in_file.read(2)

        # Decodifica o caractere bytes
        char = char_bytes.decode('utf-16-be')

        # Converte os bytes inteiros para um inteiro Python
        num = int.from_bytes(int_bytes, byteorder='big')

        dicionario.append((char, num))

    return dicionario
######################################################
entradas= sys.argv
operacao=entradas[1]
arquivo_in=''
arquivo_out=''
if(operacao=='-c'):
	arquivo_in = entradas[2]
	if(len(entradas)>3 and entradas[3]=='-o'): arquivo_out=entradas[4]
		
	else:
		arquivo_out=entradas[2][:-3]
		arquivo_out+='z78'
elif(operacao=='-d'):
	arquivo_in = entradas[2]
	if(len(entradas)>3 and entradas[3]=='-o'):arquivo_out=entradas[4]
		
	else:
		arquivo_out=entradas[2][:-3]
		arquivo_out+='txt'
		
if(operacao=='-c'):
	arq=open(arquivo_in,"r")
	texto=arq.read()
	trie=Trie()
	trie.insert(texto)

	saida=open(arquivo_out,'wb')
	to_bin(trie.dict,saida)			
		
elif(operacao=='-d'):
	arq=open(arquivo_in,"rb")
	dict=from_bin(arq)
	txt=decompress(dict)
	saida=open(arquivo_out,'w')
	saida.write(txt)
	
	
	
	
	

