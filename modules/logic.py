import os.path as osp
import modules

def initialize(args):
    # Ensuring that if --initialized is True, the repo is already initialized
    if args.initialized:
        assert osp.exists(osp.join(args.root_path, args.repo_name)) and osp.isdir(osp.join(args.root_path, args.repo_name)), 'The root directory does not exist, initialize the repo first'
        assert osp.exists(osp.join(args.root_path, args.repo_name, '.gitignore')) and osp.isfile(osp.join(args.root_path, args.repo_name, '.gitignore')), 'The .gitignore file does not exist, initialize the repo first'

    # Adding the default project path
    if args.project_name:
        args.project_path = osp.join(args.root_path, args.repo_name, args.project_name)
    else:
        args.project_path = osp.join(args.root_path, args.repo_name)

    # Create all the folders and files
    modules.create_folders(args)
    modules.create_files(args)
    modules.create_main_file(args)