# source video: https://www.youtube.com/watch?v=Maj9v-Ev7-4
# this project based on author's work for sns and news article application
# this is secondary project so that author can share with people

from fastapi import FastAPI
from typing import List
import spacy

from .models import Payload, Entities



app = FastAPI()

nlp = spacy.load("en_core_web_sm") # toeknization model from spacy
#doc = nlp("Apple is looking at buying U.K. startup for $1 billion")


@app.post('/ner-service')
async def get_ner(payload: Payload):
    tokenize_content: List[spacy.tokens.doc.Doc] = [ 
        nlp(content.content) for content in payload.data
    ] # force typing, return list of tokens from Content.content

    document_entities = []
    for doc in tokenize_content:
        x = [ {'text': ent.text, 'entity_type': ent.label_} for ent in doc.ents]
        #print(x)
        document_entities.append(x)
    
    return [
        Entities(post_url=post.post_url, entities=ents)
        for post,ents in zip(payload.data, document_entities)
    ]
        
    #for ent in doc.ents:
    #    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    #return ''
    