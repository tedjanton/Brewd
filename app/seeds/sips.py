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

 # SIPS lauren
    sip13 = Sip(user_id=3,
                coffee_id=30,
                review="Definitely packs a punch! Super smooth and left me feeling energized all day.",
                rating=5,
                img_src="",
                created_at=(datetime(2021, 1, 13)))

    sip14 = Sip(user_id=5,
                coffee_id=25,
                review="Great iced coffee! I wish they had more alterntive milk options, but overall I would come back.",
                rating=None,
                img_src="",
                created_at=(datetime(2020, 2, 18)))

    sip15 = Sip(user_id=2,
                coffee_id=19,
                review="Pretty good! Very strong vanilla flavor, though.",
                rating=None,
                img_src="",
                created_at=(datetime(2020, 4, 15)))

    sip16 = Sip(user_id=6,
                coffee_id=26,
                review="",
                rating=5,
                img_src="Perfect americano. Merit has the best espresso in Austin and the baristas are so friendly!",
                created_at=(datetime(2019, 11, 30)))

    sip17 = Sip(user_id=7,
                coffee_id=26,
                review="Fabulous espresso. Their espresso blend is delicious and it was very affordable as well.",
                rating=4,
                img_src="",
                created_at=(datetime(2021, 2, 12)))

    sip18 = Sip(user_id=12,
                coffee_id=31,
                review="Soo good!! Very smooth and delicious. I really enjoyed people watching while I drank my coffee.",
                rating=4,
                img_src="",
                created_at=(datetime(2021, 3, 20)))

    sip19 = Sip(user_id=15,
                coffee_id=30,
                review="Pretty good but way too much caffeine - I was feeling jittery all day. I wish the barista had warned me!",
                rating=3,
                img_src="",
                created_at=(datetime(2021, 2, 14)))

    sip20 = Sip(user_id=2,
                coffee_id=36,
                review="The Chai was a bit sweet for me - I prefer a more spiced Chai - but overall it was still good.",
                rating=3,
                img_src="",
                created_at=(datetime(2020, 12, 16)))


    sip21 = Sip(user_id=10,
                coffee_id=38,
                review="Mine arrived cold and the milkk tasted bitter - yuck! Also, the service was terrible and the barista was so rude.",
                rating=0,
                img_src="",
                created_at=(datetime(2020, 2, 26)))

    sip22 = Sip(user_id=10,
                coffee_id=37,
                review="Wow!! If you need a pick-me-up, definitely get this. You will absolutely be amped up.",
                rating=4,
                img_src="",
                created_at=(datetime(2020, 3, 6)))

    sip23 = Sip(user_id=7,
                coffee_id=22,
                review="My favorite coffee in Ausin! Its so delicious - it has tons of caffeine but you hardly notice because it is so sweet. I think of it as a dessert! The barista was fabulous as well!",
                rating=4,
                img_src="",
                created_at=(datetime(2021, 2, 16)))

    sip24 = Sip(user_id=14,
                coffee_id=29,
                review="Really yummy! It's pretty sweet, though, so keep that in mind.",
                rating=None,
                img_src="",
                created_at=(datetime(2021, 3, 1)))

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
    db.session.add(sip13)
    db.session.add(sip14)
    db.session.add(sip15)
    db.session.add(sip16)
    db.session.add(sip17)
    db.session.add(sip18)
    db.session.add(sip19)
    db.session.add(sip20)
    db.session.add(sip21)
    db.session.add(sip22)
    db.session.add(sip23)
    db.session.add(sip24)
    db.session.commit()


def undo_sips():
    db.session.execute('TRUNCATE sips;')
    db.session.commit()
