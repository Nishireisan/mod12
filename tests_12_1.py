import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        gog = runner.Runner('Den')
        for _ in range(0, 10):
            gog.walk()
        self.assertEqual(gog.distance, 50)

    def test_run(self):
        hoh = runner.Runner('Sam')
        for _ in range(0, 10):
            hoh.run()
        self.assertEqual(hoh.distance, 100)

    def test_challenge(self):
        ded = runner.Runner('Ben')
        tot = runner.Runner('Pit')
        for _ in range(0, 10):
            ded.run()
            tot.walk()
        self.assertNotEqual(ded.distance, tot.distance)


if __name__ == "__main__":
    unittest.main()
