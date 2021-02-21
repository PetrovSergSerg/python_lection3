import pytest
from fixture.application import Application
from data.user import User


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(User.ADMIN)

    def finalizer():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(finalizer)
    return fixture
