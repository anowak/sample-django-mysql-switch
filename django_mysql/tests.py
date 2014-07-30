from django.test import TestCase
from django_mysql.storage import Storage
from subprocess import call

class ScoreTestCase(TestCase):
  def setUp(self):
    call("mysql -e 'create database dog;'", shell=True) # just a test
    call("mysqldump prod | mysql test", shell=True)

  def test_storage_finds_score(self):
    storage = Storage()
    score = storage.get_score()
    self.assertEqual(score, 1234)
