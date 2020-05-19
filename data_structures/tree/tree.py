"""The abstract base class for the custom implementations of all tree type data
structures.
"""
from __future__ import annotations
from typing import TypeVar, Generic, Sequence
from abc import ABC, abstractmethod


GT = TypeVar('GT')
"""type: The generic type to represent the element type of the binary tree."""


class TreeNode(Generic[GT], ABC):
    # pylint: disable=too-few-public-methods
    """The abstract base class for all different kinds of a tree. This ABC only
    defines two properties, the stored value and all the children nodes in a
    list.
    """

    def __init__(self, val: GT):
        self.val = val

    @property
    @abstractmethod
    def children(self) -> Sequence[TreeNode[GT]]:
        """All the children nodes in a list.

        Returns:
            All the children nodes in a list
        """

Tree = TreeNode
"""type: type alias for a general tree, as a tree is represented by its root"""
