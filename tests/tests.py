import unittest
from solvers.cfop import cross, assert_cross_solved, f2l, first_pair, second_pair, third_pair, fourth_pair, \
    assert_first_pair, assert_second_pair, assert_third_pair, assert_fourth_pair, first_look_oll, \
    assert_first_look_oll, assert_oll, oll
from rubiks_cube.rubiks_cube import Cube
from utils import scramble_generator


class TestCFOP(unittest.TestCase):

    def test_01_cross(self):
        for i in range(1000):
            cube = Cube()
            scramble = scramble_generator(20)
            cube.scramble(scramble)
            cross_solution, cross_cube = cross(cube)
            self.assertTrue(assert_cross_solved(cross_cube), msg="error on scramble: \"{0}\"\ncross: \"{1}\"".
                            format(scramble, cross_solution))

    def test_02_first_pair(self):
        for i in range(1000):
            cube = Cube()
            scramble = scramble_generator(20)
            cube.scramble(scramble)
            cross_solution, cross_cube = cross(cube)
            first_pair_solution, fstp_cube = first_pair(cross_cube)
            self.assertTrue(assert_first_pair(fstp_cube), msg="error on scramble: \"{0}\"\ncross: \"{1}\"\nfirst pair: "
                                                              "\"{2}\"".
                            format(scramble, cross_solution, first_pair_solution))

    def test_03_second_pair(self):
        for i in range(1000):
            cube = Cube()
            scramble = scramble_generator(20)
            cube.scramble(scramble)
            cross_solution, cross_cube = cross(cube)
            first_pair_solution, fstp_cube = first_pair(cross_cube)
            second_pair_solution, sndp_cube = second_pair(fstp_cube)
            self.assertTrue(assert_second_pair(sndp_cube),
                            msg="error on scramble: \"{0}\"\ncross: \"{1}\"\nfirst pair: "
                                "\"{2}\"\nsecond pair: \"{3}\"".
                            format(scramble, cross_solution, first_pair_solution, second_pair_solution))

    def test_04_third_pair(self):
        for i in range(1000):
            cube = Cube()
            scramble = scramble_generator(20)
            cube.scramble(scramble)
            cross_solution, cross_cube = cross(cube)
            first_pair_solution, fstp_cube = first_pair(cross_cube)
            second_pair_solution, sndp_cube = second_pair(fstp_cube)
            third_pair_solution, trdp_cube = third_pair(sndp_cube)
            self.assertTrue(assert_third_pair(trdp_cube), msg="error on scramble: \"{0}\"\ncross: \"{1}\"\nfirst pair: "
                                                              "\"{2}\"\nsecond pair: \"{3}\"\nthird pair: \"{4}\"".
                            format(scramble, cross_solution, first_pair_solution, second_pair_solution,
                                   third_pair_solution))

    def test_05_fourth_pair(self):
        for i in range(1000):
            cube = Cube()
            scramble = scramble_generator(20)
            cube.scramble(scramble)
            cross_solution, cross_cube = cross(cube)
            first_pair_solution, fstp_cube = first_pair(cross_cube)
            second_pair_solution, sndp_cube = second_pair(fstp_cube)
            third_pair_solution, trdp_cube = third_pair(sndp_cube)
            fourth_pair_solution, frtp_cube = fourth_pair(trdp_cube)
            self.assertTrue(assert_fourth_pair(frtp_cube),
                            msg="error on scramble: \"{0}\"\ncross: \"{1}\"\nfirst pair: "
                                "\"{2}\"\nsecond pair: \"{3}\"\nthird pair: \"{4}\"\nfourth pair: \"{5}\"".
                            format(scramble, cross_solution, first_pair_solution, second_pair_solution,
                                   third_pair_solution, fourth_pair_solution))

    def test_06_first_look_oll(self):
        for i in range(1000):
            cube = Cube()
            scramble = scramble_generator(20)
            cube.scramble(scramble)
            cross_solution, cross_cube = cross(cube)
            f2l_solution, f2l_cube = f2l(cross_cube)
            fl_oll_solution, fl_oll_cube = first_look_oll(f2l_cube)
            self.assertTrue(assert_first_look_oll(fl_oll_cube),
                            msg="error on scramble: \"{0}\"\ncross: \"{1}\"\nf2l: \"{2}\"\nfirst look oll: \"{3}\"".
                            format(scramble, cross_solution, f2l_solution, fl_oll_solution))

    def test_07_oll(self):
        for i in range(1000):
            cube = Cube()
            scramble = scramble_generator(20)
            cube.scramble(scramble)
            cross_solution, cross_cube = cross(cube)
            f2l_solution, f2l_cube = f2l(cross_cube)
            oll_solution, oll_cube = oll(f2l_cube)
            self.assertTrue(assert_oll(oll_cube),
                            msg="error on scramble: \"{0}\"\ncross: \"{1}\"\nf2l: \"{2}\"\nfirst look oll: \"{3}\"".
                            format(scramble, cross_solution, f2l_solution, oll_solution))


if __name__ == '__main__':
    unittest.main()
