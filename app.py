from Asset import Asset
from SwiftExtension import SwiftExtensionBuilder
import logging
import sys


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    path = None
    if len(sys.argv) > 1:
        path = sys.argv[1]
    asset = Asset(path)
    builder = SwiftExtensionBuilder(color_name_list=asset.color_name_list, image_name_list=asset.image_name_list)
    logging.info(builder.build_uicolor_extension())
    logging.info(builder.build_uiimage_extension())
    with open("UIColor+Assets.swift", mode="w") as f:
        f.write(builder.build_uicolor_extension())
    with open("UIImage+Assets.swift", mode="w") as f:
        f.write(builder.build_uiimage_extension())
