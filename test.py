import unittest

from monads import *

val_nothing: Maybe[int] = Nothing
val_int: Maybe[int] = Just(456)
val_str: Maybe[str] = Just("test")
val_left: Either[int, str] = Left(12345)
val_right: Either[int, str] = Right("Some error!")

class MyTestCase(unittest.TestCase):
    def test_maybe_just_int(self):
        match val_int:
            case Just(c):
                self.assertEqual(c, 456)
            case Nothing:
                self.assertFalse(Nothing, "Nothing pattern match in maybe does not work for int")

    def test_maybe_just_str(self):
        match val_str:
            case Just(s):
                self.assertEqual(s, "test")
            case Nothing:
                self.assertFalse(Nothing, "Nothing pattern match in maybe does not work for string")

    def test_maybe_nothing(self):
        match val_nothing:
            case Just(c):
                self.assertFalse(c, "Nothing pattern match in maybe does not work for string")
            case Nothing:
                assert True

    def test_either_left(self):
        match val_left:
            case Left(t):
                self.assertEqual(t, 12345)
            case Right(e):
                self.assertFalse(e, "Mistakenly Either returned error")

    def test_either_right(self):
        match val_right:
            case Left(t):
                self.assertFalse(t, "Mistakenly Either returned result")
            case Right(e):
                self.assertEqual(e,  "Some error!")


if __name__ == '__main__':
    unittest.main()

