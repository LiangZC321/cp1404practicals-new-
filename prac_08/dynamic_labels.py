from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        names = ['Candy', 'Toki', 'William']
        for index, name in enumerate(names, start=1):
            label = Label(text=f'number{index}: {name}', font_size=24)
            self.root.ids.main.add_widget(label)

        return None

DynamicLabelsApp().run()