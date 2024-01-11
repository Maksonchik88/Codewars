def order(sentence):
  if len(sentence) == 0:
      return sentence
  else:
      my_dict = {}
      for el in sentence.split():
          for letter in el:
              if letter in '123456789':
                  my_dict[int(letter)] = el
                  break

      return ' '.join(dict(sorted(my_dict.items())).values())


