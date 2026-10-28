import unittest,tempfile,pathlib,runpy
m=runpy.run_path(str(pathlib.Path(__file__).resolve().parents[1]/'tools/compare_transcriptions.py'))
HEADER='# source: synthetic fixture\n# link: https://example.org/fixture\n# pages: 1\n# transcribed by: fixture A\n# minimum modulus: 2\n'
class Tests(unittest.TestCase):
 def test_compare(self):
  with tempfile.TemporaryDirectory() as d:
   a=pathlib.Path(d)/'a';b=pathlib.Path(d)/'b';a.write_text(HEADER+'0 mod 2\n1 mod 3\n');b.write_text(HEADER+'1 mod 3\n0 mod 2\n')
   self.assertTrue(m['compare'](a,b)['agree'])
   b.write_text(HEADER+'0 mod 2\n2 mod 3\n');self.assertFalse(m['compare'](a,b)['agree'])
   b.write_text(HEADER+'0 mod 2\n1 mod 2\n')
   with self.assertRaises(ValueError):m['read'](b)
   b.write_text('0 mod 2\n')
   with self.assertRaises(ValueError):m['read'](b)
if __name__=='__main__':unittest.main()
