# problem: https://leetcode.com/problems/linked-list-cycle/

def has_cycle(head) -> bool:
    '''
    Em um você anda 1 no outro você anda 2
    em algum momento eles vão se encontrar
    e ai você comprova que tem um ciclo na sua
    linked list
    '''
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False