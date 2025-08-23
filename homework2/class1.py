class string_operations:
    def __init__(self):
        pass

    def getString(self, text):
        self.text = text

    def printString(self):
        return self.text.upper()



string1 = string_operations()
string1.getString("Hello")
print(string1.printString())