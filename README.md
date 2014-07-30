Django+MySQL sample with mirroring production database
======================================================

This sample demonstrates how to copy data from production database to the test one prior to running the tests.

A separate `prod` database is created in `shippable.yml` file that contains one row for the only model that is
defined in this sample. The tests contain assertion to check if this data shows up in the test database.

Two approaches can be taken here:

1. Copy the data in the test suite `setUp` method. For example, if the production database is called `prod` and
test database is called `test`:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'prod',
                'USER': 'shippable',
                'TEST_NAME': 'test',
            },
        }

  We can perform the copy with the following command:

        from django.test import TestCase

        class ScoreTestCase(TestCase):
          def setUp(self):
            call("mysqldump prod | mysql test", shell=True)

2. Use `TEST_MIRROR` option to make Django perform the copy for us. This is a little bit hacky, but very
convenient. All that is required is the following database definition:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'prod',
                'USER': 'shippable',
                'TEST_NAME': 'test',
                'TEST_MIRROR': 'default'
            },
        }

This sample is built for Shippable, a docker based continuous integration and deployment platform.
