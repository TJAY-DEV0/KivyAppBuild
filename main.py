from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class counter(App):
    def build(self):
        
        layout  = BoxLayout(orientation="vertical")
        
        self.count_label = Label(text="0",size_hint=(1,.7),font_size=100)
        layout.add_widget(self.count_label)
        
        btn_layout = BoxLayout(orientation="horizontal",size_hint=(1,.3))
        layout.add_widget(btn_layout)
        
        btn_add = Button(text="Count",size_hint=(.5,1))
        btn_add.bind(on_release=self.add_count)
        self.btn_reset = Button(text="Reset",size_hint=(.5,1))
        self.btn_reset.bind(on_release=self.reset_count)
        
        btn_layout.add_widget(btn_add)
        btn_layout.add_widget(self.btn_reset)
        Clock.schedule_interval(self.check_number,.1)
        
        return layout
        
    def add_count(self,instance):
        num = int(self.count_label.text)
        num += 1
        self.count_label.text = str(num)
    def reset_count(self,instance):
        self.count_label.text = "0"
    def check_number(self,*args):
        if self.count_label.text == "0":
            self.btn_reset.disabled = True
        else:
            self.btn_reset.disabled = False
        
if __name__ == "__main__":
    counter().run()