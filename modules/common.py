DATASET_FILE = '''
#! ADD YOUR OWN DATASETS HERE !#
'''

TRANSFORMS_FILE = '''
#! ADD YOUR OWN TRANSFORMS HERE !#
'''

TRAIN_FILE = '''import os
import torch
import models
import dataset
from tqdm import tqdm

def adjust_learning_rate(optimizer, epoch, args):
    pass

def train(args):
    model = None
    loss = None
    optimizer = None

    dataset = None
    dataloader = None

    model.train()
    for epoch in tqdm(range(args.epochs)):
        for batch_idx, (data, target) in enumerate(dataloader):
            optimizer.zero_grad()
            adjust_learning_rate(optimizer, epoch, args)

            output = model(data)
            loss = loss(output, target)
            loss.backward()
            optimizer.step()     
        
        # Validate the model
        models.validate(model, loss, args)
'''

VALIDATE_FILE = '''import os
import torch
import models
import dataset

def validate(model, loss, args):
    dataset = None
    dataloader = None

    model.eval()
    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(dataloader):
            output = model(data)
            loss = loss(output, target)
'''

TEST_FILE = '''import os
import torch
import models
import dataset

def test(model, args):
    dataset = None
    dataloader = None

    model.eval()
    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(dataloader):
            output = model(data)
'''

NETWORK_FILE = '''#! ADD YOUR OWN NETWORKS HERE !#'''

LOSS_FILE = '''#! ADD YOUR OWN LOSSES HERE !#'''

COMMON_FILE = '''#! ADD YOUR OWN CONSTANTS HERE !#'''

CONFIG_FILE = '''#! ADD YOUR OWN CONFIGURATIONS HERE !#'''

MISC_FILE = '''#! ADD YOUR OWN FUNCTIONS HERE !#'''

MAIN_FILE = '''import os
import os.path as osp
import argparse
import random
import torch
import numpy as np
import models

def main():
    parser = argparse.ArgumentParser(description='AI Template')
    # Generic arguments for each project
    parser.add_argument('--root-path', default=os.getcwd(), help='Directory where the project will be created')
    parser.add_argument('--repo-name', help='Name of the repo, this is the name of the directory created in the root path')
    parser.add_argument('--project-name', help='Name of the project, this is the name of a project inside a directory')
    parser.add_argument('--data-folder', default='.data', help='Name of the data folder')
    parser.add_argument('--output-folder', default='.output', help='Name of the output folder')
    parser.add_argument('--learning-rate', default=0.01, help='Learning rate for the optimizer')
    parser.add_argument('--momentum', default=0.5, help='Momentum for the optimizer')
    parser.add_argument('--weight-decay', default=0.0005, help='Weight decay for the optimizer')
    parser.add_argument('--epochs', default=10, help='Number of epochs to train the model')
    parser.add_argument('--batch-size', default=32, help='Batch size for the data loader')
    parser.add_argument('--num-workers', default=2, help='Number of workers for the data loader')
    parser.add_argument('--seed', default=1, help='Seed for the random number generator')
    parser.add_argument('--run-mode', default='train', choices=['train_src', 'test_src', 'train_tgt', 'test_tgt', 'full'], help='Run mode for the script, this can be train, validate or test')
    parser.add_argument('--debug-mode', action='store_true', help='Run the script in debug mode')
    parser.add_argument('--create-txt', action='store_true', help='Create the dataset txt files')
    args = parser.parse_args()

    # Set the seed
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed(args.seed)

    # Set paths based on the OS
    if args.windows_debugger:
        args.main_path = osp.join(args.root_path, args.repo_name, args.project_name)
    else:
        args.main_path = args.root_path

    # Set the other paths once the main path is set
    args.data_path = osp.join(args.main_path, args.data_folder)
    args.output_path = osp.join(args.main_path, args.output_folder)
    #! ADD YOUR OWN PATHS HERE !#

    # Based on the run mode, run the corresponding function/s
    if args.run_mode == 'train':
        # Train the model
        models.train(args)
    elif args.run_mode == 'test':
        # Test the model
        models.test(args)
    elif args.run_mode == 'full':
        # Train the model
        models.train(args)
        # Test the model
        models.test(args)

if __name__ == '__main__':
    main()
'''

FILES_DICT = {
    'dsets.py': DATASET_FILE,
    'transforms.py': TRANSFORMS_FILE,
    'network.py': NETWORK_FILE,
    'loss.py': LOSS_FILE,
    'train.py': TRAIN_FILE,
    'validate.py': VALIDATE_FILE,
    'test.py': TEST_FILE,
    'common.py': COMMON_FILE,
    'config.py': CONFIG_FILE,
    'misc.py': MISC_FILE,
    'main.py': MAIN_FILE
}

DATASET_FILE = '''from dataset.dsets import *
from dataset.transforms import *
'''

MODELS_FILE = '''from models.network import *
from models.loss import *
from models.train import *
from models.validate import *
from models.test import *
'''

UTILS_FILE = '''from utils.common import *
from utils.config import *
from utils.misc import *
'''

INIT_DICT = {
    'dataset': DATASET_FILE,
    'models': MODELS_FILE,
    'utils': UTILS_FILE
}
