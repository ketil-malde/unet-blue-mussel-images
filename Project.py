#!/usr/bin/python3

import os
import os.path

model='git:...'
dataset='git:...'

class Project:

    def setup():
        '''Get data and model repositories'''
        os.system(f'git clone {model}')
        sys.path.insert(1, os.path.basename(dataset))
        import Model
        self.m = Model.Model()
        os.path.remove(os.path.basename(dataset))

        os.system(f'git clone {dataset}')
        sys.path.insert(1, os.path.basename(dataset))
        import Data
        self.d = Data.Data()
        os.path.remove(os.path.basename(dataset))

    def get_data():
        '''Download and verify data'''
        d.get()
        d.validate()

    def build_model():
        '''Build the model and check it'''
        sys.path.insert(os.path.basename(model))
        m.build()
        m.check()

    def train_model():
        '''Train the model'''
        m.train()

