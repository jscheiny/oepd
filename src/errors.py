class UnsolvableParamsError(Exception):
    def __init__(self, reason):
        self.msg = reason

    @staticmethod
    def missingStat(stat):
        return UnsolvableParamsError('Missing statistic ' + stat)