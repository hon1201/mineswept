class Box:

    def __init__(self, value, form):
        self.value = Button(text = value , command = show_value)
        self.form = form

    def show_value(self):
        return value

    def show_form(self):
        return self.form
