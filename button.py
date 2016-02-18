class Box:

    def __init__(self, value):
        self.value = value

    def show_value(self):
        return self.value

    def show_form(self):
        return self.form


abc = Box(55)
abc.show_value()
print(abc.show_value())
