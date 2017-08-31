from pprint import pprint as pp
from trash_cache import TrashCache

tc = TrashCache()
pp(vars(tc))

exps = [
        {
            'id': 12345,
            'vars': [
                {
                    'name':'corr_matrix',
                    'data':[1,2,3,4,5]
                    }
                ]
            }
        ]

tc.save_experiments(experiments=exps)

vals = tc.load_experiments([12345])
pp(vals)
