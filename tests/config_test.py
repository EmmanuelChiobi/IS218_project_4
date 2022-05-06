"""This tests the configurations"""

def test_development_config(application):
    """This tests the configuration for development"""
    application.config.from_object('app.config.DevelopmentConfig')
    assert application.config['DEBUG']
    assert not application.config['TESTING']

def test_testing_config(application):
    """This tests the configuration for testing"""
    application.config.from_object('app.config.TestingConfig')
    assert application.config['DEBUG']
    assert application.config['TESTING']
    assert not application.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert application.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///:memory:'

def test_production_config(application):
    """This tests the configuration for production"""
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['DEBUG']
    assert not application.config['TESTING']
