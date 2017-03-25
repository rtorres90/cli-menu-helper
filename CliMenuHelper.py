
class CliMenuHelper(object):
    """docstring for CliMenuHelper."""
    frame_pattern = "#"
    def __init__(self, title, options, quit_option="q", padding_space=1):
        self.title = title
        self.options = options
        self.quit_option = quit_option
        self.padding_space = padding_space
        self.padding_blank_space = " " * self.padding_space
        self.max_space = max([len(option) for option in self.options])
        self.head = self.frame_pattern * (self.max_space + (self.padding_space * 2) + 5)
        self.line_wrapper = self.create_line_wrapper()

    def start(self):
        print self.head
        print self.create_menu_title()
        print self.create_options_panel()
        print self.head

    def create_menu_title(self):
        return self.line_wrapper.replace("#toreplace#", self.title)

    def create_options_panel(self):
        response = []
        for position, option in enumerate(self.options):
            response.append(self.line_wrapper.replace("#toreplace#", "%s. %s" % (position, option)))
        return "\n".join(response)

    def create_line_wrapper(self):
        return "{0}{1}#toreplace#{1}{2}".format(self.frame_pattern, self.padding_blank_space, self.frame_pattern)
