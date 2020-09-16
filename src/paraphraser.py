from googletrans import Translator
from random import randint

def paraphrase(sentence):
  """
    returns list of sentences with similar meaning to sentence
  """

  language_list = ["ko","fr","ja","id","it","pt","ru","af","sq","am","ar","ca","nl","de","es","tr"]
  translator = Translator()
  translated_sentence_list = []
  for language in language_list:
    text = translator.translate(sentence,dest=language)  
    text = translator.translate(text.text,src=language,dest = "en")
    translated_sentence_list.append(text.text)
  translated_sentence_list.sort()
  translated_sentence_list = list(set(translated_sentence_list))
  return translated_sentence_list
