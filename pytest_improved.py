#python3.10.0
#-*-coding:Latin-1 -*

import random
import unittest


class RandomTest(unittest.TestCase):
    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10))

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        self.assertIn(elt, self.liste)

    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)
        #on vérifie le comportement de sample en cas d'erreur 
        #on a donc reproduit le comportement normal en cas d'erreur 
        # de cette méthode
        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)

