import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.chunk import *
from nltk.chunk.regexp import *
from nltk.chunk.util import *
from nltk.book import *
from matplotlib import pylab

#nltk.download()


# print(text1)
# print("==========================================")
# text2.concordance("monstrous") #find particular word usage in a text - word occurence and context given
# print("==========================================")
# text2.concordance("fearless")
# print("==========================================")
# text1.similar("monstrous")
# print("==========================================")
# text2.concordance("very")
# print("==========================================")
# text2.similar("monstrous") #gives common words that can replace monstrous in various sentences and work in that context still
# print("==========================================")
# text2.common_contexts(["monstrous", "heartily"]) #finds all contexts wherein heartily can replace monstrous

#you can see from how the word monstrous is being used in both texts.
#text1 associates it with being scary (-ve)
#text2 associates it with being profound (+ve)


#get the frequency of each word of interest as per index.
#text1.dispersion_plot(["monstrous", "that", "the", "very", "whatever"])

#
#
# text3.generate("""In the beginning of his brother is a hairy man , whose top may reach
# unto heaven ; and ye shall sow the land of Egypt there was no bread in
# all that he was taken out of the month , upon the earth . So shall thy
# wages be ? And they made their father ; and Isaac was old , and kissed
# him : and Laban with his cattle in the midst of the hands of Esau thy
# first born , and Phichol the chief butler unto his son Isaac , she""")
#
# print(len(text3))
#
# print(sorted(set(text3))) #distinct tokens (vocabulary) in text without repeats
#
# print(len(set(text3)))
#
# print(len(set(text3))/len(text3)) #richness of a text (unique/total words)
#
#
# print(text5.count('lol'))
# print(100*(text5.count("lol")/len(text5))) #  % of word occurence wrt to entire text
#
#
# def lexical_diversity(text):
#     return len(set(text))/len(text)
#
# def percent(count,total):
#     return 100*(count/total)
#
#
# #lists
# sent1 = ['call', 'me','Srikanth']
# print(len(sent1))
# print(lexical_diversity(sent1))
#
# print(sent2)
# print(percent(sent2.count("been"),len(sent2)))
#
# print(sent1+sent2)
# print(text4.index('awaken'))
# print(text4[-2:]) #backward search
#
# name = "srikanth,kijiji"
# print(name*2)
# print(name.split(','))

# print(FreqDist(text1))
#
# fr = FreqDist(text1)
# print(FreqDist(text1).most_common(50))
# fr.plot(50, cumulative =True)

#finding specific words

vocab = set(text1)
frq=FreqDist(text1)
long_words = [w for w in vocab if len(w) > 15 and frq[w] >7]
print (long_words)

text1.collocations() #gives all the bigrams








#===========================================================================================
#-Part 2-

#===========================================================================================



#tokenizing - word tokenziers, sentence tokenizers
#corpora (body of text ie medical journals, presidential speeches) and
# lexicons (dictionary - words and meanings ie. investors speak, english speak, science talk)


##preprocessing sentences
# example_text ="Hello there, how are you today? The weather is great in Canada and Python is awesome.  The sky is pretty today!"
# example_test_fix = example_text.split(" ")
# print(example_test_fix)
#
# print(sent_tokenize(example_text)) #split by sentence
# print(word_tokenize(example_text)) # split by word - treats punctuation as its own word.
#
# for i in (word_tokenize(example_text)):
#     print(i)

##stop words --filler words
#remove stop words for analysis
# example_sentence = "This is an example showing off stop word filtration."
# stop_words = set(stopwords.words("english"))
# print(stop_words)
#
# words = word_tokenize(example_sentence)
# filtered_sentence = []
# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
# #filtered_sentence = [for w in words if w not in stop_words]
# print(filtered_sentence)

#stemming - normalization kind of (ie: liking = lik)
#I was taking a ride in the car
#I was riding in the car

# ps = PorterStemmer()
# example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
#
# for w in example_words:
#     print(ps.stem(w))
# # better to use "wordnet"
# new_text = "It is very important to be pythonly while you are pythoning with python.  All pythoners have pythoned"
# new_text_words = word_tokenize(new_text)
# for w in new_text_words:
#     print(ps.stem(w))


#Part of speech tagging
#
# train_text = state_union.raw("2005-GWBush.txt")
# sample_text = state_union.raw("2006-GWBush.txt")
# #Punkt is already training, but we can train again.
# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
#
# tokenized = custom_sent_tokenizer.tokenize(sample_text) #sentences right now
# print(tokenized)
#
# def process_content():
#     try:
#         for i in tokenized: #per sentence
#             words = nltk.word_tokenize(i) #make words
#             tagged = nltk.pos_tag(words) #tag each word
#             print(tagged)
#
#     except Exception as e:
#         print(str(e))


