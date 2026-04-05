class Solution(object):
    def splitListToParts(self, head, k):
        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next
        part_size, extra = total // k, total % k
        result, curr = [], head
        for i in range(k):
            part_head = curr
            size = part_size + (1 if i < extra else 0)
            for j in range(size - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            result.append(part_head)
        return result