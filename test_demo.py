import unittest
import tempfile
import json
from pathlib import Path
from demo import run

class ExperimentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        cls.output=Path(cls.temp.name)/'results.json'
        cls.r=run(cls.output)
    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()
    def test_output_matches_returned_result(self):
        self.assertEqual(json.loads(self.output.read_text()),self.r)
    def test_baseline(self):
        self.assertGreater(self.r['models']['logistic']['macro_f1'], self.r['models']['majority']['macro_f1'])
    def test_split(self):
        self.assertEqual(self.r['train_rows']+self.r['test_rows'],178)
    def test_confusion(self):
        self.assertEqual(sum(map(sum,self.r['models']['forest']['confusion_matrix'])),self.r['test_rows'])

if __name__ == "__main__":
    unittest.main()
