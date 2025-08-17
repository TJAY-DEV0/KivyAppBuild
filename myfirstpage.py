from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.graphics import Rectangle,Color

class MyFirstScreen(FloatLayout):
    def __init__(self,**kwargs):
        super(MyFirstScreen,self).__init__(**kwargs)
        
        with self.canvas.before:
            Color(1,1,1)
            
            self.rect = Rectangle(size=self.size,pos=self.pos)
            self.bind(size=self.update_rect,pos=self.update_rect)
            
    def update_rect(self,instance,value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size
            
            
class MyApp(App):
    def build(self):
            self.per = 0
            layout = MyFirstScreen()
            
            optimal_logo = Image(source='/storage/emulated/0/Mykivy/calculator/optimal_logo.png',size_hint=(.7,.7),pos_hint={'center_y':.5,'center_x':.3})
            layout.add_widget(optimal_logo)
            
            other_labels = Label(text='Ptimal',color=(0,0,0),font_size=100,bold=True,pos_hint={'center_y':.48,'center_x':.7})
            layout.add_widget(other_labels)
            
            loading_label = Label(text='Loading...',color=(0,0,0,),pos_hint={'center_y':.13,'center_x':.5})
            layout.add_widget(loading_label)
            self.progress_bar = ProgressBar(pos_hint={'center_y':.1,'center_x':.5},size_hint_x=.85)
            layout.add_widget(self.progress_bar)
            
            Clock.schedule_interval(self.update_bar,0.01)
            
            return layout
            
    def update_bar(self,instance):
        self.per += 1
        
        self.progress_bar.value = self.per
        if self.per == 100:
            self.per = 1
        
        
    
if __name__ == '__main__':
    MyApp().run()