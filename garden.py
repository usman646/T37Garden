# Import spacy
import spacy
nlp = spacy.load('en_core_web_sm')

# Create list of garden path sentences
gardenpathSentences = ["The old man the boat", "Without her contributions would be impossible", "The horse raced past the barn fell.", "I convinced her children are noisy", "The girl told the story cried"]

# Iterate through list of garden path sentences and tokenise each sentence
for i in range(len(gardenpathSentences)):
    sentence = gardenpathSentences[i]
    nlp_gardenpathSentences = nlp(sentence)
    print([(token, token.orth_, token.orth) for token in nlp_gardenpathSentences])

# Iterate through list of garden path sentences and entitiy recognition on each sentence
for i in range(len(gardenpathSentences)):
    sentence = gardenpathSentences[i]
    nlp_gardenpathSentences = nlp(sentence)
    print([(i, i.label_, i.label) for i in nlp_gardenpathSentences.ents])

''' 
- Each garden path sentence was tokenised

- The sentences were not entity recognised unlike the priyanka chopra setence in the lecture
- Within the priyanka chopra entity recognition I was surpirsed by how numbers were in the entity "Cardinal" irrespective if they were written as "1" or "One"
- I was also intrigued by the entity of NORP for "Indian"

'''