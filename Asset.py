import os
import logging
import re

I18N_PATTERN = re.compile("^\"(?P<name>.*?)\".*;$")


class Asset(object):
    def __init__(self, input_path):
        self.__input_path = input_path
        self.__path = None
        self.color_name_list = []
        self.image_name_list = []
        self.i18n_string_list = []

        self.__search_assets_folder()
        logging.info(self.color_name_list)
        logging.info(self.image_name_list)

    def __search_assets_folder(self):
        if self.__input_path and os.path.exists(self.__input_path) and os.path.isdir(self.__input_path):
            for root, dirs, files in os.walk(self.__input_path):
                for name in dirs:
                    if name.endswith(".colorset"):
                        self.color_name_list.append(name[:-1 * len(".colorset")])
                    if name.endswith(".imageset"):
                        self.image_name_list.append(name[:-1 * len(".imageset")])
                for name in files:
                    if name.endswith(".strings"):
                        with open(root + "/" + name, mode="r") as f:
                            for line in f.readlines():
                                match = I18N_PATTERN.match(line)
                                if match:
                                    self.i18n_string_list.append(match.groupdict()['name'])

