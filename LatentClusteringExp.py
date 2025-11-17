import os
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from sam2.build_sam import build_sam2
from sam2.automatic_mask_generator import SAM2AutomaticMaskGenerator
import torch
import json
from torch import randint
import re
import pandas as pd
import argparse
import numpy as np
from tqdm import tqdm










class DataSetProcessor : 


    def __init__(self, input_folder) :

        """
        Args : 
        ____

        input_folder : shape of 

                input_folder/
                        images / 
                                ...tif

        """

        self.input_folder=input_folder

        