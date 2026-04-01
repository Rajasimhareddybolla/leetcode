class Solution:
    def reorderList(self, head):
        self.left = head
        self.stop = False

        def recurse(right):
            if not right:
                return

            recurse(right.next)

            if self.stop:
                return

            if self.left == right or self.left.next == right:
                right.next = None
                self.stop = True
                return

            temp = self.left.next
            self.left.next = right
            right.next = temp
            self.left = temp

        recurse(head)