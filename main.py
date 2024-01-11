import os
import argparse
import modules

def main():
    '''
        PLEASE READ THIS BEFORE RUNNING THE SCRIPT
        This script makes use of the os.getcwd() function to get the current working directory.
        This function returns the path of the current working directory, which is the directory from which the script is being run.
        This means that if you run the script from the ai-template directory, the root path will be the ai-template directory.
        
        RUN THIS IN YOUR GENERAL WORKSPACE DIRECTORY OR OVERRIDE THE --root-path ARGUMENT WITH THE PATH TO YOUR GENERAL WORKSPACE DIRECTORY
    '''
    parser = argparse.ArgumentParser(description='AI Template')
    parser.add_argument('--root-path', default=os.getcwd(), help='Directory where the project will be created')
    parser.add_argument('--repo-name', help='Name of the repo, this is the name of the directory created in the root path')
    parser.add_argument('--project-name', help='Name of the project, this is the name of a project inside a directory')
    parser.add_argument('--initialized', default=True, help='This indicates wheter the root folder already exists or not')
    args = parser.parse_args()

    modules.initialize(args)

if __name__ == '__main__':
    main()