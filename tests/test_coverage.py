import importlib.util,pathlib,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(file):
 s=importlib.util.spec_from_file_location(file,ROOT/'tools'/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
A=load('check_coverage.py');B=load('check_coverage_independent.py')
GOOD='# minimum modulus: 2\n0 mod 2\n0 mod 3\n1 mod 4\n5 mod 6\n7 mod 12\n'
class Controls(unittest.TestCase):
 def run_both(self,text,ok):
  with tempfile.TemporaryDirectory()as d:
   p=pathlib.Path(d)/'system.txt';p.write_text(text)
   for fn in (A.check,B.verify):
    if ok:self.assertTrue(fn(p)['covered'])
    else:
     with self.assertRaises(ValueError):fn(p)
 def test_cover(self):self.run_both(GOOD,True)
 def test_hole(self):self.run_both(GOOD.replace('7 mod 12\n',''),False)
 def test_duplicate(self):self.run_both(GOOD+'1 mod 2\n',False)
 def test_header(self):self.run_both(GOOD.replace('modulus: 2','modulus: 3'),False)
 def test_bad_residue(self):self.run_both(GOOD+'15 mod 13\n',False)
 def test_budget(self):
  with tempfile.TemporaryDirectory()as d:
   p=pathlib.Path(d)/'s';p.write_text(GOOD)
   for fn in (A.check,B.verify):
    with self.assertRaises(ValueError):fn(p,1)
if __name__=='__main__':unittest.main()
