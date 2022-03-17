
def init_bound_manager():
    BoundManager.ghost_line = []
    BoundManager.bound_lines = []
    BoundManager.outer_bound_lines = []


class BoundManager:
    @property
    @staticmethod
    def ghost_line(self):
        return self.__ghost_line

    @ghost_line.setter
    @staticmethod
    def ghost_line(self, value):
        self.__ghost_line = value

    @property
    @staticmethod
    def bound_lines(self):
        return self.__bound_lines

    @bound_lines.setter
    @staticmethod
    def bound_lines(self, value):
        self.__bound_lines = value

    @property
    @staticmethod
    def outer_bound_lines(self):
        return self.__outer_bound_lines

    @outer_bound_lines.setter
    @staticmethod
    def outer_bound_lines(self, value):
        self.__outer_bound_lines = value