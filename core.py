from model import Model


class CleaningAgent(Model):
    model_filename = 'memory/bot-model-w.txt'
    def __init__(self, filename: str = None):
        super().__init__(self.model_filename, filename)
        self._update_model()
    def run(self):
if __name__ == '__main__':
    action = CleaningAgent().run()
    print(action)