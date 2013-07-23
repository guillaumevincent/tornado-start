from ConfigParser import ConfigParser


class Config(ConfigParser):

    def get_option(self, section, option, default=None):
        if self.has_option(section, option) or default is None:
            return ConfigParser.get(self, section, option)
        else:
            return default

    def get_int(self, section, option, default=None):
        if self.has_option(section, option) or not isinstance(default, int):
            return ConfigParser.getint(self, section, option)
        else:
            return default

    def get_float(self, section, option, default=None):
        if self.has_option(section, option) or not isinstance(default, float):
            return ConfigParser.getfloat(self, section, option)
        else:
            return default

    def get_boolean(self, section, option, default=None):
        if self.has_option(section, option) or not isinstance(default, bool):
            return ConfigParser.getboolean(self, section, option)
        else:
            return default
