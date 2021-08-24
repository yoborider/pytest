print (" Hello world !")

# Remove carriage return
print (" Hello world1 !", end ="")
print (" Hello world2 !", end ="")
print (" Hello "); print (" Joe ")

var = 3
print(var)

x = 32
nom="john"
print(nom,"a",x,"ans")
# Separator custom
print(nom,"a",x,"ans",sep="-")

# f-strings
print (f"{nom} a {x} ans ")

# format
print ("{} a {} ans".format(nom,x))

# Ecriture scientifique
y = 1000000
print (f"{y:.3e}")

# Ecriture avec arrondi
perc_GC = ((4500 + 2575)/14800)*100
print("Le pouventage de GC est {}".format(perc_GC))
#Le pouventage de GC est 47.80405405405405
print("Le pouventage de GC est {:.0f}".format(perc_GC))
#Le pouventage de GC est 48
print("Le pouventage de GC est {:.1f}".format(perc_GC))
#Le pouventage de GC est 47.8
print("Le pouventage de GC est {:.2f}".format(perc_GC))
#Le pouventage de GC est 47.80
print("Le pouventage de GC est {:.3f}".format(perc_GC))
#Le pouventage de GC est 47.804