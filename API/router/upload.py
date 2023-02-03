from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from starlette.status import HTTP_201_CREATED, HTTP_200_OK
from typing import List
import os
from os.path import join 
import zipfile

upload = APIRouter(prefix="/api/upload",
                   responses={404:{"message": "No encontrado"}})

@upload.post("/{id}")
async def upload_file(id: str, files: List[UploadFile] = File(...)):
    
        newpath = r"d:/archivos/" + str(id) + "/"
             
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            
        for file in files:
            try:
                contents = file.file.read()
                with open(newpath + file.filename, "wb") as myfile:    
                    myfile.write(contents)
        
            except Exception:
                return {"message": "Hubo un error al subir el archivo"}
            finally:
                file.file.close()
        return ('Success')




#@upload.post("/{id}")
#async def upload_file(id: str, file: UploadFile = File(...)):
    
#        newpath = r"d:/archivos/" + str(id) + "/"
                 
#        if not os.path.exists(newpath):
#            os.makedirs(newpath)
    
    
#        with open(newpath + file.filename, "wb") as myfile:
#            content = await file.read()
#            myfile.write(content)
#            myfile.close
#        return ('Success')
    
@upload.get("/{id}", response_class=FileResponse, status_code=HTTP_201_CREATED)
async def files(id: str):

        newpath = "d:/archivos/" + str(id) + "/"
        
        zip = zipfile.ZipFile(str(id)+'.zip', 'w')
        
        for archivo in os.listdir(newpath):
            
            #zip.write('D:/Proyectos Python/backendAeroclub/API/Zip/'(newpath,archivo))
            zip.write(os.path.join(newpath,archivo))
        
        zip.close()
        
        #return ('Success')
        return FileResponse( path='D:/Proyectos Python/backendAeroclub/API/'+str(id)+'.zip', filename=str(id)+'.zip')