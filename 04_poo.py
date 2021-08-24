from dataclasses import dataclass

@dataclass
class Person:
    nom: str
    age: int

    def isOfAge(self):
        return True if self.age >= 18 else False

if __name__ == '__main__':
    p = Person('toto', 10)
    if p.isOfAge():
        print('Majeur')
    else:
        print('Mineur')