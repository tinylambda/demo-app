from kivy.app import App
from kivy.uix.widget import Widget


class CanvasWidget(Widget):
    pass


class PaintApp(App):
    def build(self):
        return CanvasWidget()


if __name__ == '__main__':
    from kivy.config import Config
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')
    Config.set('graphics', 'resizable', '0')

    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex

    Window.clearcolor = get_color_from_hex('#FFFFFF')

    PaintApp().run()

