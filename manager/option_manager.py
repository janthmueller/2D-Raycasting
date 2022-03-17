def init_option_manager():
    OptionManager.ray_num = 100
    OptionManager.max_ray_num = 500
    OptionManager.min_ray_num = 4
    OptionManager.screen_width = 680
    OptionManager.screen_height = 460



class OptionManager:
    @property
    @staticmethod
    def ray_num(self):
        return self.__ray_num

    @ray_num.setter
    @staticmethod
    def ray_num(self, value):
        self.__ray_num = value

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

    @property
    @staticmethod
    def max_ray_num(self):
        return self.__max_ray_num

    @max_ray_num.setter
    @staticmethod
    def max_ray_num(self, value):
        self.__max_ray_num = value

    @property
    @staticmethod
    def min_ray_num(self):
        return self.__min_ray_num

    @min_ray_num.setter
    @staticmethod
    def min_ray_num(self, value):
        self.__min_ray_num = value


