from manager.input_manager import *
from manager.light_source_manager import *
from manager.line_segment_manager import *
from manager.screen_manager import *

def init_manager():
    init_input_manager()
    init_screen_manager()
    init_light_source_manager()
    init_line_segment_manager()