#process_content()
# [('PRESIDENT', 'NNP'), ('GEORGE', 'NNP'), ('W.', 'NNP'), ('BUSH', 'NNP'), ("'S", 'POS'), ('ADDRESS', 'NNP'), ('BEFORE', 'IN'), ('A', 'NNP'), ('JOINT', 'NNP'), ('SESSION', 'NNP'), ('OF', 'IN'), ('THE', 'NNP'), ('CONGRESS', 'NNP'), ('ON', 'NNP'), ('THE', 'NNP'), ('STATE', 'NNP'), ('OF', 'IN'), ('THE', 'NNP'), ('UNION', 'NNP'), ('January', 'NNP'), ('31', 'CD'), (',', ','), ('2006', 'CD'), ('THE', 'NNP'), ('PRESIDENT', 'NNP'), (':', ':'), ('Thank', 'NNP'), ('you', 'PRP'), ('all', 'DT'), ('.', '.')]
# [('Mr.', 'NNP'), ('Speaker', 'NNP'), (',', ','), ('Vice', 'NNP'), ('President', 'NNP'), ('Cheney', 'NNP'), (',', ','), ('members', 'NNS'), ('of', 'IN'), ('Congress', 'NNP'), (',', ','), ('members', 'NNS'), ('of', 'IN'), ('the', 'DT'), ('Supreme', 'NNP'), ('Court', 'NNP'), ('and', 'CC'), ('diplomatic', 'JJ'), ('corps', 'NN'), (',', ','), ('distinguished', 'JJ'), ('guests', 'NNS'), (',', ','), ('and', 'CC'), ('fellow', 'JJ'), ('citizens', 'NNS'), (':', ':'), ('Today', 'VB'), ('our', 'PRP$'), ('nation', 'NN'), ('lost', 'VBD'), ('a', 'DT'), ('beloved', 'VBN'), (',', ','), ('graceful', 'JJ'), (',', ','), ('courageous', 'JJ'), ('woman', 'NN'), ('who', 'WP'), ('called', 'VBD'), ('America', 'NNP'), ('to', 'TO'), ('its', 'PRP$'), ('founding', 'NN'), ('ideals', 'NNS'), ('and', 'CC'), ('carried', 'VBD'), ('on', 'IN'), ('a', 'DT'), ('noble', 'JJ'), ('dream', 'NN'), ('.', '.')]
# [('Tonight', 'NN'), ('we', 'PRP'), ('are', 'VBP'), ('comforted', 'VBN'), ('by', 'IN'), ('the', 'DT'), ('hope', 'NN'), ('of', 'IN'), ('a', 'DT'), ('glad', 'JJ'), ('reunion', 'NN'), ('with', 'IN'), ('the', 'DT'), ('husband', 'NN'), ('who', 'WP'), ('was', 'VBD'), ('taken', 'VBN'), ('so', 'RB'), ('long', 'RB'), ('ago', 'RB'), (',', ','), ('and', 'CC'), ('we', 'PRP'), ('are', 'VBP'), ('grateful', 'JJ'), ('for', 'IN'), ('the', 'DT'), ('good', 'JJ'), ('life', 'NN'), ('of', 'IN'), ('Coretta', 'NNP'), ('Scott', 'NNP'), ('King', 'NNP'), ('.', '.')]
# [('(', '('), ('Applause', 'NNP'), ('.', '.'), (')', ')')]
# [('President', 'NNP'), ('George', 'NNP'), ('W.', 'NNP'), ('Bush', 'NNP'), ('reacts', 'VBZ'), ('to', 'TO'), ('applause', 'VB'), ('during', 'IN'), ('his', 'PRP$'), ('State', 'NNP'), ('of', 'IN'), ('the', 'DT'), ('Union', 'NNP'), ('Address', 'NNP'), ('at', 'IN'), ('the', 'DT'), ('Capitol', 'NNP'), (',', ','), ('Tuesday', 'NNP'), (',', ','), ('Jan', 'NNP'), ('.', '.')]
# [('31', 'CD'), (',', ','), ('2006', 'CD'), ('.', '.')]

##Chunking

# train_text = state_union.raw("2005-GWBush.txt")
# sample_text = state_union.raw("2006-GWBush.txt")
# #Punkt is already trained, but we can train again.
# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
#
# tokenized = custom_sent_tokenizer.tokenize(sample_text) #sentences right now
# #print(tokenized)
#
# def process_content():
#     try:
#         for i in tokenized: #per sentence
#             words = nltk.word_tokenize(i) #make words
#             tagged = nltk.pos_tag(words) #tag each word
#
#             chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
#             chunkParser = nltk.RegexpParser(chunkGram)
#             chunked = chunkParser.parse(tagged)
#             chunked.draw()
#     except Exception as e:
#         print(str(e))
#
# process_content()
