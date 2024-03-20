from abc import ABC, abstractmethod


class IChessman(ABC):
    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def go_to_position(self, new_position):
        pass
