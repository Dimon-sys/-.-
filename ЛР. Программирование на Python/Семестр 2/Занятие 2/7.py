class Library:
    def __init__(self, library=dict()):
        self.library = library.copy()

    def add(self, name, author):
        self.library[name] = author

    def __contains__(self, item):
        return item in self.library
    
    def __delitem__(self, key):
        del self.library[key]

lib = Library()
lib.add("1984", "Orwell")
print("1984" in lib) # true
del lib["1984"]
print("1984" in lib) # false
