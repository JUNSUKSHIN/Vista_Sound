import torch
import torch.nn as nn
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import torch.optim as optim

import torchvision
from torchvision import datasets, models, transforms
import numpy as np
import time
import os

PATH = './weights/'

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = torch.load(PATH + 'model.pt', map_location=torch.device('cpu'))
model.load_state_dict(torch.load(PATH + 'model_state_dict.pt', map_location=torch.device('cpu')))

checkpoint = torch.load(PATH + 'all.tar', map_location=torch.device('cpu'))
model.load_state_dict(checkpoint['model'])
criterion = nn.CrossEntropyLoss()


transforms_train = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

transforms_test = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])