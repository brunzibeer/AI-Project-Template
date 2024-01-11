import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='AI Template')
    parser.add_argument('--root-path', help='Directory where the project will be created')
    parser.add_argument('--project-name', help='Name of the project, this will be the name of the directory created in the root path')
    parser.add_argument('--initialized-repo', default=True, help='This indicates wheter the root folder already exists or not')
    args = parser.parse_args()

if __name__ == '__main__':
    main()