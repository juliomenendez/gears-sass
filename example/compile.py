import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(ROOT_DIR, '..')))

from gears.environment import Environment
from gears.finders import FileSystemFinder

from gears_sass import SASSCompiler


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

env = Environment(root=STATIC_DIR, public_assets=(r'.*\.css',), fingerprinting=False)
env.finders.register(FileSystemFinder([ASSETS_DIR]))
env.compilers.register('.scss', SASSCompiler().as_handler())
env.register_defaults()


if __name__ == '__main__':
    env.save()
