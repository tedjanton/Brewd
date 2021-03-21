from app.models import db, Shop


def seed_shops():
    shop1 = Shop(name="Oromo Cafe",
                 description="This is a veritable United Nations for coffee, as Oromo Cafe takes flavors from Africa, India and Turkey to offer some of Chicago's most-unique coffee drinks. Oromo also spikes its beverages with superfoods for added nutrients in the drinks.",
                 address_1="4703 N Lincoln Ave",
                 address_2="",
                 city="Chicago",
                 state="Illinois",
                 zip_code=60625,
                 logo_src="https://brewd.s3.amazonaws.com/shop-logos/oromo_cafe_logo.jpeg")

    shop2 = Shop(name="Metric Coffee Co.",
                 description="Dreamed into existence by Caffe Streets owner Darko Arandjelovic and former Intelligentsia roasting manager Xavier Alexander, Metric Coffee is undeniably cool. The modern, public-facing shop and back-room roasting facility are housed on a lesser-trafficked stretch of Fulton Street, making it the perfect destination for a lazy Saturday morning. Grab a cup or sign up for a tour, where you'll get an inside look at the Chicago-born business's fascinating operation.",
                 address_1="2021 W Fulton St",
                 address_2="",
                 city="Chicago",
                 state="Illinois",
                 zip_code=60612,
                 logo_src="https://brewd.s3.amazonaws.com/shop-logos/metric-coffee.png")

    shop3 = Shop(name="Four Letter Word Coffee",
                 description="Don't expect to find pumpkin-spice anything at this tiny but specialized coffee shop in Logan Square. Branching off from its roastery in Back of the Yards (and another in Istanbul), Four Letter Word Coffee offers drip, pour-over, espresso, Turkish-style, cold coffee and tea. Pair your cup o' Joe with a pastry from Cellar Door Provisions and have a seat in the exquisitely decorated space.",
                 address_1="3022 W Diversey Ave",
                 address_2="",
                 city="Chicago",
                 state="Illinois",
                 zip_code=60647,
                 logo_src="https://brewd.s3.amazonaws.com/shop-logos/four-letter-word.png")

    shop4 = Shop(name="Sip & Savor",
                 description="Boasting three locations on the South Side of Chicago, Sip & Savor is a coffee empire in the making. Founder Trez Pugh, III has long been committed to empowering his community by creating new jobs and offering space for people to come together. He does just that with Sip & Savor, which centers around fair-trade beans to boot. Get your coffee straight or spring for something a bit more indulgent, like the Bull Frog Mocha, with chocolate sauce, peppermint syrup, espresso and whipped cream.",
                 address_1="5301 S Hyde Park Blvd",
                 address_2="",
                 city="Chicago",
                 state="Illinois",
                 zip_code=60615,
                 logo_src="https://brewd.s3.amazonaws.com/shop-logos/sip-savor.png")

    shop5 = Shop(name="The Wormhole",
                 description="To get Wicker Park excited about another coffee shop, you’d have to do something pretty crazy. Like, say, install a DeLorean in the front of the store. Okay, Wormhole, you win. So now that this time-travel–themed coffee shop has the neighborhood’s attention, what else is going on here? Some very serious baristas, who use beans from a variety of cult roasters and who cold-brew the strongest iced coffee that’s ever graced our parched, caffeine-starved lips.",
                 address_1="1462 N Milwaukee Ave",
                 address_2="",
                 city="Chicago",
                 state="Illinois",
                 zip_code=60622,
                 logo_src="https://brewd.s3.amazonaws.com/shop-logos/the-wormhole.jpeg")

    shop6 = Shop(name="Caffé Streets",
                 description="Proving that not every coffee shop must take its inspiration from Seattle in the ’90s, Caffé Streets has the look of a European coffee bar and the coffee expertise to match. The staff is comfortable talking beans (the selection of which changes weekly) and brewing styles, such as pour-over, Chemex and siphon. Housemade pastries are also available, including scones and croissants.",
                 address_1="1750 W Division St",
                 address_2="",
                 city="Chicago",
                 state="Illinois",
                 zip_code=60622,
                 logo_src="https://brewd.s3.amazonaws.com/shop-logos/caffee-streets.jpeg")

    db.session.add(shop1)
    db.session.add(shop2)
    db.session.add(shop3)
    db.session.add(shop4)
    db.session.add(shop5)
    db.session.add(shop6)
    db.session.commit()


def undo_shops():
    db.session.execute('TRUNCATE shops;')
    db.session.commit()
