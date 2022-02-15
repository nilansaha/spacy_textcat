import spacy
from spacy.tokens import DocBin
from sklearn.datasets import fetch_20newsgroups


def generate_spacy_dataset(subset: str, filename: str):
    dataset = fetch_20newsgroups(
        subset=subset,
        categories=["rec.autos", "sci.space", "talk.religion.misc"],
        shuffle=True,
        random_state=42,
    )

    nlp = spacy.blank("en")
    db = DocBin()
    data_tuples = (
        (dataset.data[idx], dataset.target[idx]) for idx in range(len(dataset.data))
    )
    for doc, label in nlp.pipe(data_tuples, as_tuples=True):
        doc.cats["autos"] = label == 0
        doc.cats["space"] = label == 1
        doc.cats["religion"] = label == 2
        db.add(doc)
    db.to_disk(filename)


generate_spacy_dataset("train", "./train.spacy")
generate_spacy_dataset("test", "./valid.spacy")
