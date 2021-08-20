import unittest


class ClassCreation(unittest.TestCase):
    def test_import_french(self):
        from card_engine.decks import french
        self.french = french


if __name__ == '__main__':
    unittest.main()
