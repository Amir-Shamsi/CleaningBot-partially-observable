
class CleaningAgent(Model):
    model_filename = 'memory/bot-model-w.txt'
    def __init__(self, filename: str = None):
    def run(self):
if __name__ == '__main__':
    action = CleaningAgent().run()
    print(action)