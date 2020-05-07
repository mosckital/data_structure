"""Common algorithms based on the two pointer technique.

This module implements the common algorithms which uses the two pointer
technique as the foundation. The implementations are for illustration and
learning purposes so one may need to reimplement an algorithm with corresponding
modifications in actual usage.
"""
from typing import TypeVar, Generic, Optional
from data_structures.sequence import LinkedListMixin


GT = TypeVar('GT')
"""type: The generic type to represent the element type of linked list."""


class TwoPointer(Generic[GT]):
    """Class of algorithms based on the two pointer technique.

    All the algorithms are implemented as a static method of the class so one
    can call by:
    `TwoPointer.algo_name(params)`
    """

    Node = LinkedListMixin.Node
    """type: alias for the base class of the linked list nodes."""

    @staticmethod
    def move(node: Node[GT], step: int) -> Optional[Node[GT]]:
        """Move forward the given steps from the given node of a linked list.

        Note:
            This is a helper function, not an algorithm function.

        Args:
            node: the given node of a linked list, the start of the movement
            step: number of steps to move forward

        Returns:
            The node after movement or `None` if reaching the end of the list
        """
        while step and node:
            node = node.next
            step -= 1
        return node

    @staticmethod
    def has_a_cycle(seq: LinkedListMixin[GT]) -> bool:
        """Check if the given linked list has a cycle.

        The algorithm will spawn two pointers of different speeds. The faster
        one will move 2 steps in each turn while the slower one will move 1 step
        in each turn. The faster pointer will catch up the slower pointer if
        there is a cycle, otherwise it will reach the end of the list.

        Args:
            seq: the linked list

        Returns:
            `True` if the linked list has a cycle or `False` otherwise.
        """
        slow = fast = seq.get_head()
        slow_step, fast_step = 1, 2
        while fast:
            fast = TwoPointer.move(fast, fast_step)
            slow = TwoPointer.move(slow, slow_step)
            if fast == slow:
                return True
        return False

    @staticmethod
    def start_node_of_cycle(seq: LinkedListMixin[GT]) -> Optional[LinkedListMixin.Node[GT]]:
        """Get the start node of the cycle in a linked list.

        This algorithm will get the start node of the cycle if the given linked
        list has a cycle or return `None` otherwise. It uses a fast pointer and
        a slow pointer to check if there is a cycle, then uses two pointers, one
        starting from the meeting node of the fast and slow pointers and the
        other starting from the head node of the list, to find the start node of
        the cycle, which is the meeting node of these two pointers.

        Args:
            seq: the linked list

        Returns:
            The start node of the cycle if the cycle exists or `None` otherwise
        """
        slow = fast = seq.get_head()
        slow_step, fast_step = 1, 2
        # check if there is a cycle
        while fast:
            fast = TwoPointer.move(fast, fast_step)
            slow = TwoPointer.move(slow, slow_step)
            if fast == slow:
                break
        # return None if there is no cycle
        if not fast:
            return None
        # start from both the current node and the head node with a speed of one
        # step will meet at the start node of the cycle
        slow = seq.get_head()
        while fast != slow:
            fast = TwoPointer.move(fast, 1)
            slow = TwoPointer.move(slow, 1)
        return fast
