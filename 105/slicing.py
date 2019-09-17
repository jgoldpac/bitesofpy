from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

def slice_and_dice(text: str = text) -> list:
  results = []
  words = []
  text = text.lstrip()
  for line in text.splitlines():
    lower_line = line.lower()
    if line[0]==lower_line[0]:
      words = line.split()
      last_word = words[len(words)-1]
      len_word = len(last_word)
      last_char = last_word[len_word-1]
      if last_char=="." or last_char=="!":
        last_word = last_word[0:(len_word-2)]
      results.append(last_word)
  return(results)

#print(slice_and_dice(text))