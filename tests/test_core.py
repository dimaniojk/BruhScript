import unittest
from src.bruhscript.core import interpret_bruhscript

class TestBruhScript(unittest.TestCase):
    def test_basic_arithmetic(self):
        code = '''
        bruh start
        set x 10
        set y 20
        add x y result
        bruh end
        '''
        # Ensure no exceptions are raised
        interpret_bruhscript(code)

if __name__ == '__main__':
    unittest.main()
