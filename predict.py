import spacy

nlp = spacy.load("output/model-best")
docs = [
    "That is some space shit I think and I love to talk about dark matters",
    "I drive a Honda Civic and it is a great car for me",
    "I don't read the Bible anymore neither do I go to Church",
]

for doc in nlp.pipe(docs):
    print(doc.cats)
