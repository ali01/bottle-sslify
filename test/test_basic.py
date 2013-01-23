import subprocess
import unittest

import bottle
import bottletest

from bottle_sslify import SSLify


class TestSSLify(bottletest.ServerTestBase):

  def setUp(self):
    super(TestSSLify, self).setUp()

    @self.app.route('/')
    def index():
      return 'hello world'

    SSLify(self.app)


  def test_redirect(self):
    self.assertStatus(302)


if __name__ == '__main__':
  unittest.main()
