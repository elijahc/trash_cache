import pandas as pd
import numpy as np
import json
import os

__version__ = '0.0.1'
class TrashCache():
    def __init__(self, manifest_fp='./tpc/trash_cache_manifest.json'):
        self.manifest_fp = os.path.abspath(manifest_fp)
        self.base_path = os.path.dirname(self.manifest_fp)
        
        # mk cache path
        if os.path.exists(self.base_path) is False:
            os.makedirs(self.base_path)
        
        # mk manifest_fp path
        if os.path.isfile(self.manifest_fp) is False:
            json.dump({},open(self.manifest_fp,'a'))

        self.manifest = json.load(open(self.manifest_fp,'r'))

    def _save_exp(self, exp):
        exp_fp = os.path.join(self.exps_fp,str(exp['id']))
        print('exp_fp: ',exp_fp)
        for v in exp['vars']:
            print('saving...',v['name'])
        
    def save_experiments(self, experiments):
        self.exps_fp = os.path.join(self.base_path,'exps')
        if os.path.exists(self.exps_fp) is False:
            os.makedirs(self.exps_fp)
        for e in experiments:
            self._save_exp(e)

    def load_experiments(self, exp_ids):
        
        for exp_id in exp_ids:
            exp_dict = self.manifest[exp_id]
            # for k,v in exp_dict.iteritems()
