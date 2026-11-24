import unittest,tempfile,pathlib,runpy
m=runpy.run_path(str(pathlib.Path(__file__).resolve().parents[1]/'tools/replay_both.py'))
class Tests(unittest.TestCase):
 def test_runner(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);system=p/'s';system.write_text('synthetic')
   a=p/'a.py';b=p/'b.py';a.write_text("print({'covered':True})");b.write_text("print({'covered':True})")
   self.assertEqual(m['replay'](system,[a,b])['status'],'both_accept')
   b.write_text("print('not a verdict')");self.assertEqual(m['replay'](system,[a,b])['status'],'unresolved')
   b.write_text('raise SystemExit(1)');self.assertEqual(m['replay'](system,[a,b])['status'],'unresolved')
   with self.assertRaises(ValueError):m['replay'](system,[a,a])
if __name__=='__main__':unittest.main()
