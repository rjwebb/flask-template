import pdb
import unittest

from first_app import app, db
from first_app.models import Thing

# Uses code from: kronosapiens.github.io/blog/2014/07/29/setting-up-unit-tests-with-flask.html

class TestThing(unittest.TestCase):
    def setUp(self):
        app.config.from_object('first_app.config.TestingConfig')
        db.session.close()
        db.drop_all()
        db.create_all()

    def test_lookup(self):
        thing = Thing('test')
        db.session.add(thing)
        db.session.commit()

        things = Thing.query.all()
        assert thing in things
        print "NUMBER OF THINGS:", len(things)

if __name__ == '__main__':
    unittest.main()
