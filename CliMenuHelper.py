class CliMenuHelper(object):
    """docstring for CliMenuHelper."""
    frame_pattern = "#"
    select_option_message = "Select the option: "
    option_doesnt_exist_message = "The selected option does not exist.\nPress any key to continue..."

    def __init__(self, title, options, quit_option="q", padding_space=1):
        self.title = title
        self.options = options
        self.options_indexes = range(len(self.options) + 1)[1:]
        self.quit_option = quit_option
        self.padding_space = padding_space
        self.padding_blank_space = " " * self.padding_space
        self.max_space = self.get_max_space()
        self.separator = self.frame_pattern * (self.max_space + (self.padding_space * 2) + 5)
        self.line_wrapper = self.create_line_wrapper()
        self.exit_line = self.create_new_line("Press %s to exit." % self.quit_option)

    def start(self):
        self.cls()
        self.create_complete_menu()
        option_selected = raw_input(self.select_option_message)
        if option_selected == self.quit_option:
            print "Bye."
            return None
        try:
            option_selected = int(option_selected)
            if option_selected in self.options_indexes:
                return option_selected
        except ValueError:
            pass
        print self.option_doesnt_exist_message
        raw_input()
        self.start()

    def create_complete_menu(self):
        print self.separator
        print self.create_menu_title()
        print self.separator
        print self.create_options_panel()
        print self.exit_line
        print self.separator

    def create_menu_title(self):
        return self.create_new_line(self.title)

    def create_options_panel(self):
        response = []
        for position, option in enumerate(self.options):
            response.append(self.create_new_line("%s. %s" % (position + 1, option)))
        return "\n".join(response)

    def create_new_line(self, data_to_insert):
        new_line = self.line_wrapper.replace("#toreplace#", data_to_insert)
        if len(new_line) < len(self.separator):
            to_insert = len(self.separator) - len(new_line)
            return new_line[:-1] + (" " * to_insert) + new_line[-1:]
        return new_line

    def create_line_wrapper(self):
        return "{0}{1}#toreplace#{1}{0}".format(self.frame_pattern, self.padding_blank_space)

    def cls(self):
        import os
        os.system('cls')
        os.system('clear')

    def get_max_space(self):
        longest_value = max([len(option) for option in self.options])
        longest_value = longest_value if longest_value > len(self.title) else len(self.title)
        return longest_value if longest_value > len(self.select_option_message) else len(self.select_option_message)
