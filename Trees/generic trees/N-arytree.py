#N-ary tree each node has atleast n nodes

##this is a 6-ary tree
class SixAryTree:
    def __init__(self, data):
        self.data =data
        self.first_child = None
        self.second_child = None
        self.third_child = None
        self.fourth_child = None
        self._fifth_child = None
        self.sixth_child = None


class GenericTree:
    def __init__(self,data):
        self.data = data
        self.first_child = None
        self.next_sibling = None

        