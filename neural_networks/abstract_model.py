from abc import ABC, abstractmethod

from torch import nn


class abstract_model(nn.Module, ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def reset_game(self):
        pass
