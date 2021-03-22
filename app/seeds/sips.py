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

    sip25 = Sip(user_id=8,
                coffee_id=41,
                review="great holiday treat!",
                rating=4,
                img_src="",
                created_at=(datetime(2020, 11, 22)))

    sip26 = Sip(user_id=8,
                coffee_id=43,
                review="",
                rating=5,
                img_src="",
                created_at=(datetime(2020, 7, 12)))

    sip27 = Sip(user_id=8,
                coffee_id=46,
                review="pretty good",
                rating=4,
                img_src="",
                created_at=(datetime(2020, 2, 2)))

    sip28 = Sip(user_id=8,
                coffee_id=47,
                review="weird name",
                rating=None,
                img_src="",
                created_at=(datetime(2020, 4, 7)))

    sip29 = Sip(user_id=8,
                coffee_id=48,
                review="yummy!!",
                rating=4,
                img_src="",
                created_at=(datetime(2020, 4, 16)))

    sip30 = Sip(user_id=8,
                coffee_id=49,
                review="super delish and not too sweet",
                rating=5,
                img_src="",
                created_at=(datetime(2020, 5, 8)))

    sip31 = Sip(user_id=8,
                coffee_id=50,
                review="my favorite!!",
                rating=5,
                img_src="",
                created_at=(datetime(2020, 8, 4)))

    sip32 = Sip(user_id=8,
                coffee_id=51,
                review="",
                rating=5,
                img_src="",
                created_at=(datetime(2020, 2, 10)))

    sip33 = Sip(user_id=8,
                coffee_id=52,
                review="keeps me awake",
                rating=5,
                img_src="",
                created_at=(datetime(2020, 12, 4)))

    sip34 = Sip(user_id=8,
                coffee_id=53,
                review="",
                rating=4,
                img_src="",
                created_at=(datetime(2020, 8, 11)))

    sip35 = Sip(user_id=8,
                coffee_id=54,
                review="ok",
                rating=3,
                img_src="",
                created_at=(datetime(2020, 7, 9)))

    sip36 = Sip(user_id=8,
                coffee_id=55,
                review="classic staple",
                rating=None,
                img_src="",
                created_at=(datetime(2020, 9, 5)))
    
    sip37 = Sip(user_id=19,
                coffee_id=75,
                review="I just love Peanut Butter, especially with chocolate and up until now, I'd never got to try that combination in a coffee drink.  This was my fist time and I absolutely loved it!!!",
                rating=5,
                img_src="",
                created_at=(datetime(2020, 5, 21)))

    sip38 = Sip(user_id=16,
                coffee_id=74,
                review="This had a decent flavor but the rasberry topping was a bit overpowering if I'm being honest.",
                rating=3,
                img_src="",
                created_at=(datetime(2020, 11, 9)))

    sip39 = Sip(user_id=14,
                coffee_id=73,
                review="If you like coconut, you'll love this macchiato!",
                rating=5,
                img_src="",
                created_at=(datetime(2021, 12, 23)))

    sip40 = Sip(user_id=11,
                coffee_id=72,
                review="I'm a regular here at Bennet's and this is my regular beverage.  I'd wager it's one of the best cold brews in town.",
                rating=5,
                img_src="",
                created_at=(datetime(2021, 7, 10)))

    sip41 = Sip(user_id=8,
                coffee_id=71,
                review="The perfect version of a water-downed American drip coffee.",
                rating=2,
                img_src="",
                created_at=(datetime(2021, 9, 1)))

    sip42 = Sip(user_id=5,
                coffee_id=70,
                review="I can't start my day until I've had my Biscoff Latte!",
                rating=5,
                img_src="",
                created_at=(datetime(2021, 3, 3)))

    sip43 = Sip(user_id=20,
                coffee_id=69,
                review="Pretty standard.",
                rating=4,
                img_src="",
                created_at=(datetime(2019, 3, 2)))

    sip44 = Sip(user_id=18,
                coffee_id=68,
                review="It's my first time trying espresso cut with milk... Verdict? I prefer the pure version without milk.",
                rating=3,
                img_src="",
                created_at=(datetime(2020, 5, 19)))

    sip45 = Sip(user_id=17,
                coffee_id=67,
                review="Man, there was so much caffeine in this bad boy, that I was spinning. I think I'll grab another on the way out!!",
                rating=5,
                img_src="",
                created_at=(datetime(2019, 6, 13)))

    sip46 = Sip(user_id=16,
                coffee_id=66,
                review="Lavender belongs in a garden or in candles, not in coffee!!!",
                rating=1,
                img_src="",
                created_at=(datetime(2021, 4, 27)))

    sip47 = Sip(user_id=14,
                coffee_id=65,
                review="I love coffee and I love condensed milk, so how on earth could putting these two together go wrong? Trick question! It couldn't go wrong! This drink is amazing",
                rating=5,
                img_src="",
                created_at=(datetime(2020, 4, 4)))

    sip48 = Sip(user_id=12,
                coffee_id=64,
                review="Personally, I didn't find anyting special about this flavor combination and I actually found they didn't compliment each other well.",
                rating=3,
                img_src="",
                created_at=(datetime(2021, 2, 18)))

    sip49 = Sip(user_id=7,
                coffee_id=63,
                review="I wasn't really impressed with this coffee beverage.",
                rating=2,
                img_src="",
                created_at=(datetime(2019, 9, 17)))

    sip50 = Sip(user_id=5,
                coffee_id=62,
                review="Dulce de leche is my childhood favorite and this was an amazing way to bring me back to those days while enjoying a pretty decent cup of coffee.",
                rating=5,
                img_src="",
                created_at=(datetime(2019, 5, 23)))

    sip51 = Sip(user_id=8,
                coffee_id=61,
                review="So flavorful and aromatic. By far better than any other drip coffee I've had in a long while.",
                rating=4,
                img_src="",
                created_at=(datetime(2019, 10, 18)))

    sip52 = Sip(user_id=16,
                coffee_id=60,
                review="A Bohemian coffee drink to fit my crazy Bohemian heritage!!! I got good and faced on these babies!",
                rating=4,
                img_src="",
                created_at=(datetime(2020, 3, 30)))

    sip53 = Sip(user_id=19,
                coffee_id=59,
                review="I don't know remember if these were good, but I know that I had enough that I had to take a cab home.",
                rating=3,
                img_src="",
                created_at=(datetime(2019, 10, 24)))

    sip54 = Sip(user_id=2,
                coffee_id=58,
                review="Never had alcohol and coffee together, but I loved this drink and now I'm wondering where this coffee cocktail was all my life!",
                rating=5,
                img_src="",
                created_at=(datetime(2019, 12, 21)))

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
    db.session.add(sip25)
    db.session.add(sip26)
    db.session.add(sip27)
    db.session.add(sip28)
    db.session.add(sip29)
    db.session.add(sip30)
    db.session.add(sip31)
    db.session.add(sip32)
    db.session.add(sip33)
    db.session.add(sip34)
    db.session.add(sip35)
    db.session.add(sip36)
    db.session.add(sip37)
    db.session.add(sip38)
    db.session.add(sip39)
    db.session.add(sip40)
    db.session.add(sip41)
    db.session.add(sip42)
    db.session.add(sip43)
    db.session.add(sip44)
    db.session.add(sip45)
    db.session.add(sip46)
    db.session.add(sip47)
    db.session.add(sip48)
    db.session.add(sip49)
    db.session.add(sip50)
    db.session.add(sip51)
    db.session.add(sip52)
    db.session.add(sip53)
    db.session.add(sip54)

    db.session.commit()


def undo_sips():
    db.session.execute('TRUNCATE sips;')
    db.session.commit()
