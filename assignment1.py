# 🦸 Superhero base class with attributes and expressive methods
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name}, born of {self.origin}, wielding the power of {self.power}!"

    def use_power(self):
        return f"{self.name} unleashes {self.power} in a blaze of glory!"

# 🧠 Subclass with encapsulation and polymorphism
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.__gadget = gadget  # Encapsulated attribute

    def reveal_gadget(self):
        return f"{self.name} activates their secret gadget: {self.__gadget}!"

    def use_power(self):  # Polymorphic override
        return f"{self.name} hacks reality with {self.power} using {self.__gadget}!"

# 🌿 Another subclass
class NatureHero(Superhero):
    def __init__(self, name, power, origin, element):
        super().__init__(name, power, origin)
        self.element = element

    def use_power(self):  # Polymorphic override
        return f"{self.name} channels the spirit of {self.element} to unleash {self.power}!"

# 🎬 Example usage
hero1 = TechHero("Circuit", "Cyber Surge", "Neo-Tokyo", "Quantum Blade")
hero2 = NatureHero("Verdantia", "Earthquake Roar", "Amazon Depths", "Earth")

print(hero1.introduce())
print(hero1.use_power())
print(hero1.reveal_gadget())

print(hero2.introduce())
print(hero2.use_power())
