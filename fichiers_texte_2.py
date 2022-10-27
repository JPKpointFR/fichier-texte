import os.path

# if not os.path.exists("toto"):
#     os.mkdir("toto")
if os.path.exists("toto"):
    os.rmdir("toto")

filename = os.path.join("rep", "mon_fichier.txt")
print("filename", filename)
if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename, "r")
    texte = f.read()
    print(texte)
    f.close()
else:
    print("Le fichier n'existe pas")

if os.path.exists(filename):
    os.remove(filename)


"""try:
    f = open("mon_fichier.txt", "r")
except FileNotFoundError:
    print("ERREUR: Le fichier n'a pas pu être ouvert car introuvable")
else:
    texte = f.read()
    print(texte)
    f.close()"""


"""
text = f.readline()
print(text, end="")
text = f.readline()
print(text)"""

# for line in f:
#     print(line, end="")
