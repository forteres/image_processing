import argparse
import os
import numpy as np
import cv2 as cv
from pathlib import Path
from datetime import datetime

# import methods
try:
    import lab_m1_1
except ModuleNotFoundError:
    lab_m1_1 = None

# global vars
img_default_path = Path(__file__).parent.parent/'images'

operations = {}
if lab_m1_1 is not None:
    operations.update(lab_m1_1.operations)

# main handler
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='arguments for pdi_lab')

    parser.add_argument('-i', '--input', type=str,default=os.path.join(img_default_path, 'input', 'donkey.jpg'), help='input path+file')
    parser.add_argument('-o', '--output', type=str,default=os.path.join(img_default_path, 'output', datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.jpg'), help='output path+file')
    parser.add_argument('-p', '--operation', type=str,required=True, help='operation to perform', choices=list(operations.keys()))
    args = parser.parse_args()

    operations[args.operation](args.input, args.output)