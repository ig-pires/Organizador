import os
import shutil

cam=r'C:\Users\Pires\Desktop'
tiposdearquivos= {
    'Imagens':['.jpg','.jpeg','.png','.gif'],
    'Documentos':['.pdf','.docx','.txt'],
    'Compactados':['.zip','.rar'],
    'Executáveis':['.exe','.msi'],
    'Vídeos':['.mp4','.mov','.avi','.mp3']
}
for arquivo in os.listdir(cam):
    nomecompleto=os.path.join(cam, arquivo)
    if os.path.isfile(nomecompleto):
        nome, extensao=os.path.splitext(arquivo)
        for pasta, extensoes in tiposdearquivos.items():
            if extensao.lower() in extensoes:
                pastadestino=os.path.join(cam,pasta)
                if not os.path.exists(pastadestino):
                    os.mkdir(pastadestino)
                shutil.move(nomecompleto,os.path.join(pastadestino,arquivo))
                print('Movido: {} >> {}'.format(arquivo, pasta))
