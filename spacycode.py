import spacy

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_lm")
#nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("en_core_web_trf")

