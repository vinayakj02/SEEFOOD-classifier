# SeeFood
![phone-gif](https://user-images.githubusercontent.com/74676945/176158166-e24d4065-aae8-4cd8-a6e5-3002ebf15117.gif)

To classify whether food in the picture is a hotdog or not. Based on the app [seefood in HBO's Silicon Valley ](https://www.youtube.com/watch?v=vIci3C4JkL0). To make this I used a pre-trained <b>Densenet121</b> model and applied transfer learning with the help of GPUs in cloud to fine tune the model to the hot-dogs dataset. This was made using <b>PyTorch</b> with <b>Python</b>. Made into a web application with <b>Flask</b> </p> 

### Demo : [Gradio demo](https://thawing-castle-09965.herokuapp.com/)

## Model 
* Classifier built upon a densenet121 model using transfer learning using PyTorch. 
* [Dataset , Hot Dog - Not Hot Dog](https://www.kaggle.com/dansbecker/hot-dog-not-hot-dog)
* The model gave a accuracy of 87% unseen test data.

![S-E-E FOOD](https://user-images.githubusercontent.com/74676945/176158167-70dacb97-35f2-455b-8cfb-4b32c0caca57.gif)

