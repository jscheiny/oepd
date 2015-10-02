class MissingStatError(Exception):
    def __init__(self, stat, distro):
        self.msg = 'Cannot solve for params without stat %s' % (distro, stat.value)