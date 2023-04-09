# Credits: @pySmartDL
# Copyright (C) 2023 CustomThumb
#
# This file is a part of < https://github.com/BukanDev/CustomThumb/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/BukanDev/CustomThumb/blob/main/LICENSE/>.
#

from glob import glob
from os.path import basename, dirname, isfile

from thumb import *


def all_modules():
    mod_paths = glob(f"{dirname(__file__)}/*.py")
    return sorted(
        [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
    )


ALL_MODULES = sorted(all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
