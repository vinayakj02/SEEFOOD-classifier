import gradio as gr 
import torch 
from torchvision import transforms, models
from torch import nn

path = "seefood89.pth"

model = models.densenet121(pretrained=False)

for params in model.parameters():
    params.require_grad = False 
classifier = nn.Sequential(nn.Linear(1024,1024),nn.ReLU(),nn.Dropout(p=0.3),
                           nn.Linear(1024,512),nn.ReLU(),nn.Dropout(p=0.3),
                           nn.Linear(512,2),nn.LogSoftmax(dim=1))
model.classifier = classifier
model.load_state_dict(torch.load(path,map_location='cpu'))
model.eval()

classes = {0:'✅ hot dog 🌭 ', 1:'❌ not hot dog 🌭 '}


def get_prediction(img):
    transform = transforms.Compose([transforms.ToPILImage(),transforms.Resize(256),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),])
    img_t = transform(img)  
    output = model(img_t.unsqueeze(0))
    prediction = torch.argmax(output,dim=1)
    return classes[prediction.item()]


title = "SEEFOOD"
description = "<p style='text-align: center'>It's shazam for food but only hotdogs (from HBO's Silicon Valley) , made using transfer learning ( Densenet121)</p>"
article="<p style='text-align: center'><a href='https://github.com/vinayakj02/SEEFOOD-classifier' target='_blank'>Github</a></p>"

gr.Interface(fn=get_prediction, 
             inputs="image",
             outputs="label",
             examples=["burger_1.jpg", "hotdog1.jpg", "pizza.jpg", "cream.jpg"],
             title=title,description=description,article=article,).launch(debug=True)
