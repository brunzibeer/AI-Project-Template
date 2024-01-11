import os.path as osp

def create_files(args):
    FOLDER_NAMES = ['dataset', 'models', 'utils']
    FILE_NAMES = {
        'dataset': ['dsets.py', 'transforms.py'],
        'models': ['network.py', 'loss.py', 'train.py', 'validate.py', 'test.py'],
        'utils': ['common.py', 'config.py', 'misc.py']
    }

    # Create each file in the corresponding folder
    for folder_name in FOLDER_NAMES:
        for file_name in FILE_NAMES[folder_name]:
            with open(osp.join(args.project_path, folder_name, file_name), 'w') as f:
                pass

def create_main_file(args):
    pass