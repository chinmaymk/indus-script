import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from analyze_h95_profile import profile_volume


class ProfileVolumeTests(unittest.TestCase):
    def test_cylinder_and_cone_exact(self):
        self.assertAlmostEqual(profile_volume([(0,10),(20,10)],1),2*math.pi)
        self.assertAlmostEqual(profile_volume([(0,10),(20,0)],1),2*math.pi/3)

    def test_split_frustum_preserves_volume(self):
        self.assertAlmostEqual(profile_volume([(0,3),(10,9)],2),
                               profile_volume([(0,3),(4,5.4),(10,9)],2))

    def test_scale_cube_and_fill_monotonicity(self):
        points=[(0,10),(20,10)]
        v=profile_volume(points,1)
        self.assertAlmostEqual(profile_volume(points,2),8*v)
        self.assertAlmostEqual(profile_volume(points,1,cutoff_y=10),v/2)
        self.assertEqual(profile_volume(points,1,cutoff_y=30),0)
        self.assertLess(profile_volume(points,1,radial_shift=-1),v)

    def test_invalid_profile(self):
        for p in [[(0,1)],[(2,1),(1,1)],[(0,-1),(1,1)]]:
            with self.assertRaises(ValueError): profile_volume(p,1)


if __name__=='__main__': unittest.main()
