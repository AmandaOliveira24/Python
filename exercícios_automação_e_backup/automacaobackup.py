import os
import shutil
from datetime import datetime

# Caminho do "banco de dados" (pode ser .csv, .txt, .json, etc.)
arquivo_origem = 'lista.xlsx'  # Substitua pelo nome correto, se necessário

# Pasta onde os backups serão salvos
pasta_backups = 'backups'

# 1. Verifica se o arquivo original existe
if not os.path.exists(arquivo_origem):
    print(f"Arquivo '{arquivo_origem}' não encontrado.")
    exit(1)

# 2. Cria a pasta de backups se não existir
os.makedirs(pasta_backups, exist_ok=True)

# 3. Gera o nome do backup com data e hora
agora = datetime.now()
timestamp = agora.strftime("%Y-%m-%d_%H-%M")
nome_backup = f"{os.path.splitext(arquivo_origem)[0]}_backup_{timestamp}{os.path.splitext(arquivo_origem)[1]}"
caminho_backup = os.path.join(pasta_backups, nome_backup)

# 4. Copia o arquivo original para a pasta de backups
shutil.copy2(arquivo_origem, caminho_backup)

# 5. Remove backups antigos (mantém apenas os 5 mais recentes)
# Lista todos os arquivos de backup relacionados
backups = [f for f in os.listdir(pasta_backups) if f.startswith(os.path.splitext(arquivo_origem)[0])]
# Ordena por data de modificação (mais recentes por último)
backups.sort(key=lambda x: os.path.getmtime(os.path.join(pasta_backups, x)))

# Remove os mais antigos se houver mais de 5
while len(backups) > 5:
    arquivo_antigo = backups.pop(0)
    os.remove(os.path.join(pasta_backups, arquivo_antigo))

# 6. Mensagem final
print(f"Backup realizado com sucesso: {nome_backup}")



#modificando

#modificando para outra atividade











