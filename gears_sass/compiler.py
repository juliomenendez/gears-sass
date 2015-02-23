import os
import sys

from gears.compilers import ExecCompiler


class SASSCompiler(ExecCompiler):
    result_mimetype = 'text/css'
    executable = 'sass'
    params = ['--scss']

    def __init__(self, *args, **kwargs):
        self.paths = []
        super(SASSCompiler, self).__init__(*args, **kwargs)

    def __call__(self, asset):
        self.asset = asset
        super(SASSCompiler, self).__call__(asset)

    def run(self, src):
        return super(SASSCompiler, self).run(src)

    def get_args(self):
        args = super(SASSCompiler, self).get_args()
        args.extend(map(lambda x: '-I' + x, self.asset.attributes.environment.paths))
        args.append('-I' + os.path.dirname(self.asset.absolute_path))
        return args
