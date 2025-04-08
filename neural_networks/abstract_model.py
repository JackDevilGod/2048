from abc import ABC, abstractmethod

from torch import nn
import torch


class abstract_model(nn.Module, ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @abstractmethod
    def forward(self) -> torch.Tensor:
        pass

    @abstractmethod
    def reset_game(self) -> None:
        """
        Function to reset the model to prepare for a new game.
        """
        pass
