# Pokemon CNN
As an avid Pokemon fan I wanted to build my own pokedex and the first step of getting this done is to build a functional image classification model . Using [this dataset](https://www.kaggle.com/datasets/lantian773030/pokemonclassification) from Kaggle I started my process of training.

## Data Processing
The dataset is rather small with only 7000 labeled images. If I am to start training with this dataset I’m bound to run into sampling bias and overfitting issues. In order to make the dataset a bit more robust without having to put hours of work into downloading thousands of more images myself, I wrote a simple python script that skews the data by greyscaling, rotating, and flipping the images. By doing this I was able to turn a 7000 image dataset into a 21000 image dataset. 

## Training
While I could’ve tried to train a model by building a neural network from scratch, there exist plenty of models that are great at image classification. I took the existing VGG19 model and applied transfer learning to train it to recognize pokemon.

## Next Steps
Next up I’d like to build a mobile app around this and allow people to take photos of pokemon for this to identify and then output data about the classified pokemon to the user, like a real life pokedex.
