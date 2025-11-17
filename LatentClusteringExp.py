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
import shutil 









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
                self.__prepare_folder()

        
        def __prepare_folder(self) : 


                self.output_folder=os.path.join(self.input_folder,"output")
                if os.path.exists(self.output_folder) : 
                        shutil.rmtree(self.output_folder)

                os.makedirs(self.output_folder)

                self.list_images=[os.path.join(self.input_folder,"images",i) for i in os.listdir(os.path.join(self.input_folder,"images") ]
        
           
        def instantiate_SAM(self) : 

                        sam2 = build_sam2(self.model_cfg_path, self.model_ckpt_path, device=self.device, apply_postprocessing=False)

                        self.predictor = SAM2AutomaticMaskGenerator(
                        model=sam2,
                        points_per_side=64,
                        pred_iou_thresh=0.8,
                        stability_score_thresh=0.2,
                        mask_threshold=0.0,
                        min_mask_region_area=0,
                        output_mode="binary_mask",
                        multimask_output=False
                )




                        



        
        
        

                





        
        
        