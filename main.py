from time import strftime

from kivy.app import App
from kivy.clock import Clock


class ClockApp(App):
    sw_seconds = 0
    sw_started = False

    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    def update_stop_watch(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = '%02d:%02d.[size=40]%02d[/size]' % \
                                       (int(minutes), int(seconds), int(seconds * 100 % 100))

    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)
        Clock.schedule_interval(self.update_stop_watch, 0.016)

    def start_stop(self):
        self.root.ids.stopwatch.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.stopwatch.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0


if __name__ == '__main__':
    ClockApp().run()

