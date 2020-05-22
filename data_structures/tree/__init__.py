
"""
The custom implementations of the common tree data structure.

This package includes the custom implementations of the common tree data
structures like binary tree, binary search tree, n-ary tree etc. These
implementations are only for learning purpose and have no practical usage.

All the implemented classes are flatly imported here so that one can easily
import them by `data_structure.tree.ClassName` instead of adding the module file
name before the class name in the path
"""
# binary tree
from .binary_tree import BinaryTree
from .linked_binary_tree import LinkedBinaryTree
from .array_binary_tree import ArrayBinaryTree
# binary search tree
from .binary_search_tree_mixin import BinarySearchTreeMixin
from .array_binary_search_tree import ArrayBinarySearchTree
from .linked_binary_search_tree import LinkedBinarySearchTree
