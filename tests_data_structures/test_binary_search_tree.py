"""Test suite for the implementations of a binary search tree.

The most of the functions of a binary search tree are implemented by a mixin
class instead of subclassing the BinaryTree abstract base class. This mixin will
then be inherited by the actual implementation class of a binary search tree.

There are two implementations, one based on linked nodes, and the other based on
array. This module tests the correctness of these two custom implementations.

A third-party library, `binarytree`, has been used to provide a correct
implementation as the reference for the tests.
"""
from typing import Type
from random import randint, choice
from bisect import bisect
import pytest
from binarytree import build, bst
from data_structures.tree import BinarySearchTree, \
    LinkedBinarySearchTree, ArrayBinarySearchTree
from .test_binary_tree import TestBinaryTree


class TestBinarySearchTree():
    """The test suite class for the implementations of a binary search tree."""

    @staticmethod
    def construct_ref_bst_tree(target: BinarySearchTree):
        """Construct a reference tree identical to the given target tree and
        check if the generated tree is a binary search tree.

        Note:
            This function will add a random element to the given tree at the
            start of the function if the given tree is empty, to avoid raising
            errors when operating on an empty tree.
        """
        if not target.root:
            target.insert(randint(-100, 100))
        print(target.list_repr)
        tree = build(target.list_repr)
        assert tree.is_bst
        assert len(target) == len(tree)
        return tree

    @staticmethod
    def check_op_search(target: BinarySearchTree, n_random: int):
        """Check the search operation on a binary search tree."""
        tree = TestBinarySearchTree.construct_ref_bst_tree(target)
        assert not target.search(tree.min_node_value - 1)
        assert target.search(tree.min_node_value)
        assert target.search(tree.max_node_value)
        assert not target.search(tree.max_node_value + 1)
        in_order = [node.value for node in tree.inorder]
        for _ in range(n_random):
            number = randint(tree.min_node_value, tree.max_node_value)
            assert target.search(number) == (number in in_order)

    @staticmethod
    def check_op_insert_delete(target: BinarySearchTree):
        """Check the insert and delete operations on a binary search tree."""
        tree = TestBinarySearchTree.construct_ref_bst_tree(target)
        in_order = [node.value for node in tree.inorder]
        options = [
            tree.min_node_value,
            tree.max_node_value,
            tree.min_node_value - 100,
            tree.max_node_value + 100,
            (tree.min_node_value + tree.max_node_value) // 2,
            in_order[len(tree) // 2]
        ]
        target.insert(choice(options))
        tree = TestBinarySearchTree.construct_ref_bst_tree(target)
        target.delete(choice(options))
        tree = TestBinarySearchTree.construct_ref_bst_tree(target)

    @staticmethod
    def check_op_inorder_successor(target: BinarySearchTree):
        """Check the inorder_successor operation on a binary search tree."""
        tree = TestBinarySearchTree.construct_ref_bst_tree(target)
        in_order = [node.value for node in tree.inorder]
        options = [
            tree.min_node_value,
            tree.max_node_value,
            tree.min_node_value - 100,
            tree.max_node_value + 100,
            (tree.min_node_value + tree.max_node_value) // 2,
            in_order[len(tree) // 2]
        ]
        for val in options:
            ref_idx = bisect(in_order, val)
            if ref_idx == len(in_order):
                assert target.inorder_successor(val) is None
            else:
                assert target.inorder_successor(val) == in_order[ref_idx]

    @staticmethod
    def repeat_checks(
            tree_cls: Type[BinarySearchTree],
            height: int,
            n_checks: int
        ):
        """Repeatedly check the correctness of the operations of a binary search
        tree.
        """
        for _ in range(n_checks):
            ref = bst(height=height)
            target = tree_cls.from_list_repr(ref.values)
            assert target.list_repr == ref.values
            TestBinaryTree.check_tree_and_sub_tree(target, ref)
            TestBinarySearchTree.check_op_search(target, n_checks)
            TestBinarySearchTree.check_op_insert_delete(target)
            TestBinarySearchTree.check_op_inorder_successor(target)

    @pytest.mark.parametrize('height', (3,))
    @pytest.mark.parametrize('n_checks', (100,))
    def test_linked_binary_search_tree(self, height: int, n_checks: int):
        """Test the correctness of LinkedBinarySearchTree."""
        self.repeat_checks(LinkedBinarySearchTree, height, n_checks)

    @pytest.mark.parametrize('height', (3,))
    @pytest.mark.parametrize('n_checks', (100,))
    def test_array_binary_search_tree(self, height: int, n_checks: int):
        """Test the correctness of ArrayBinarySearchTree."""
        self.repeat_checks(ArrayBinarySearchTree, height, n_checks)
