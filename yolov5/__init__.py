
# try:
#     import importlib.metadata as importlib_metadata
# except ModuleNotFoundError:
#     import importlib_metadata

# __version__ = importlib_metadata.version(__name__)


__version__ = "4.0.0"

import imp
_, path, _ = imp.find_module('yolov5')
