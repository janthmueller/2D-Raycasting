def init_light_source_manager():
    LightSourceManager.source = ()
    LightSourceManager.ray_num = 100
    LightSourceManager.max_ray_num = 500
    LightSourceManager.min_ray_num = 4


class LightSourceManager:
    @property
    @staticmethod
    def source(self):
        return self.__source

    @source.setter
    @staticmethod
    def source(self, value):
        self.__source = value

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
