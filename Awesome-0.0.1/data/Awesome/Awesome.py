from HaikuR1.ApplicationKit import Application
from HaikuR1.InterfaceKit import Window, TextView, B_TITLED_WINDOW, B_QUIT_ON_WINDOW_CLOSE

app = Application("application/x-vnd.Awesome")


class AppWindow(Window):
    def __init__(self, *args, **kwargs):
        self.textview = TextView(
            frame        = [50, 50, 250, 140],
            textRect     = [0, 0, 190, 90],
            name         = "Aweview",
            color        = "#000000",
        )
        self.textview.DoesWordWrap()
        self.AddChild(self.textview)


window = AppWindow(
    frame      = [350, 350, 800, 600],
    title      = "Awesome",
    type       = B_TITLED_WINDOW,
    flags      = B_QUIT_ON_WINDOW_CLOSE,
)




window.Show()

app.Run()
