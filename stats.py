def get_num_words(text):
  words = text.split()
  return len(words)

def get_chars_dict(text):
  chars = {}
  for char in text:
    lowered = char.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_on(items):
  return items['num']

def dict_to_list_of_dicts(num_chars):
  result = []
  for char, count in num_chars.items():
    result.append({'char': char, 'num': count})
  result.sort(reverse=True, key=sort_on)
  return result