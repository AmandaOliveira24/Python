import pandas as pd
from openpyxl import load_workbook

clientes = [ 
    { "nome": "Ana Clara Martins", "email": "ana.martins@email.com", "telefone": "11991234567", "data_nascimento": "12/03/1990"},
    {"nome": "Carlos Henrique Lima", "email": "carlos.lima@email.com", "telefone": "21993456789", "data_nascimento": "08/07/1985"},
    {"nome": "Juliana Sousa Reis", "email": "juliana.reis@email.com", "telefone": "31998887766", "data_nascimento": "25/11/1992"},
    {"nome": "Felipe Andrade Rocha", "email": "felipe.rocha@email.com", "telefone": "11994561234", "data_nascimento": "03/09/1988"},
    {"nome": "Larissa Gomes Vieira", "email": "larissa.vieira@email.com", "telefone": "21990011223", "data_nascimento": "30/01/1995"},
    {"nome": "Bruno Fereira Costa", "email": "bruno.costa@email.com", "telefone": "11997885644", "data_nascimento": "14/06/1991"},
    {"nome": "Patrícia Melo Cardoso", "email": "patricia.cardoso@email.com", "telefone": "31992334455", "data_nascimento": "22/12/1987"},
    {"nome": "Ricardo Alves Pinto", "email": "ricardo.pinto@email.com", "telefone": "21991112233", "data_nascimento": "09/04/1983"},
    {"nome": "Marina Duarte Lopes", "email": "marina.lopes@email.com", "telefone": "31991112233", "data_nascimento": "17/08/1996"},
    {"nome": "Diego Ribeiro Teixeira", "email": "diego.teixeira@email.com", "telefone": "11993216548", "data_nascimento": "05/10/1989"},
]

# Criar um DataFrame com pandas
df = pd.DataFrame(clientes)

# Exportar para um arquivo Excel
df.to_excel(r"C:\Users\DBA_Nanda\Desktop\lista.2\clientes.xlsx", index=False)

# Agora, ajustando o tamanho das colunas
wb = load_workbook(r"C:\Users\DBA_Nanda\Desktop\lista.2\clientes.xlsx")  # Corrigido
ws = wb.active

wb.save(r"C:\Users\DBA_Nanda\Desktop\lista.2\clientes_ajustado.xlsx")  # Corrigido


# Ajustar largura das colunas automaticamente
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter  # Obter a letra da coluna
    
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    
    adjusted_width = (max_length + 2)  # Adicionando um pequeno espaço extra
    ws.column_dimensions[column].width = adjusted_width

# Salvar o arquivo com a formatação
wb.save(r"C:\Users\DBA_Nanda\Desktop\lista.2\clientes_ajustado.xlsx")







