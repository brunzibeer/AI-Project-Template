import os
import os.path as osp

def create_folders(args):
    FOLDER_NAMES = ['.data', '.output', 'dataset', 'models', 'utils']

    # For each folder name, check if it exists, if not, create it
    for folder_name in FOLDER_NAMES:
        if not osp.exists(osp.join(args.project_path, folder_name)):
            os.makedirs(osp.join(args.project_path, folder_name))