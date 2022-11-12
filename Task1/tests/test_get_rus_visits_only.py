from Task1.main import get_rus_visits_only, get_only_unique_ids, get_queries_amount


def test_get_rus_visits_only():
    assert type(get_rus_visits_only()) is list
    for visit in get_rus_visits_only():
        assert 'Россия' in visit


def test_get_only_unique_ids():
    assert type(get_only_unique_ids()) is list
    checking_list = []
    for user_id in get_only_unique_ids():
        if user_id not in checking_list:
            checking_list += [user_id]
    assert checking_list == get_only_unique_ids()


def test_get_queries_amount():
    assert type(get_queries_amount()) is str

