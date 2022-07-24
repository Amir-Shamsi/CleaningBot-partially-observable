class Data:
    @staticmethod
    def get_data(filename: str = None, dataline=5):
        file = None
        if filename is not None: file = open(filename, 'r')
        bot_pos = list(map(int, (file.readline() if file is not None else input()).strip().split()))
        cw_data = [input().strip() for _ in range(dataline)] if file is None else [file.readline() for _ in range(dataline)]
        height, width = dataline, len(cw_data[0])

        return bot_pos, cw_data, height, width