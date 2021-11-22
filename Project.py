#!/usr/bin/python3

import os
import os.path
import sys

model='--branch standardize git@github.com:ketil-malde/Pytorch-UNet'
dataset='git@github.com:ketil-malde/blue-mussel-drone-testdata'

# default configuration
config = {
    'runtime': '--gpus device=0'  # or just '' for CPU
}

class Project:

    def __init__(self, conf):
        self.m = None
        self.d = None
        self.config = conf

    def setup(self):
        '''Get data and model repositories'''
        os.system(f'git clone {model}')
        self.config['modelpath'] = os.path.basename(model)
        os.system(f'git clone {dataset}')
        self.config['datapath'] = os.path.basename(dataset)

        sys.path.insert(1, self.config['modelpath'])
        import Model
        self.m = Model.Model(self.config)
        sys.path.remove(self.config['modelpath'])

        sys.path.insert(1, self.config['datapath'])
        import Data
        self.d = Data.Data(self.config)
        sys.path.remove(self.config['datapath'])

    def get_data(self):
        '''Download and verify data'''
        self.d.get()
        self.d.validate()

    def build_model(self):
        '''Build the model and check it'''
        self.m.build()
        self.m.check()

    def train_model(self):
        '''Train the model'''
        self.m.train()

config = {
    # Configuration items here
    }

if __name__ == '__main__':
    p = Project(config)
    p.setup()
    p.build_model()
    p.get_data()
    p.train_model()
