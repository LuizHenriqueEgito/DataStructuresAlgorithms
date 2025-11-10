# problem: https://leetcode.com/problems/middle-of-the-linked-list/

def middle_node(head):
    '''
    Enquanto um ponteiro (head) anda 1 o outro (ahead) anda 2
    E quando o segundo chegar ao final o primeiro estará na metade
    '''
    ahead = head
    while ahead and ahead.next:
        ahead = ahead.next.next
        head = head.next
    return head