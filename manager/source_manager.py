def init_source_manager():
    SourceManager.ghost_source = ()
    SourceManager.source = ()

class SourceManager:
    @property
    @staticmethod
    def ghost_source(self):
        return self.__ghost_source

    @ghost_source.setter
    @staticmethod
    def ghost_source(self, value):
        self.__ghost_source = value

    @property
    @staticmethod
    def source(self):
        return self.__source

    @source.setter
    @staticmethod
    def source(self, value):
        self.__source = value