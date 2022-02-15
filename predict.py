import spacy

nlp = spacy.load("output/model-best")
doc = nlp("That is some space shit I think and I love to talk about dark matters")
print(doc.cats)
doc = nlp("I drive a Honda Civic and it is a great car for me")
print(doc.cats)
doc = nlp("I don't read the Bible anymore, neither do I go to Church")
print(doc.cats)
