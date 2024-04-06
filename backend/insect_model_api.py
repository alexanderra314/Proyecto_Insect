import os
import torch
from enum import Enum, auto
from pathlib import Path
import typing
from abc import ABC
from fastapi import FastAPI, HTTPException, UploadFile, File, APIRouter, Request
from fastapi.responses import JSONResponse
from models import InsectModel, Framework
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/predict")
async def predict_insect(request: Request, file: UploadFile = File(...)):
  
    # Verificar si se envió algún archivo
    if not file:
        raise HTTPException(status_code=400, detail="No se ha proporcionado ninguna imagen")
    if not file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise HTTPException(status_code=422, detail="El archivo debe estar en formato JPEG, JPG o PNG")

    #file_extension = file.filename.split('.')[-1]
    file_extension = Path(file.filename).suffix

    temp_file_path = f"temp{file_extension}"
    print("Ruta del archivo temporal:", temp_file_path)


    try:

        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(file.file.read())
        logger.info("Archivo temporal creado:", temp_file_path)
        # Si la imagen es válida, continuar con el proceso de predicción

        insect_model = InsectModel()
        predictions = insect_model.predict(temp_file_path)
        print("predictions..."+predictions)
        
#        # Convertir las predicciones a un formato JSON-friendly
#        json_predictions = []
#        for pred in predictions:
#            json_predictions.append({
#                "class": pred["label"],
#                "confidence": pred["confidence"],
#                "bbox": pred["bbox"]
#            })
#
#        logger.info("Predictions:", json_predictions)
#
        return predictions
    except Exception as e:
        logger.error(f"Error durante el procesamiento de la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Se produjo un error interno del servidor")

