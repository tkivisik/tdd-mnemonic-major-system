class NotPositiveDimensionsException(Exception):
    pass

class TooBigDimensionsException(Exception):
    pass

DIMENSION_MAX = 20
class MultiplicationTable(object):
    def __init__(self, height, width):
        if height <= 0 or width <= 0:
            raise NotPositiveDimensionsException("MultiplicationTable expects positive height and width")
        if height > DIMENSION_MAX or width > DIMENSION_MAX:
            raise TooBigDimensionsException("Dimensions must be <= {}".format(DIMENSION_MAX))
        self.height = height
        self.width = width

    def show_table_string(self):
        table_string = ""
        for h in range(1, self.height + 1):
            line = ''
            for w in range(1, self.width + 1):
                new_element = str(h*w).rjust(4)
                line = "{}{}".format(line, new_element)
            table_string = "{}{}\n".format(table_string, line)
        return table_string