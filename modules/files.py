import os.path as osp
import modules

def create_files(args):
    FOLDER_NAMES = ['dataset', 'models', 'utils']
    FILE_NAMES = {
        'dataset': ['__init__.py', 'dsets.py', 'transforms.py'],
        'models': ['__init__.py', 'network.py', 'loss.py', 'train.py', 'validate.py', 'test.py'],
        'utils': ['__init__.py', 'common.py', 'config.py', 'misc.py']
    }

    # Create each file in the corresponding folder
    for folder_name in FOLDER_NAMES:
        for file_name in FILE_NAMES[folder_name]:
            with open(osp.join(args.project_path, folder_name, file_name), 'w') as f:
                # Check if it is the __init__.py file
                if file_name == '__init__.py':
                    f.write(modules.INIT_DICT[folder_name])
                else:
                    f.write(modules.FILES_DICT[file_name])

def create_main_file(args):
    with open(osp.join(args.project_path, 'main.py'), 'w') as f:
        f.write(modules.MAIN_FILE)