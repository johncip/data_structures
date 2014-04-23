from unittest import main, TestCase, skip

from bt import Bt


class TestBt(TestCase):
    def setUp(self):
        self.bt = Bt(4)
        [self.bt.add(e) for e in [2, 6, 3, 1, 5]]

    def test_inorder(self):
        self.assertEqual(self.bt.inorder(), range(1, 7))

    def test_unique_queue(self):
        Bt(1)
        self.assertEqual(Bt(2).inorder(), [2])

    def test_floor(self):
        x = self.bt
        for i in range(1, 7):
            self.assertEqual(x.floor(i), i)
        self.assertEqual(self.bt.floor(7), 6)
        self.assertIsNone(self.bt.floor(-1))

    def test_ceil(self):
        x = self.bt
        for i in range(1, 7):
            self.assertEqual(x.ceil(i), i)
        self.assertEqual(x.ceil(0), 1)
        self.assertIsNone(x.ceil(7))

    def test_get(self):
        x = self.bt
        self.assertIs(x.get(4), x.root)
        for i in range(1, 7):
            self.assertEqual(x.get(i).key, i)

    def test_parent(self):
        x = self.bt
        self.assertIsNone(x.parent(x.root.key))
        self.assertIs(x.get(4), x.parent(2))
        self.assertIs(x.get(4), x.parent(6))
        self.assertIs(x.get(2), x.parent(1))

    def test_height(self):
        x = self.bt
        self.assertEqual(x.height(), 3)

    def test_delete_min(self):
        for i in range(2, 8):
            self.bt.delete_min()
            self.assertEqual(self.bt.inorder(), range(i, 7))

    # def test_level_order(self):
    #     print '--------'
    #     print 'tree:'
    #     self.bt.level_order()
    #     print '--------'

    def test_delete(self):
        for i in [5, 3, 1, 2, 6, 4]:
            self.bt.delete(i)
        self.assertEqual(self.bt.inorder(), [])



if __name__ == '__main__':
    main()