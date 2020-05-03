class Table:
    instance = None

    def __init__(self, val):
        self.val = val

    def get_instance(self, val):
        if not Table.instance:
            self.instance = Table(val)