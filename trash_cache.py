import pandas as pd
import numpy as np
import json
import os

class TrashCache():
    def __init__(self, manifest_file='./tpc/trash_cache_manifest.json'):
        self.manifest_file = os.path.abspath(manifest_file)
        self.base_path = os.path.dirname(self.manifest_file)
        if ~os.path.exists(self.base_path):
            os.makedirs(self.base_path)