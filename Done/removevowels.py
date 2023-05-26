def remove_vowels(string_:str):
  return "".join([x for x in string_ if x.lower() not in "aeiou"])