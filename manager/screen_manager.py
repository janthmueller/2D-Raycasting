def init_screen_manager():
    ScreenManager.screen_width = 680
    ScreenManager.screen_height = 460


class ScreenManager:
    @property
    @staticmethod
    def screen_width(self):
        return self.__screen_width

    @screen_width.setter
    @staticmethod
    def screen_width(self, value):
        self.__screen_width = value

    @property
    @staticmethod
    def screen_height(self):
        return self.__screen_height

    @screen_height.setter
    @staticmethod
    def screen_height(self, value):
        self.__screen_height = value
