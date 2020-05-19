"""Test suite for the sub classes of the BinaryTree abstract base class.

These sub classes are the custom implementations of binary tree type data
structures. A binary tree can be implemented by linked nodes or by an array.
This module tests the correctness of these custom implementations.

A third-party library, `binarytree`, has been used to provide a correct
implementation as the reference for the tests.
"""
from typing import Type
import pytest
from binarytree import tree, Node
from data_structures.tree import BinaryTree, LinkedBinaryTree, ArrayBinaryTree


class TestBinaryTree():
    """The test suite class for subclasses of BinaryTree."""

    TRAVERSE_OPS_MAPPING = [
        ('pre_order_traverse_recursive', 'preorder'),
        ('in_order_traverse_recursive', 'inorder'),
        ('post_order_traverse_recursive', 'postorder'),
        ('level_order_traverse_iterative', 'levelorder'),
        ('pre_order_traverse_iterative', 'preorder'),
        ('in_order_traverse_iterative', 'inorder'),
        ('post_order_traverse_iterative', 'postorder'),
    ]
    """The mapping pairs between the operations of BinaryTree and the operations
        of reference implementation."""

    @staticmethod
    def check_all_traverse(target: BinaryTree, ref: Node):
        """Check all traverse implementations are correct."""
        if target or ref:
            for op_target, op_ref in TestBinaryTree.TRAVERSE_OPS_MAPPING:
                traverse_target = getattr(target, op_target)()
                traverse_ref = [n.value for n in getattr(ref, op_ref)]
                assert traverse_target == traverse_ref

    @staticmethod
    def check_tree_and_sub_tree(target: BinaryTree, ref: Node):
        """Check all traverses of the target tree are correct."""
        if target or ref:
            TestBinaryTree.check_all_traverse(target, ref)

    @staticmethod
    def random_test(tree_cls: Type[BinaryTree], height: int = 3) -> BinaryTree:
        """Test the correctness with a randomly generated tree."""
        ref = tree(height=height)
        target = tree_cls.from_list_repr(ref.values)
        TestBinaryTree.check_tree_and_sub_tree(target, ref)

    @pytest.mark.parametrize('height', (3, 5))
    @pytest.mark.parametrize('n_checks', (1000,))
    def test_linked_binary_tree(self, height: int, n_checks: int):
        """Test the correctness of LinkedBinaryTree."""
        for _ in range(n_checks):
            self.random_test(LinkedBinaryTree[int], height)

    @pytest.mark.parametrize('height', (3, 5))
    @pytest.mark.parametrize('n_checks', (1000,))
    def test_array_binary_tree(self, height: int, n_checks: int):
        """Test the correctness of ArrayBinaryTree."""
        for _ in range(n_checks):
            self.random_test(ArrayBinaryTree[int], height)
