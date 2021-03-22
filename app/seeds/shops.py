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

# SHOPS lauren
    shop7 = Shop(name="Alfred",
                 description="Keeping. Austin. Weirder. Enjoy picturesque views of Town Lake with your World Fmamous Iced Vanilla Latte while sitting at The LINE Hotel's infinity pool.",
                 address_1="111 E Cesar Chavez St",
                 address_2="",
                 city="Austin",
                 state="Texas",
                 zip_code=78701,
                 logo_src="https://pbs.twimg.com/profile_images/1138864169409585152/d3uciIYM_400x400.jpg")

    shop8 = Shop(name="Merit Coffee",
                 description="Like you, we care about the taste and quality of the coffee we serve and the hospitality you experience at Merit Coffee. We’ve trained with some of the best coffee people in the world, some of us earning certification as professional coffee stewards and all of us acquiring the skills to make your cup of coffee the best in Texas.",
                 address_1="1105 S Lamar Blvd",
                 address_2="",
                 city="Austin",
                 state="Texas",
                 zip_code=78704,
                 logo_src="http://static1.squarespace.com/static/56a027871f4039e3596c17aa/5aff965c70a6ada6e2100d91/5ccb6135ea82dc000154c41d/1576520601676/0.jpg?format=1500w")

    shop9 = Shop(name="Houndstooth Coffee",
                 description="Contemporary cafe serving select coffees, teas, wines, craft beer & pastries in a chill setting.",
                 address_1="401 Congress Ave",
                 address_2="100C",
                 city="Austin",
                 state="Texas",
                 zip_code=78701,
                 logo_src="https://uploads.poachedjobs.com/wp-content/uploads/2017/10/11135305/Chandler-Ad-768x768.jpg")

    shop10 = Shop(name="Halcyon",
                  description="Coffeehouse by day, bar & lounge by night where you can always relax and find your own personal 'halcyon'.",
                  address_1="218 W 4th St",
                  address_2="",
                  city="Austin",
                  state="Texas",
                  zip_code=78701,
                  logo_src="https://halcyonathome.square.site/uploads/b/71a53da0-7067-11ea-b314-e1400c853f79/Copy%20of%20HAL_rgb_tag.jpg")

    shop11 = Shop(name="Jo's Coffee",
                  description="Stumptown coffee, baked goods & more from a colorful kiosk with outdoor seating & iconic graffiti.",
                  address_1="1300 S Congress Ave",
                  address_2="",
                  city="Austin",
                  state="Texas",
                  zip_code=78704,
                  logo_src="https://static1.squarespace.com/static/55679273e4b0f3550bf4a8fe/t/5bc8b75d8165f54f6a6dc2f0/1612461235598/")

    shop12 = Shop(name="The Buzz Mill",
                  description="Rustic spot serves coffee, beer & cider around the clock in general-store digs with a back patio.",
                  address_1="1505 Town Creek Dr",
                  address_2="",
                  city="Austin",
                  state="Texas",
                  zip_code=78741,
                  logo_src="https://pbs.twimg.com/profile_images/534750859502964736/l8Su6pqm.jpeg")

    shop13 = Shop(name="Brewed Awakenings Cafe",
                  description="From carefully hand-crafted coffee to baked goods & soups made from scratch as well as sandwiches, paninis and salads, we proudly serve Saline area customers with the freshest local ingredients.",
                  address_1="7025 E Michigan Avenue",
                  address_2="",
                  city="Saline",
                  state="Michigan",
                  zip_code=48176,
                  logo_src="")

    shop14 = Shop(name="Backyard Beans Coffee Company",
                  description="Backyard Beans Coffee Company is a craft coffee roaster specializing in high quality coffee beans and cold brew.",
                  address_1="408 W Main Street",
                  address_2="",
                  city="Landsdale",
                  state="Pennsylvania",
                  zip_code=19446,
                  logo_src="")

    shop15 = Shop(name="Zingerman's Coffee Company",
                  description="Zingerman’s Coffee Company is a wholesale roaster supplying cafés, restaurants and businesses with great coffees. We also serve our single estate, small batch coffees at our coffee bar in Ann Arbor.",
                  address_1="3723 Plaza Drive",
                  address_2="",
                  city="Ann Arbor",
                  state="Michigan",
                  zip_code=48108,
                  logo_src="https://www.zingermanscoffee.com/app/themes/zingermanscoffee17/images/logo_green.svg")

    shop16 = Shop(name="RoosRoast Liberty",
                  description="Chill, comfy hangout featuring coffee, cold brew & espresso, plus breakfast bites & pastries.",
                  address_1="117 E Liberty Street",
                  address_2="",
                  city="Ann Arbor",
                  state="Michigan",
                  zip_code=48104,
                  logo_src="https://cdn.shopify.com/s/files/1/1461/7372/files/Round_logo_blue_coffee-01_500x.png?v=1603375215")

    shop17 = Shop(name="Elixr Coffee Roasters",
                  description="Elixr has become a mecca for desperate coffee lovers. Elixr has developed a reputation for serving real deal coffee in a modern, yet relaxed atmosphere.",
                  address_1="315 N 12th Street",
                  address_2="",
                  city="Philadelphia",
                  state="Pennsylvania",
                  zip_code=19107,
                  logo_src="https://cdn.shopify.com/s/files/1/2565/6836/files/elixrcoffeeroastersblue_x150@2x.png?v=1511318250")

    shop18 = Shop(name="ReAnimator Coffee",
                  description="Local micro coffee roasters share brews & expertise in a snug, chic hangout with hardwood floors.",
                  address_1="1523 E Susquehanna Ave",
                  address_2="",
                  city="Philadelphia",
                  state="Pennsylvania",
                  zip_code=19125,
                  logo_src="https://pbs.twimg.com/profile_images/833752955862052868/f59GA6nj_400x400.jpg")

    

    db.session.add(shop1)
    db.session.add(shop2)
    db.session.add(shop3)
    db.session.add(shop4)
    db.session.add(shop5)
    db.session.add(shop6)
    db.session.add(shop7)
    db.session.add(shop8)
    db.session.add(shop9)
    db.session.add(shop10)
    db.session.add(shop11)
    db.session.add(shop12)
    db.session.add(shop13)
    db.session.add(shop14)
    db.session.add(shop15)
    db.session.add(shop16)
    db.session.add(shop17)
    db.session.add(shop18)

    db.session.commit()


def undo_shops():
    db.session.execute('TRUNCATE shops;')
    db.session.commit()
