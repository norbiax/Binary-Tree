class NewNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    @property
    def node_property(self):
        return '{}'.format(self.key)
