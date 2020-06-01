from abc import abstractmethod


class Query():

    def __init__(self):
        pass

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def names(self):
        """ Return a short name (slug) and a more descriptive name """
        return ("", "")

    @abstractmethod
    def inputs(self):
        return []

    @abstractmethod
    def fetch(self, params, offset=-1, limit=-1):
        return []
