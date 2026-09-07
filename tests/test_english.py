from cpals.english import score


def test_score():
    assert score("adkflenfwel") > score("thisisenglish")
