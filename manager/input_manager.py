def init_input_manager():
    InputManager.h_key = False
    InputManager.b_key = False


class InputManager:
    @property
    @staticmethod
    def left_down(self):
        return self.__left_down

    @left_down.setter
    @staticmethod
    def left_down(self, value):
        self.__left_down = value

    @property
    @staticmethod
    def right_down(self):
        return self.__right_down

    @right_down.setter
    @staticmethod
    def right_down(self, value):
        self.__right_down = value

    @property
    @staticmethod
    def left_up(self):
        return self.__left_up

    @left_up.setter
    @staticmethod
    def left_up(self, value):
        self.__left_up = value

    @property
    @staticmethod
    def right_up(self):
        return self.__right_up

    @right_up.setter
    @staticmethod
    def right_up(self, value):
        self.__right_up = value

    @property
    @staticmethod
    def left_last(self):
        return self.__left_last

    @left_last.setter
    @staticmethod
    def left_last(self, value):
        self.__left_last = value

    @property
    @staticmethod
    def right_last(self):
        return self.__right_last

    @right_last.setter
    @staticmethod
    def right_last(self, value):
        self.__right_last = value

    @property
    @staticmethod
    def h_key(self):
        return self.__h_key

    @h_key.setter
    @staticmethod
    def h_key(self, value):
        self.__h_key = value

    @property
    @staticmethod
    def b_key(self):
        return self.__b_key

    @b_key.setter
    @staticmethod
    def b_key(self, value):
        self.__b_key = value
