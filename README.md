### Spacy Textcat

This project uses spaCy to train a `multi-class classifier` where the classes are exclusive. Training a `binary classifier` would simply involve not setting one of the labels. However, for training a `multilabel classifier` the config has to be changed and the labels explicitly set like this one.

#### Generate data and train model

```
python data.py && spacy train config.cfg --output ./output
```

#### Run demo predictions

```
python predict.py
```
