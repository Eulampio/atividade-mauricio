import remi.gui as gui
from remi import start, App
class HelloWeb(App):
   def __init__(self, *args):
      super(HelloWeb, self).__init__(*args)
   def main(self):
      wid = gui.VBox(style={"background-color": "#64778D"})
      self.lbl = gui.Label('Hello World', width='100%', height='100%',
      style={ "color":"white",
         "text-align": "center",
         "font-family": "Arial Bold",
         "font-size": "20px"}
      )
      wid.append(self.lbl)
      return wid
      if __name__ == "__main__":
         start(HelloWeb, debug=True, address='0.0.0.0', port=0)