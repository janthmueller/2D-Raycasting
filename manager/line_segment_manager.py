def init_line_segment_manager():
    LineSegmentManager.temp_line = []
    LineSegmentManager.settled_lines = []
    LineSegmentManager.outer_bound_lines = []


class LineSegmentManager:
    @property
    @staticmethod
    def temp_line(self):
        return self.__temp_line

    @temp_line.setter
    @staticmethod
    def temp_line(self, value):
        self.__temp_line = value

    @property
    @staticmethod
    def settled_lines(self):
        return self.__settled_lines

    @settled_lines.setter
    @staticmethod
    def settled_lines(self, value):
        self.__settled_lines = value

    @property
    @staticmethod
    def outer_bound_lines(self):
        return self.__outer_bound_lines

    @outer_bound_lines.setter
    @staticmethod
    def outer_bound_lines(self, value):
        self.__outer_bound_lines = value
