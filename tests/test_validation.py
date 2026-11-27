import contextlib
import io
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"tools"))
import validate

class ValidationTests(unittest.TestCase):
    def test_development(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate.check_project(),0)

    def test_release(self):
        expected = 0 if all((validate.PACK/p).is_file() for p in validate.BASE) else 2
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate.check_project(release=True),expected)

    def test_include_cycle(self):
        documents = {"content.json":{"Changes":[{"Action":"Include","FromFile":"content.json"}]}}
        with self.assertRaisesRegex(ValueError,"Include circular"):
            list(validate.patches(documents))

    def test_duplicate_json_keys(self):
        with self.assertRaisesRegex(ValueError,"duplicada"):
            validate.unique_object([("id",0),("id",1)])

    def test_connected_walkable_tiles(self):
        self.assertEqual(validate.reachable((0,0),{(0,0),(1,0),(3,0)}),{(0,0),(1,0)})

if __name__ == "__main__":
    unittest.main()
