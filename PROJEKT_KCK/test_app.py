import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class MyTest(TestCase):

    def create_app(self):
        # Konfigurowanie aplikacji do testów
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_home_page(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('index.html')
        self.assertIn(b'Witamy w aplikacji webowej do nauki gry na gitarze!', response.data)

    def test_lessons_page(self):
        response = self.client.get('/lessons')
        self.assert200(response)
        self.assert_template_used('lessons.html')
        self.assertIn(b'Lekcje', response.data)

    def test_metronome_page(self):
        response = self.client.get('/metronome')
        self.assert200(response)
        self.assert_template_used('metronome.html')
        self.assertIn(b'Metronom', response.data)

    def test_chords_scales_page(self):
        response = self.client.get('/library')
        self.assert200(response)
        self.assert_template_used('library.html')
        self.assertIn(b'Biblioteka akordow i skal', response.data)

    def test_chords_page(self):
        response = self.client.get('/chords')
        self.assert200(response)
        self.assert_template_used('chords.html')
        self.assertIn(b'Akordy', response.data)

    def test_scales_page(self):
        response = self.client.get('/scales')
        self.assert200(response)
        self.assert_template_used('scales.html')
        self.assertIn(b'Skale muzyczne', response.data)

if __name__ == '__main__':
    unittest.main()
