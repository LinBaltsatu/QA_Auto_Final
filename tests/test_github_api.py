import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('some_user_non_exist')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 32


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('repononexist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_user_doesnt_follow_target_user(github_api):
    code = github_api.user_follows_target_user ('LinBaltsatu', 'defunkt')
    assert code == 404 
