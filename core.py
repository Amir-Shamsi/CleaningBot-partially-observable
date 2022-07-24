from model import Model


class CleaningAgent(Model):
    model_filename = 'memory/bot-model-w.txt'
    cleanup_flag = False

    def __init__(self, filename: str = None):
        super().__init__(self.model_filename, filename)
        self._update_model()

    def _get_next_pos(self, board):
        posx, posy = self.bot_pos
        positions = [[i, j] for i in range(self.height) for j in range(self.width) if board[i][j] == self.signs['dirty']]
        nearest_paths = [math.sqrt(((positions[i][0] - posx) ** 2) + ((positions[i][1] - posy) ** 2)) for i in range(len(positions))]
        if len(nearest_paths) > 0: return [x for (y, x) in sorted(zip(nearest_paths, positions))][0]
        positions = [[i, j] for i in range(self.height) for j in range(self.width) if board[i][j] == self.signs['invisible']]
        nearest_paths = [math.sqrt(((positions[i][0] - posx) ** 2) + ((positions[i][1] - posy) ** 2)) for i in range(len(positions))]
        if len(nearest_paths) > 0: return [x for (y, x) in sorted(zip(nearest_paths, positions))][0]
        else: return list()

    def run(self):
if __name__ == '__main__':
    action = CleaningAgent().run()
    print(action)