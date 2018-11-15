import os
import logging


class Asset(object):
    def __init__(self, input_path):
        self.__input_path = input_path
        self.__path = None
        self.color_name_list = []
        self.image_name_list = []

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
