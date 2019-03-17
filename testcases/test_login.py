import pytest
from pages.loginpage import LoginPageObject

@pytest.mark.parametrize('username, password',[
    ('EmailReady','passwordReady')
])
def test_douban(username, password):
    _login_in = LoginPageObject()
    _login_in.login(username, password)
    assert _login_in.get_my_douban_text() =='我的豆瓣'



