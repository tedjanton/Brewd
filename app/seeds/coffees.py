from app.models import db, Coffee


def seed_coffees():
    coffee1 = Coffee(shop_id=1,
                     name="Golden Mylk Latte",
                     description="An ancient Indian Elixir. Almond Milk, Honey, Turmeric, Cinnamon, Ginger, Ashwagandha, Black Pepper, Espresso (Double Shot)",
                     caffeine=203,
                     type="hot",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/01-golden-mylk-latte.jpeg")

    coffee2 = Coffee(shop_id=1,
                     name="Cold Brew + Hazelnut Truffle",
                     description="Cold Brew Coffee, Cacao, Frozen Bananas, House made Toasted Hazelnut Milk, Coconut Caramel, Vanilla, Sea Salt, Maple Syrup.",
                     caffeine=231,
                     type="cold",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/02-cold-brew-hazelnult-truffle.jpeg")

    coffee3 = Coffee(shop_id=1,
                     name="Pistachio + Rose Latte",
                     description="Inspired by the Turkish Delight. Made with house made Pistachio Milk, Rose Syrup, Espresso (double shot)",
                     caffeine=167,
                     type="hot",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/03-pistachio-rose-latte.jpeg")

    # Metric
    coffee4 = Coffee(shop_id=2,
                     name="Cappuccino",
                     description="Simple, yet tasty and rich.",
                     caffeine=170,
                     type="hot",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/04-cappucino.jpeg")

    coffee5 = Coffee(shop_id=2,
                     name="Maple + Maca + Pecan",
                     description="House made Pecan Milk, Maple Syrup, Maca, Espresso (Double Shot)",
                     caffeine=210,
                     type="hot",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/05-maple-maca-pecan.jpeg")

    coffee6 = Coffee(shop_id=2,
                     name="Hazelnut Horchata Latte",
                     description="House made Toasted Hazelnut Milk, Rice Milk, Coconut Milk, Vanilla, Cinnamon, Maple Syrup, Espresso (Double Shot)",
                     caffeine=212,
                     type="hot",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/06-hazelnut-horchata-latte.jpeg")

    # Four Letter Word
    coffee7 = Coffee(shop_id=3,
                     name="Cinnamon Dolce Latte",
                     description="We add freshly steamed milk and cinnamon dolce-flavored syrup to our classic espresso, topped with sweetened whipped cream and a cinnamon dolce topping to bring you specialness in a treat.",
                     caffeine=95,
                     type="hot",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/07-cinnamon-dolce-latte.jpeg")

    coffee8 = Coffee(shop_id=3,
                     name="Caramel Macchiato",
                     description="Freshly steamed milk with vanilla-flavored syrup marked with espresso and topped with a caramel drizzle for an oh-so-sweet finish.",
                     caffeine=104,
                     type="hot",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/08-caramel-macchiato.jpeg")

    coffee9 = Coffee(shop_id=3,
                     name="Irish Cream Nitro Cold Brew",
                     description="This on-tap holiday drink awakens the merry: a velvety-smooth blend of Starbucks® Nitro Cold Brew with Irish cream syrup, topped with vanilla sweet cream cold foam and cocoa.",
                     caffeine=232,
                     type="cold",
                     img_src="https://brewd.s3.amazonaws.com/coffee-pics/09-irish-cream-nitro-cold-brew.jpeg")

    # Sip & Savor
    coffee10 = Coffee(shop_id=4,
                      name="Banana Mocha",
                      description="Chocolate sauce, banana syrup, 2 shots of espresso, steamed milk with whip cream.",
                      caffeine=62,
                      type="hot",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/10-banana-mocha.jpeg")

    coffee11 = Coffee(shop_id=4,
                      name="Caramel Nut Shake",
                      description="Caramel sauce, caramel, and hazelnut syrup, 2 scoops of ice cream, a dash of milk, a cup of ice, 2 shots of espresso all blended and topped with whip cream.",
                      caffeine=84,
                      type="cold",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/11-caramel-nut-shake.jpeg")

    coffee12 = Coffee(shop_id=4,
                      name="Tuxedo Mocha",
                      description="Dark and white chocolate sauce, coconut syrup, 2 shots of intense espresso and steamed milk with whip cream.",
                      caffeine=102,
                      type="hot",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/12-tuxedo-mocha.jpeg")

    # The Wormhole
    coffee13 = Coffee(shop_id=5,
                      name="Honey Bear Latte",
                      description="Created with locally sourced honey and two shots of espresso.",
                      caffeine=188,
                      type="hot",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/13-honey-bear-latte.jpeg")

    coffee14 = Coffee(shop_id=5,
                      name="Peanut Butter Koopa-Troopa",
                      description="Made with peanut mousse and local chocolate.",
                      caffeine=57,
                      type="cold",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/14-peanut-butter-koopa-troopa.jpeg")

    coffee15 = Coffee(shop_id=5,
                      name="Homemade Vanilla Bean",
                      description="The House Special. A simple vanilla latte dusted with vanilla bean seeds.",
                      caffeine=103,
                      type="hot",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/15-homemade-vanilla-bean.jpeg")

    # Caffé Streets
    coffee16 = Coffee(shop_id=6,
                      name="Macchiato",
                      description="An espresso with a dash of frothy steamed milk.",
                      caffeine=150,
                      type="hot",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/16-macchiato.jpeg")

    coffee17 = Coffee(shop_id=6,
                      name="Espresso",
                      description="Our smooth signature Espresso Roast with rich flavor and caramelly sweetness is at the very heart of everything we do.",
                      caffeine=130,
                      type="hot",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/17-espresso.jpeg")

    coffee18 = Coffee(shop_id=6,
                      name="Whipped Mocha Delight",
                      description="We blend mocha sauce and mocha chips with coffee, milk and ice, then top it off with whipped cream and a mocha drizzle to bring you endless java joy.",
                      caffeine=93,
                      type="cold",
                      img_src="https://brewd.s3.amazonaws.com/coffee-pics/18-whipped-mocha-delight.jpeg")

    db.session.add(coffee1)
    db.session.add(coffee2)
    db.session.add(coffee3)
    db.session.add(coffee4)
    db.session.add(coffee5)
    db.session.add(coffee6)
    db.session.add(coffee7)
    db.session.add(coffee8)
    db.session.add(coffee9)
    db.session.add(coffee10)
    db.session.add(coffee11)
    db.session.add(coffee12)
    db.session.add(coffee13)
    db.session.add(coffee14)
    db.session.add(coffee15)
    db.session.add(coffee16)
    db.session.add(coffee17)
    db.session.add(coffee18)
    db.session.commit()


def undo_coffees():
    db.session.execute('TRUNCATE coffees;')
    db.session.commit()
