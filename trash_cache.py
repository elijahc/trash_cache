import json
import os
import pickle

import pandas as pd
import numpy as np


__version__ = '0.0.2'
class TrashCache():
    def __init__(self, manifest_fp='./tpc/trash_cache_manifest.json'):
        self.manifest_fp = os.path.abspath(manifest_fp)
        self.base_path = os.path.dirname(self.manifest_fp)
        
        # mk cache path
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        
        # mk manifest_fp path
        if not os.path.isfile(self.manifest_fp):
            json.dump({},open(self.manifest_fp,'w+'))

        self.manifest = json.load(open(self.manifest_fp,'r'))

    def _save_exp(self, exp):
        exp_fp = os.path.join(self.exps_fp,str(exp['id']))
        print('exp_fp: ',exp_fp)
        manifest_vars = []

        if not os.path.exists(exp_fp):
            os.makedirs(exp_fp)
        for v in exp['vars']:
            vpath = os.path.join(exp_fp,v['name'])
            print('saving...',vpath)

            if isinstance(v['data'],pd.DataFrame):
                vpath = vpath + '.df'
                v['data'].to_pickle(vpath)
            elif isinstance(v['data'],np.ndarray):
                vpath = vpath + '.nda'
                v['data'].dump(vpath)
            else:
                vpath = vpath + '.pk'
                pickle.dump(v['data'],open(vpath,'w+'))
            
            v['fp'] = vpath

            manifest_vars.append({v['name']:vpath})

        self.manifest[ str(exp['id']) ] = manifest_vars
        
    def save_experiments(self, experiments):
        self.exps_fp = os.path.join(self.base_path,'exps')
        if os.path.exists(self.exps_fp) is False:
            os.makedirs(self.exps_fp)
        for e in experiments:
            self._save_exp(e)
        
        json.dump(self.manifest,open(self.manifest_fp,'w+'))

    def load_vars(self,exp_id,verbose=False):
        values = {}
        for v in self.manifest[ str(exp_id) ]:
            name = v.keys()[0]
            fp = v.values()[0]
            extension = fp.split('.')[1]
            
            
            if extension is '.df':
                if verbose:
                    print('loading dataframe...',fp)
                values[name] = pd.read_pickle(fp)

            elif extension is '.nda':
                if verbose:
                    print('loading ndarray...',fp)
                values[name] = np.load(fp)

            else:
                if verbose:
                    print('loading pickle...',fp)
                values[name] = pickle.load(open(fp,'r'))

        return values

    def load_experiments(self, exp_ids,verbose=False):
        return [self.load_vars(eid,verbose) for eid in exp_ids]