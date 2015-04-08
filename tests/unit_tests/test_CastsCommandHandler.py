from src.MessageHandler import new_get_cats_response


def new_url_content_fetcher(file_name):
    return lambda url: open('tests/data/' + file_name, 'r').read()


def test_get_5_latest_casts():
    get_cats_response = new_get_cats_response(new_url_content_fetcher('youtube-casts-five.json'))

    assert get_cats_response('!casts') == [
        "5 Latest youtube videos:",
        "Supreme Commander Forged Alliance Forever: Anaryl & Steinklotz by KBodLdIi00ezUQbTYuZnVQ - http://www.youtube.com/watch?v=kf89NSzZJwI - 2015-04-04 (0 likes)",
        "Let's (Re)play Supreme Commander Forged Alliance #20 - Purer Stress by kuenssi - http://www.youtube.com/watch?v=FHOPgEtCQuQ - 2015-04-04 (0 likes)",
        "Supreme Commander Forged Alliance Early Access Free Download by Sw2oXWDu4PaSLbFrSWhF4w - http://www.youtube.com/watch?v=5NXd8JMXWc0 - 2015-04-04 (0 likes)",
        "Countdown to Insanity! - Supreme Commander Forged Alliance by brnkoinsanity - http://www.youtube.com/watch?v=okrX1FI1iGM - 2015-04-04 (20 likes)",
        "Gyle's Patreon campaign is now live... by felixlighta - http://www.youtube.com/watch?v=SN8ujL1iMWU - 2015-04-03 (230 likes)"
    ]


def test_when_getting_videos_from_blacklisted_users_they_get_omitted():
    get_cats_response = new_get_cats_response(
        new_url_content_fetcher('youtube-casts-ten.json'),
        blacklisted_youtubers=['kuenssi', 'brnkoinsanity']
    )

    assert get_cats_response('!casts') == [
        "5 Latest youtube videos:",
        "Supreme Commander Forged Alliance Forever: Anaryl & Steinklotz by KBodLdIi00ezUQbTYuZnVQ - http://www.youtube.com/watch?v=kf89NSzZJwI - 2015-04-04 (0 likes)",
        "Supreme Commander Forged Alliance Early Access Free Download by Sw2oXWDu4PaSLbFrSWhF4w - http://www.youtube.com/watch?v=5NXd8JMXWc0 - 2015-04-04 (0 likes)",
        "Gyle's Patreon campaign is now live... by felixlighta - http://www.youtube.com/watch?v=SN8ujL1iMWU - 2015-04-03 (230 likes)",
        "Forged Alliance Forever - Balvery Mountains 1v1 HD by tOqRXhQ9Alej12qfAlXL2A - http://www.youtube.com/watch?v=wQh2yU-1gMo - 2015-04-03 (1 likes)",
        "Forged Alliance vs. Heroic Blast Furnace (Not a kill) by hp2fa - http://www.youtube.com/watch?v=g7zMtpMXMOM - 2015-04-03 (0 likes)"
    ]


def test_get_2_latest_casts():
    get_cats_response = new_get_cats_response(
        new_url_content_fetcher('youtube-casts-five.json'),
        cast_count=2
    )

    assert get_cats_response('!casts') == [
        "2 Latest youtube videos:",
        "Supreme Commander Forged Alliance Forever: Anaryl & Steinklotz by KBodLdIi00ezUQbTYuZnVQ - http://www.youtube.com/watch?v=kf89NSzZJwI - 2015-04-04 (0 likes)",
        "Let's (Re)play Supreme Commander Forged Alliance #20 - Purer Stress by kuenssi - http://www.youtube.com/watch?v=FHOPgEtCQuQ - 2015-04-04 (0 likes)"
    ]
