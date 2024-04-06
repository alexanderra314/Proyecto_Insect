import torch
import typing
import os
from enum import Enum, auto
from abc import ABC
from ultralytics import YOLO
import subprocess

from torchvision.transforms import functional as F
from PIL import Image

from ultralytics import YOLO

# Define el directorio actual
current_directory = os.path.dirname(os.path.realpath(__file__))
print("directorio " + current_directory)

# Ruta relativa al archivo Yolo_m_25_epocas_best.pt
model_filename = "../backend/models/Yolo_m_25_epocas_best.pt"

# Definir el framework
class Framework(Enum):
    pytorch = auto()

# Definir la clase Model
class Model(ABC):
    def __init__(
        self,
        model_name: str,
        model_path: typing.Union[str, os.PathLike],
        framework: Framework,
        version: int,
        classes: typing.List[str],
    ):
        self.model_name = model_name
        self.model_path = model_path
        self.framework = framework
        self.version = version
        self.classes = classes
        self.model = None

        self.load()

    def load(self):
        """
        Load the model from the model_path
        """
        if self.framework == Framework.pytorch:
            self.__load_pytorch_model()
        else:
            raise ValueError(f"Framework {self.framework} not supported")

    def __load_pytorch_model(self):
        """
        Load a PyTorch model
        """
        import torch

        # Load the PyTorch model from the model_path
        checkpoint = torch.load(self.model_path)

        # Extract the model from the checkpoint
        self.model = checkpoint["model"]

    def __call__(self, X: typing.Any) -> typing.Any:
        return self.predict(X)

    def predict(self, X: typing.Any) -> typing.Any:
        """
        Make a prediction.
        """
        raise NotImplementedError("Subclasses must implement this method")

# Definir la clase InsectModel
class InsectModel(Model):
    def __init__(self):
        model_path = os.path.join(current_directory, model_filename)
        framework = Framework.pytorch
        version = 1
        classes = [
            "Bees", "Butterfly", "caterpillar", "centipedes", "cockroach", 
            "dragonfly", "fly", "grasshopper", "ladybug", "Mantis", 
            "mosquito", "spider", "wasp"
        ]
        name = "yolo-model"
        print("Model Path:", model_path)
        super().__init__(name, model_path, framework, version, classes)
        self._Model__load_pytorch_model()  # Llama al método para cargar el modelo PyTorch

    def predict(self, image_path: str):
        print("Model path:", self.model_path)  # Verifica la ruta del modelo
        print("Image path:", image_path)

#        model = YOLO(self.model_path)
#        results = model(image_path, save=True, imgsz=640, conf=0.5, max_det=1, visualize=False, save_txt=True)
#

        # Define los parámetros del comando
        command = "yolo"
        model_path = "/content/Yolo_m_25_epocas_best.pt"
        confidence_threshold = 0.40
        #image_path = "/content/EuropeanPaperWasp.jpg"
        mode = "predict"
        task = "detect"

        # Construye el comando completo
        full_command = f"{command} model={self.model_path} conf={confidence_threshold} source={image_path} mode={mode} task={task}"
     

        # Ejecuta el comando
        output = subprocess.run(full_command, shell=True, capture_output=True, text=True)

        # Imprime la salida
        # Verifica si hubo algún error durante la ejecución
        if output.returncode != 0:
            return "0"

        else:
            return "1"


