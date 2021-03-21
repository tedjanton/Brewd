from app.models import db, Sip
from datetime import datetime


def seed_sips():
    sip1 = Sip(user_id=1,
               coffee_id=1,
               review="Super tasty! Would highly recommend to anyone.",
               rating=5,
               img_src="",
               created_at=(datetime(2020, 8, 24)))

    sip2 = Sip(user_id=1,
               coffee_id=4,
               review="This had a really nice flavor. It was a bit too sweet for me though.",
               rating=4,
               img_src="",
               created_at=(datetime(2020, 12, 3)))

    sip3 = Sip(user_id=1,
               coffee_id=7,
               review="One of my favorite coffees!",
               rating=5,
               img_src="",
               created_at=(datetime(2021, 3, 3)))

    sip4 = Sip(user_id=1,
               coffee_id=10,
               review="Felt like giving this one a try - I might get it again with a bit more sugar.",
               rating=4,
               img_src="",
               created_at=(datetime(2021, 2, 22)))

    sip5 = Sip(user_id=1,
               coffee_id=13,
               review="This is perfect for any occasion.",
               rating=5,
               img_src="",
               created_at=(datetime(2021, 1, 5)))

    sip6 = Sip(user_id=1,
               coffee_id=16,
               review="",
               rating=5,
               img_src="",
               created_at=(datetime(2021, 3, 3)))

    sip7 = Sip(user_id=2,
               coffee_id=2,
               review="This one was great. I'll be getting it again!",
               rating=5,
               img_src="",
               created_at=(datetime(2020, 2, 3)))

    sip7 = Sip(user_id=2,
               coffee_id=5,
               review="Super yummy.",
               rating=5,
               img_src="",
               created_at=(datetime(2020, 10, 12)))

    sip8 = Sip(user_id=2,
               coffee_id=8,
               review="Not so great.",
               rating=2,
               img_src="",
               created_at=(datetime(2020, 7, 12)))

    sip9 = Sip(user_id=2,
               coffee_id=11,
               review="Amazing drink. I would highly recommend this to anyone.",
               rating=5,
               img_src="",
               created_at=(datetime(2021, 2, 2)))

    sip10 = Sip(user_id=2,
                coffee_id=14,
                review="",
                rating=None,
                img_src="",
                created_at=(datetime(2021, 1, 2)))

    sip11 = Sip(user_id=2,
                coffee_id=17,
                review="This one got me gittery.",
                rating=3,
                img_src="",
                created_at=(datetime(2021, 1, 18)))

    sip12 = Sip(user_id=2,
                coffee_id=18,
                review="Ok.",
                rating=None,
                img_src="",
                created_at=(datetime(2021, 2, 26)))

    db.session.add(sip1)
    db.session.add(sip2)
    db.session.add(sip3)
    db.session.add(sip4)
    db.session.add(sip5)
    db.session.add(sip6)
    db.session.add(sip7)
    db.session.add(sip8)
    db.session.add(sip9)
    db.session.add(sip10)
    db.session.add(sip11)
    db.session.add(sip12)
    db.session.commit()


def undo_sips():
    db.session.execute('TRUNCATE sips;')
    db.session.commit()
