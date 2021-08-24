class Mere:
    def bonjour(self):
        return "Vous avez le bonjour de la classe mère !"


class Fille2(Mere):
    def bonjour(self):
        return "Vous avez le bonjour de la classe fille !"


if __name__ == " __main__ ":
    fille = Fille2()
    print(fille.bonjour())
