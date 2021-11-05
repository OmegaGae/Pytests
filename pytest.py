# python3.10.0
# -*-coding:Latin-1 -*

import random
import unittest


class RandomTest(unittest.TestCase):
    """Test le fonctionnement de certaines fonctions du module 'random'."""
    
    def testChoice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        self.assertIn(elt, liste)

    def testChoiceEchec(self):
        """Test le fonctionnement de la fonction 'random.choice' \
            en cas d'echec."""
        liste = list(range(10))
        elt = random.choice(liste)
        # vérifie si elt est contenue ds la liste
        self.assertIn(elt, ("a", "b", "c"))  

    # Autres méthodes de test
    def testShuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'"""
        liste = list(range(10))
        random.shuffle(liste)  # mélange les élements de la liste
        liste.sort()
        # on regarde liste == list(range(10))
        self.assertEqual(liste, list(range(10)))

    def testSample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        liste = list(range(10))
        # .sample: retourne une liste de n element selectionnée
        # aléatoiremt ds une lsite
        extrait = random.sample(liste, 5)
        for element in extrait:
            self.assertIn(element, liste)

    def testSampleExcedanSilently(self):
        """Test le fonctionnement de la fonction 'random.sample'.\
            cas si n element > n element lsite d'origine (excedant)"""
        liste = list(range(10))
        # .sample: retourne une liste de n element selectionnée
        # aléatoiremt ds une lsite
        extrait = random.sample(liste, 11)
        for element in extrait:
            self.assertIn(element, liste)

    def testSampleExcedantNoSilently(self):
        """Test le fonctionnement de la fonction 'random.sample'.\
            cas si n element > n element lsite d'origine (excedant)"""

        liste = list(range(10))
        # .sample: retourne une liste de n element selectionnée
        # aléatoiremt ds une lsite

        extrait = random.sample(liste, 6)
        for element in extrait:
            self.assertIn(element, liste)
        # utilisation d'un context manager 'with' sinon
        # self.assertRaises (ValueError, random.sample, liste, 11)
        # pour tester la levé de Value ERror lorsque n element > n element
        # liste d'origine
        with self.assertRaises(ValueError):
            random.sample(liste, 20)


unittest.main()
