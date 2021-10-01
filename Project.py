#!/usr/bin/python3

import os
import os.path
import sys

model='--branch standardize https://github.com/ketil-malde/Pytorch-UNet'
dataset='git://github.com/ketil-malde/blue-mussel-drone-testdata'

class Project:

    def __init__(self):
        self.m = None
        self.d = None
        self.config = {}

    def setup(self):
        '''Get data and model repositories'''
        os.system(f'git clone {model}')
        self.config['modelpath'] = os.path.basename(model)
        sys.path.insert(1, self.config['modelpath'])
        import Model
        self.m = Model.Model()
        sys.path.remove(self.config['modelpath'])

        os.system(f'git clone {dataset}')
        self.config['datapath'] = os.path.basename(dataset)
        sys.path.insert(1, self.config['datapath'])
        import Data
        self.d = Data.Data()
        sys.path.remove(self.config['datapath'])

    def get_data(self):
        '''Download and verify data'''
        self.d.get(self.config)
        self.d.validate(self.config)

    def build_model(self):
        '''Build the model and check it'''
        self.m.build(self.config)
        self.m.check(self.config)

    def train_model(self):
        '''Train the model'''
        self.m.train(self.config)


if __name__ == '__main__':
    p = Project()
    p.setup()
    p.build_model()
    p.get_data()
    p.train_model()

    print(dir(p))
