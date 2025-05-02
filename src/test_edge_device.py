import unittest

from edge_device import EdgeDevice

class TestEdgeDevice(unittest.TestCase):
    def test_repr(self):
        edge = EdgeDevice("172.20.10.3")
        self.assertEqual(
                edge.__repr__(),
                "EdgeDevice(172.20.10.3)",
                )

if __name__ == "__main__":
    unittest.main()
