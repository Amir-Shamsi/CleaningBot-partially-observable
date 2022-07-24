import os

class Model:
    signs = {'bot': 'b', 'dirty': 'd', 'empty': '-', 'invisible': 'o'}

    def __init__(self, model_filename, filename):
        self.model_filename = model_filename
    def _update_model(self):
        if os.path.isfile(self.model_filename):
            posr, posc = self.bot_pos
            lenr, lenc = self.height, self.width
            obsx_range = range(0 if posr - 1 < 0 else posr - 1, (lenr - 1 if posr + 1 > lenr - 1 else posr + 1) + 1)
            obsy_range = range(0 if posc - 1 < 0 else posc - 1, (lenc - 1 if posc + 1 > lenc - 1 else posc + 1) + 1)
            with open(self.model_filename, 'r+') as f:
                pw_data = [list(line) for line in f.read().split('\n')]
                for r in obsx_range:
                    for c in obsy_range:
                        if self.bot_pos == [r, c] and pw_data[r][c] == self.signs['dirty']:
                            pw_data[r][c] = self.signs['empty']
                            self.cleanup_flag = True
                            continue
                        if pw_data[r][c] != self.signs['invisible']: continue
                        pw_data[r][c] = self.cw_data[r][c] if self.cw_data[r][c] != self.signs['bot'] else self.signs['empty']
                f.seek(0)
                f.write('\n'.join([''.join(line) for line in pw_data]))
                f.truncate()
        else:
            self._save_model()

