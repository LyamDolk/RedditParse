python -m pip install --upgrade pip
python pip install -U pip setuptools wheel
pip install -U 'spacy[cuda12x]'
pip install pygls 

python -m spacy download en_core_web_trf # success
python -m spacy download en_core_web_sm # success
python -m spacy download en_core_web_lg # success

#Validate spacy
python -m spacy validate



