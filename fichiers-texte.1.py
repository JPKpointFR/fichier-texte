# FICHIERS TEXTE
#
# ouvrir (open) <- nom du fichier, mode
# écrire (write) / lire (read)
# fermer (close)
#

f = open("mon_fichier.txt", "w")
f2 = open("mon_fichier2.txt", "w")

# f.write("Bonjour\n")
# f.write("Bonjour")


l = ["phrase 1", "phrase 2", "phraseut"]

f.write("\n".join(l))
f.write("\nFin")

f.close()
