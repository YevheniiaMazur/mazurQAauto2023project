import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")

    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")

    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")

    assert r["total_count"] == 43
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")

    assert r["total_count"] != 0


@pytest.mark.api_opt
def test_last_commit_author(github_api):
    r = github_api.get_commits("YevheniiaMazur", "mazurQAauto2023project")
    author = r[0]["commit"]["author"]["name"]

    assert author == "YevheniiaMazur"


@pytest.mark.api_opt
def test_commits_repo_not_exist(github_api):
    r = github_api.get_commits("YevheniiaMazur", "auto2023project")

    assert r["message"] == "Not Found"
    assert (
        r["documentation_url"]
        == "https://docs.github.com/rest/commits/commits#list-commits"
    )


@pytest.mark.api_opt
def test_code_of_conduct_exists(github_api):
    r = github_api.get_code_of_conduct("contributor_covenant")

    assert r["name"] == "Contributor Covenant"


@pytest.mark.api_opt
def test_code_of_conduct_not_exist(github_api):
    key = "not_exist_code"
    r = github_api.get_code_of_conduct(key)
    status = github_api.get_code_of_conduct_status(key)

    assert status == 404
    assert r["message"] == "Not Found"
