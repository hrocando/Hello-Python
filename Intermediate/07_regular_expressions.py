# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=19762

### Regular Expressions ###

import re

# Match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de Ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# if not (match == None):
# if match != None:
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#print(re.match("Expresiones Regulares", my_string))

# Search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# Search

findall = re.findall("lección", my_string)
print(findall)

# Split

print(re.split(":", my_string))

# Sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Clase en vídeo (09/11/22): https://www.twitch.tv/videos/1648023317

### Regular Expressions Patterns ###

# Para aprender y valir expresiones regulares: https://regex101.com/

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.dev"
print(re.findall(pattern, email))