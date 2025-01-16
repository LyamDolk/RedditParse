import spacy

spacy.prefer_gpu()
#nlp = spacy.load("en_core_web_lm") # model selection
#nlp = spacy.load("en_core_web_sm") # model selection
nlp = spacy.load("en_core_web_trf") # model selection

import en_core_web_trf

nlp = en_core_web_trf.load()
#doc = nlp("This is a symptom of woke culture, where people are afraid to speak their minds.")
doc = nlp("This is a symptom of woke culture, but I woke up tired.")
print([(w.text, w.pos_) for w in doc])