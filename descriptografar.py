import os
import pyaes

# Nome do arquivo criptografado
file_name = "teste2025.txt.criptografado2025"

# Abre o arquivo criptografado em modo de leitura binária
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave para descriptografia (deve ter 16, 24 ou 32 bytes)
key = b"ransomwares2025b"
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografa os dados do arquivo
decrypt_data = aes.decrypt(file_data)

# Remove o arquivo criptografado
os.remove(file_name)

# Nome do novo arquivo descriptografado
new_file_name = "teste2025.txt"

# Salva os dados descriptografados em um novo arquivo
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypt_data)

# Exibe uma mensagem de sucesso ao descriptografar o arquivo
print(f"Arquivo {new_file_name} descriptografado com sucesso!"