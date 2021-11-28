from flask import Flask, render_template, request
import torch 
from torchvision import transforms, models
from torch import nn
from PIL import Image
import os 
from werkzeug.utils import secure_filename

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

classes = {0:'yes', 1:'not'}
def get_prediction(image_path):

    img = Image.open(image_path)
    transform = transforms.Compose([transforms.Resize(256),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),])
    img_t = transform(img)  
    output = model(img_t.unsqueeze(0))
    prediction = torch.argmax(output,dim=1)
    return classes[prediction.item()]
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        filepath = os.path.join('static\\uploads', filename)
        uploaded_file.save(filepath)
    

    x = get_prediction(filepath)
    r = f"""
    <html> <body>
    <img src="static\\uploads\\{x}-hotdog.png" alt="" width="1600" height="800">
    </body> </html>
    """ 
    return r 


if __name__ == '__main__':
    app.run(debug=True)