def init_light_source_manager():
    LightSourceManager.light_source_pos = ()
    LightSourceManager.ray_num = 100
    LightSourceManager.max_ray_num = 500
    LightSourceManager.min_ray_num = 4


class LightSourceManager:
    @property
    @staticmethod
    def light_source_pos(self):
        return self.__light_source_pos

    @light_source_pos.setter
    @staticmethod
    def light_source_pos(self, value):
        self.__light_source_pos = value

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
