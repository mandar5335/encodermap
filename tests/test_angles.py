import encodermap as em
import MDAnalysis as md
import numpy as np
from math import pi
import tensorflow as tf
import os
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'


class TestAngles(tf.test.TestCase):
    def test_ala10_angles(self):
        uni = md.Universe("Ala10_helix.pdb")
        selected_atoms = uni.select_atoms("backbone or name O1 or name H or name CB")
        moldata = em.MolData(selected_atoms)
        self.assertAllClose(moldata.angles,
                            [[1.9216446, 2.0355537, 2.128159,  1.9212531, 2.0357149, 2.1278918, 1.9220486,
                              2.0346954, 2.1269655, 1.9218233, 2.0352163, 2.1275373, 1.9212493, 2.035614,
                              2.128058,  1.9211367, 2.0354483, 2.128482,  1.9212018, 2.034529,  2.1266387,
                              1.9220015, 2.034642,  2.1270595, 1.9208968, 2.0354831, 2.127831,  1.9212908]])

    def test_chain_in_plane(self):
        bond_lengths = tf.constant([[1, 0.5, 1, 0.5, 1, 0.5],
                                    [1, 1, 1, 1, 1, 1]], tf.float32)
        angles = tf.constant([[pi/1.5, pi/8, pi/2, pi/8, pi/2],
                              [pi/4, pi/4, pi/4, pi/4, pi/4]], tf.float32)

        cartesians = em.chain_in_plane(bond_lengths, angles)
        with self.test_session() as sess:
            result = sess.run(cartesians)
        fig, axe = plt.subplots()
        axe.plot(result[0, :, 0], result[0, :, 1])
        axe.axis('equal')
        plt.show()
