import os

import neovim

from myo.nvim_plugin import MyoNvimPlugin

import amino
from amino.logging import tryp_file_logging, VERBOSE

if 'MYO_DEBUG' in os.environ:
    amino.development = True
    tryp_file_logging(VERBOSE)


@neovim.plugin
class Plugin(MyoNvimPlugin):
    pass
