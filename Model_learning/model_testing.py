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

data_dir = './custom_dataset'
train_datasets = datasets.ImageFolder(os.path.join(data_dir, 'train'), transforms_train)
test_datasets = datasets.ImageFolder(os.path.join(data_dir, 'test'), transforms_test)

train_dataloader = torch.utils.data.DataLoader(train_datasets, batch_size=10, shuffle=True, num_workers=4)
test_dataloader = torch.utils.data.DataLoader(test_datasets, batch_size=10, shuffle=True, num_workers=4)

print('학습 데이터셋 크기:', len(train_datasets))
print('테스트 데이터셋 크기:', len(test_datasets))

class_names = train_datasets.classes

model.eval()
start_time = time.time()

def imshow(input, title):

    input = input.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    input = std * input + mean
    input = np.clip(input, 0, 1)
    plt.imshow(input)
    plt.title(title)
    plt.show()

if __name__ == '__main__':
    with torch.no_grad():
        running_loss = 0.
        running_corrects = 0

        for inputs, labels in test_dataloader:
            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)
            print(outputs)
            _, preds = torch.max(outputs, 1)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)