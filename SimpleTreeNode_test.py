import unittest
import SimpleTree_ForTest


class MyTestCase(unittest.TestCase):
    def test_AddChild(self):
        node1 = SimpleTree_ForTest.SimpleTreeNode(1, None)
        node2 = SimpleTree_ForTest.SimpleTreeNode(2, None)
        node3 = SimpleTree_ForTest.SimpleTreeNode(3, None)
        node4 = SimpleTree_ForTest.SimpleTreeNode(4, None)
        node5 = SimpleTree_ForTest.SimpleTreeNode(5, None)
        node6 = SimpleTree_ForTest.SimpleTreeNode(6, None)
        node7 = SimpleTree_ForTest.SimpleTreeNode(7, None)
        node8 = SimpleTree_ForTest.SimpleTreeNode(8, None)
        node9 = SimpleTree_ForTest.SimpleTreeNode(9, None)
        graf = SimpleTree_ForTest.SimpleTree(node1)
        self.assertEqual(graf.LeafCount(), 1)
        self.assertEqual(graf.Count(), 1)
        graf.AddChild(node1, node2)
        graf.AddChild(node1, node3)
        graf.AddChild(node2, node4)
        graf.AddChild(node2, node5)
        graf.AddChild(node5, node6)
        graf.AddChild(node5, node7)
        graf.AddChild(node3, node8)
        graf.AddChild(node8, node9)
        self.assertEqual(graf.LeafCount(), 4)
        self.assertEqual(graf.Count(), 9)

    def test_DeleteNode(self):
        node1 = SimpleTree_ForTest.SimpleTreeNode(1, None)
        node2 = SimpleTree_ForTest.SimpleTreeNode(2, None)
        node3 = SimpleTree_ForTest.SimpleTreeNode(3, None)
        node4 = SimpleTree_ForTest.SimpleTreeNode(4, None)
        node5 = SimpleTree_ForTest.SimpleTreeNode(5, None)
        node6 = SimpleTree_ForTest.SimpleTreeNode(6, None)
        node7 = SimpleTree_ForTest.SimpleTreeNode(7, None)
        node8 = SimpleTree_ForTest.SimpleTreeNode(8, None)
        node9 = SimpleTree_ForTest.SimpleTreeNode(9, None)
        graf = SimpleTree_ForTest.SimpleTree(node1)
        graf.AddChild(node1, node2)
        graf.AddChild(node1, node3)
        graf.AddChild(node2, node4)
        graf.AddChild(node2, node5)
        graf.AddChild(node5, node6)
        graf.AddChild(node5, node7)
        graf.AddChild(node3, node8)
        graf.AddChild(node8, node9)
        self.assertEqual(graf.LeafCount(), 4)
        self.assertEqual(graf.Count(), 9)
        graf.DeleteNode(node3)
        self.assertEqual(graf.LeafCount(), 3)
        self.assertEqual(graf.Count(), 6)
        graf.DeleteNode(node7)
        self.assertEqual(graf.LeafCount(), 2)
        self.assertEqual(graf.Count(), 5)

    def test_DeleteNodeNone(self):
        node1 = SimpleTree_ForTest.SimpleTreeNode(1, None)
        graf = SimpleTree_ForTest.SimpleTree(node1)
        self.assertEqual(graf.LeafCount(), 1)
        self.assertEqual(graf.Count(), 1)
        graf.DeleteNode(node1)
        self.assertEqual(graf.LeafCount(), 0)
        self.assertEqual(graf.Count(), 0)

    def test_GetAllNodes(self):
        node1 = SimpleTree_ForTest.SimpleTreeNode(1, None)
        node2 = SimpleTree_ForTest.SimpleTreeNode(2, None)
        node3 = SimpleTree_ForTest.SimpleTreeNode(3, None)
        node4 = SimpleTree_ForTest.SimpleTreeNode(4, None)
        node5 = SimpleTree_ForTest.SimpleTreeNode(5, None)
        node6 = SimpleTree_ForTest.SimpleTreeNode(6, None)
        node7 = SimpleTree_ForTest.SimpleTreeNode(7, None)
        node8 = SimpleTree_ForTest.SimpleTreeNode(8, None)
        node9 = SimpleTree_ForTest.SimpleTreeNode(9, None)
        graf = SimpleTree_ForTest.SimpleTree(node1)
        graf.AddChild(node1, node2)
        graf.AddChild(node1, node3)
        graf.AddChild(node2, node4)
        graf.AddChild(node2, node5)
        graf.AddChild(node5, node6)
        graf.AddChild(node5, node7)
        graf.AddChild(node3, node8)
        graf.AddChild(node8, node9)
        self.assertEqual(graf.LeafCount(), 4)
        self.assertEqual(len(graf.GetAllNodes()), 9)
        graf.DeleteNode(node3)
        self.assertEqual(graf.LeafCount(), 3)
        self.assertEqual(len(graf.GetAllNodes()), 6)
        graf.DeleteNode(node7)
        self.assertEqual(graf.LeafCount(), 2)
        self.assertEqual(len(graf.GetAllNodes()), 5)

    def test_GetAllNodesNone(self):
            graf = SimpleTree_ForTest.SimpleTree(None)
            self.assertEqual(len(graf.GetAllNodes()), 0)

    def test_FindNodesByValue(self):
        node1 = SimpleTree_ForTest.SimpleTreeNode(1, None)
        node2 = SimpleTree_ForTest.SimpleTreeNode(2, None)
        node3 = SimpleTree_ForTest.SimpleTreeNode(3, None)
        node4 = SimpleTree_ForTest.SimpleTreeNode(4, None)
        node5 = SimpleTree_ForTest.SimpleTreeNode(5, None)
        node6 = SimpleTree_ForTest.SimpleTreeNode(6, None)
        node7 = SimpleTree_ForTest.SimpleTreeNode(7, None)
        node8 = SimpleTree_ForTest.SimpleTreeNode(8, None)
        node9 = SimpleTree_ForTest.SimpleTreeNode(9, None)
        graf = SimpleTree_ForTest.SimpleTree(node1)
        graf.AddChild(node1, node2)
        graf.AddChild(node1, node3)
        graf.AddChild(node2, node4)
        graf.AddChild(node2, node5)
        graf.AddChild(node5, node6)
        graf.AddChild(node5, node7)
        graf.AddChild(node3, node8)
        graf.AddChild(node8, node9)
        self.assertEqual(graf.FindNodesByValue(4), [node4])
        self.assertEqual(graf.FindNodesByValue(8), [node8])

    def test_MoveNode(self):
        node1 = SimpleTree_ForTest.SimpleTreeNode(1, None)
        node2 = SimpleTree_ForTest.SimpleTreeNode(2, None)
        node3 = SimpleTree_ForTest.SimpleTreeNode(3, None)
        node4 = SimpleTree_ForTest.SimpleTreeNode(4, None)
        node5 = SimpleTree_ForTest.SimpleTreeNode(5, None)
        node6 = SimpleTree_ForTest.SimpleTreeNode(6, None)
        node7 = SimpleTree_ForTest.SimpleTreeNode(7, None)
        node8 = SimpleTree_ForTest.SimpleTreeNode(8, None)
        node9 = SimpleTree_ForTest.SimpleTreeNode(9, None)
        graf = SimpleTree_ForTest.SimpleTree(node1)
        graf.AddChild(node1, node2)
        graf.AddChild(node1, node3)
        graf.AddChild(node2, node4)
        graf.AddChild(node2, node5)
        graf.AddChild(node5, node6)
        graf.AddChild(node5, node7)
        graf.AddChild(node3, node8)
        graf.AddChild(node8, node9)
        graf.MoveNode(node4, node2) # если переставляемые ноды уже так и стоят graf.AddChild(node2, node4) - graf.MoveNode(node4, node2)
        self.assertEqual(node4.Parent, node2)
        self.assertEqual(node2.Children[0], node4)
        self.assertEqual(graf.LeafCount(), 4)
        self.assertEqual(node9.Parent, node8)
        self.assertEqual(node8.Children[0], node9)
        graf.MoveNode(node9, node3)
        self.assertEqual(node8.Children, [])
        self.assertEqual(node9.Parent, node3)
        self.assertEqual(node3.Children[1], node9)
        self.assertEqual(graf.LeafCount(), 5)
        #graf.MoveNode(node5, node1) проверяем начальное состояние
        self.assertEqual(node5.Children[0], node6)
        self.assertEqual(node5.Parent, node2)
        graf.MoveNode(node5, node1)
        self.assertEqual(node1.Children[2], node5)
        self.assertEqual(node5.Parent, node1)
        self.assertEqual(graf.LeafCount(), 5)



if __name__ == '__main__':
    unittest.main()