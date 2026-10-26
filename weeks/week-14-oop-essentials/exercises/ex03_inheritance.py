"""Exercise 03: one clear basic inheritance example."""


class Animal:
    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name}: woof"


if __name__ == "__main__":
    dog = Dog("Milo")
    print(dog.speak())
    # Dog is an Animal because it inherits the shared name/state from Animal
    # and specializes the general concept with dog-specific behavior.
