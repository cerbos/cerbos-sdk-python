# Copyright 2021-2022 Zenauth Ltd.
# SPDX-License-Identifier: Apache-2.0

import importlib.metadata
import pkgutil

__version__ = importlib.metadata.version(__package__ or __name__)
__path__ = pkgutil.extend_path(__path__, __name__)
