#!/usr/bin/env python3

import os
import glob
#pip install glob2==0.4.1
import zipfile

dir_name_base = os.path.dirname(os.path.realpath(__file__))
print(dir_name_base)

#Descompactar arquivo
def unzipefile():
    dir_name_base = os.path.dirname(os.path.realpath(__file__))
    
    for arc_name in glob.iglob(os.path.join(dir_name_base, "*.zip")):
        arc_dir_name = os.path.splitext(os.path.basename(arc_name))[0]
        zf = zipfile.ZipFile(arc_name)
        zf.extractall(path=os.path.join(dir_name_base, arc_dir_name))
        zf.close() # close file after extraction is completed'''


#Não é para remover porque o arquivo vai baixar tudo novamente.
#_________________________________________________Removendo arquivos zipados_______________________________
def delzip():
    dir_name_base = os.path.dirname(os.path.realpath(__file__))
    test = os.listdir(dir_name_base)

    for arc_name in test:
        if arc_name.endswith(".zip"):
            os.remove(os.path.join(dir_name_base, arc_name))






