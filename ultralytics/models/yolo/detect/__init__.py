# Ultralytics YOLO 🚀, AGPL-3.0 license

from .predict import DetectionPredictor
from .train import DetectionTrainer
from .val import DetectionValidator
from .uda_train import UDADetectionTrainer

__all__ = "DetectionPredictor", "DetectionTrainer", "DetectionValidator" ,"UDADetectionTrainer"
