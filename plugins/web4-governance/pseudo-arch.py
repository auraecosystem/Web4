class LCTNode:
    def __init__(self, id):
        self.id = id
        self.history = []
        self.trust = 0.5

class TrustEngine:
    def update(self, node, success):
        node.trust += 0.01 if success else -0.02

class HardboundRuntime:
    def execute(self, action):
        if action.trust > 0.6:
            return action.run()
        return "rejected"
