import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle
from nltk import pos_tag, ne_chunk
from sparknlp.pretrained import PretrainedPipeline
from requests import post

nlp_pipeline = PretrainedPipeline("entity_recognition")

cognitive_services_api_key = "MY_API_KEY"

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w!= "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)

tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return np.array(bag)

def handle_unknown_input(inp):

    entities = nlp_pipeline.annotate(inp)["entities"]
    entity_types = [entity["entity"] for entity in entities]

    sentiment_response = post("https://westus.api.cognitive.microsoft.com/text/analytics/v3.0/sentiment",
                              headers={"Ocp-Apim-Subscription-Key": cognitive_services_api_key},
                              json={"documents": [{"language": "en", "id": "1", "text": inp}]})
    sentiment_score = sentiment_response.json()["documents"][0]["score"]

    pos_tags = pos_tag(nltk.word_tokenize(inp))

    return {"entities": entity_types, "sentiment": sentiment_score, "pos_tags": pos_tags}

def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = np.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        unknown_input_results = handle_unknown_input(inp)
        print("Entities:", unknown_input_results["entities"])
        print("Sentiment:", unknown_input_results["sentiment"])
        print("POS Tags:", unknown_input_results["pos_tags"])

        print(random.choice(responses))

chat()