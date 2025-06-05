import os


lista_documentos = os.listdir('PASTA/documentos')
print(lista_documentos)

# print(lista_arquivos[5])

# # os.rename("arquivos/abr22.txt", "arquivos/22/abr22.txt")

for documentos in lista_documentos:
    if 'documento' in documentos:
         if '.docx' in documentos:
            os.rename(f"C:\\Users\\DBA_Nanda\\Desktop\\python\\PASTA\\documentos\\{documentos}", f"C:\\Users\\DBA_Nanda\\Desktop\\python\\PASTA\\documentos\\word\\{documentos}")
         elif '.xlsx' in documentos:
            os.rename(f"C:\\Users\\DBA_Nanda\\Desktop\\python\\PASTA\\documentos\\{documentos}", f"C:\\Users\\DBA_Nanda\\Desktop\\python\\PASTA\\documentos\\excel\\{documentos}")
         else:
             os.rename(f"C:\\Users\\DBA_Nanda\\Desktop\\python\\PASTA\\documentos\\{documentos}", f"C:\\Users\\DBA_Nanda\\Desktop\\python\\PASTA\\documentos\\powerpoint\\{documentos}")

#modificando

#modificando para outra atividade









