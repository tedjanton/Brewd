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
    # COFFEES lauren
# alfred
    coffee 19 = Coffee(name='Iced Vanilla Latte',
                       shopId='7',
                       description='Behold our “World Famous” Iced Vanilla Latte: a double shot of espresso over milk and a helping of housemade vanilla – made with real vanilla bean.',
                       caffeine='200',
                       type='Cold',
                       imgSrc='https://i.pinimg.com/originals/79/cd/a2/79cda2b03a10dc87c80266508033682c.jpg')

    coffee 20 = Coffee(name='Iced Matcha Latte',
                       shopId='7',
                       description='Alfred’s own shade-grown, single-origin, tea-master blended matcha with the milk of your choice. No simpler way to CRUSH the day.',
                       caffeine='100',
                       type='Cold',
                       imgSrc='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F13c18270-5519-4e9c-aa55-3cda9727fdf8%2Foriginal.jpg%3Fv%3D63778513865&quality=85&w=320&h=0&mode=auto&format=&v=4')

    coffee 21 = Coffee(name='Cagaccino',
                       shopId='7',
                       description='Chaga, the superhero of the mushroom world, stars here in our most popular special where it is blended with vanilla, cacao, cinnamon, monkfruit, and topped with espresso and milk.',
                       caffeine='80',
                       type='Hot',
                       imgSrc='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2Fb28bfc57-e7c7-4390-9bde-90ddd8b13d68%2Foriginal.jpg%3Fv%3D63778513030&quality=85&w=320&h=0&mode=auto&format=&v=4')

    # jo's
    coffee 22 = Coffee(name='Iced Turbo',
                       shopId='11',
                       description='Our signature sweet drink made with coffee, espresso, chocolate, hazelnut, and cream.',
                       caffeine='125',
                       type='Cold',
                       imgSrc='https://www.austin360.com/storyimage/TX/20170706/ENTERTAINMENT/307069804/AR/0/AR-307069804.jpg',
                       createdAt='',
                       updatedAt='')

    coffee 23 = Coffee(name='Cortado',
                       shopId='11',
                       description='Double shot of espresso topped with 4oz of steamed milk.',
                       caffeine='110',
                       type='Hot',
                       imgSrc='https://perfectdailygrind.com/wp-content/uploads/2020/03/Cortadito-1.png')

    # merit
    coffee 24 = Coffee(name='Dirty Chai Latte',
                       shopId='8',
                       description='Chai tea with steamed milk and a shot of espresso.',
                       caffeine='85',
                       type='Hot',
                       imgSrc='https://raster-static.postmates.com/?url=com.postmates.img.prod.s3.amazonaws.com%2F2b616f0c-c417-4b5b-aea5-40ffef86a116%2Forig.jpg&quality=85&w=500&h=0&mode=auto&format=webp&v=4',
                       createdAt='',
                       updatedAt='')

    coffee 25 = Coffee(name='Iced Coffee',
                       shopId='8',
                       description='Our signature Cold Brew coffee served over ice.',
                       caffeine='175',
                       type='Cold',
                       imgSrc='https://i5.walmartimages.com/asr/7e29785b-9858-4aae-be64-ba96bafe299d.485f44a394c1b2d4829872f1bfb2f3de.jpeg',
                       createdAt='',
                       updatedAt='')


    coffee 26 = Coffee(name='Caffe Americano',
                       shopId='8',
                       description='Espresso shots topped with hot water create a light layer of crema culminating in this wonderfully rich cup with depth and nuance. Pro Tip: For an additional boost, ask your barista to try this with an extra shot.',
                       caffeine='225',
                       type='Hot',
                       imgSrc='https://globalassets.starbucks.com/assets/f12bc8af498d45ed92c5d6f1dac64062.jpg?impolicy=1by1_wide_1242',
                       createdAt='',
                       updatedAt='')

    coffee 27 = Coffee(name='Cappuccino',
                       shopId='8',
                       description='Dark, rich espresso lies in wait under a smoothed and stretched layer of thick milk foam. An alchemy of barista artistry and craft.',
                       caffeine='150',
                       type='Hot',
                       imgSrc='https://globalassets.starbucks.com/assets/5c515339667943ce84dc56effdf5fc1b.jpg?impolicy=1by1_wide_1242',
                       createdAt='',
                       updatedAt='')

    # houndstooth
    coffee 28 = Coffee(name='Honey Almondmilk Flat White',
                       shopId='9',
                       description='This flat white intentionally pairs almondmilk and Blonde Espresso Roast with a hint of honey, making a perfect amount of creamy, nutty sweetness.',
                       caffeine='150',
                       type='Hot',
                       imgSrc='https://globalassets.starbucks.com/assets/77801559b72b469583f4d484adc1bfa7.jpg?impolicy=1by1_wide_1242',
                       createdAt='',
                       updatedAt='')

    coffee 29 = Coffee(name='Salted Caramel Cream Cold Brew',
                       shopId='9',
                       description="Here's a savory-meets-sweet refreshing beverage certain to delight: our signature, super-smooth cold brew, sweetened with a touch of caramel and topped with a salted, rich cold foam.",
                       caffeine='185',
                       type='Cold',
                       imgSrc='https://globalassets.starbucks.com/assets/6ffca0a4b4ec4af98d07c4e860baca45.jpg?impolicy=1by1_wide_1242',
                       createdAt='',
                       updatedAt='')

    coffee 30 = Coffee(name='Nitro Cold Brew',
                       shopId='9',
                       description="Our small-batch cold brew—slow-steeped for a super-smooth taste—gets even better. We're infusing it with nitrogen to create a sweet flavor without sugar and cascading, velvety crema. Perfection is served.",
                       caffeine='280',
                       type='Cold',
                       imgSrc='https://globalassets.starbucks.com/assets/85ae42ce9eb5423d83c4410f7b561882.jpg?impolicy=1by1_wide_1242',
                       createdAt='',
                       updatedAt='')

    coffee 31 = Coffee(name='Nitro Flat White',
                       shopId='9',
                       description='Our bold ristretto shots of espresso mingle with the perfect amount of cold, creamy nitrogen-infused whole milk. The end result: an irresistible velvety crema.',
                       caffeine='130',
                       type='Cold',
                       imgSrc='https://globalassets.starbucks.com/assets/44dfc376272044878f2c8ee32cc7ca7e.jpg',
                       createdAt='',
                       updatedAt='')

    coffee 32 = Coffee(name='Iced Cinnamon Dolce Latte',
                       shopId='9',
                       description='We add freshly steamed milk and cinnamon dolce-flavored syrup to our classic espresso and ice, topped with sweetened whipped cream and a cinnamon dolce topping to bring you specialness in a treat.',
                       caffeine='150',
                       type='Cold',
                       imgSrc='https://globalassets.starbucks.com/assets/2a7651bc593044ba9043e90ddc20e3f1.jpg?impolicy=1by1_wide_1242',
                       createdAt='',
                       updatedAt='')
    # halcyon
    coffee 33 = Coffee(name='Iced Caramel Macchiato',
                       shopId='10',
                       description='We combine our rich, full-bodied espresso with vanilla-flavored syrup, milk and ice, then top it off with a caramel drizzle for an oh-so-sweet finish.',
                       caffeine='150',
                       type='Cold',
                       imgSrc='https://globalassets.starbucks.com/assets/79bfec31ab7447f691b3c48f39cc7661.jpg?impolicy=1by1_wide_1242',
                       createdAt='',
                       updatedAt='')

    coffee 34 = Coffee(name='Blonde Roast',
                       shopId='10',
                       description="Lightly roasted coffee that's soft, mellow and flavorful. Easy-drinking on its own and delicious with milk, sugar or flavored with vanilla, caramel or hazelnut.",
                       caffeine='360',
                       type='Hot',
                       imgSrc='https://globalassets.starbucks.com/assets/abb4f97948c948c28ea2dcaf933c4f6b.jpg?impolicy=1by1_wide_1242',
                       createdAt='',
                       updatedAt='')

    coffee 35 = Coffee(name='Iced Mocha',
                       shopId='10',
                       description='Silky housemade dark chocolate (vegan, soy-free) mixed with a double shot of espresso, topped with ice and milk.',
                       caffeine='220',
                       type='Cold',
                       imgSrc='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F682f540e-5784-4838-a987-5162d9e7d96f%2Foriginal.jpg%3Fv%3D63771239607&quality=85&w=320&h=0&mode=auto&format=&v=4',
                       createdAt='',
                       updatedAt='')
    # alfred
    coffee 36 = Coffee(name='Iced Chai Latte',
                       shopId='7',
                       description='Our signature spicy-sweet black tea brewed with cinnamon, ginger, cardamom, and molasses. Iced and mixed with milk.',
                       caffeine='95',
                       type='Cold',
                       imgSrc='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F3fb11e45-451d-4d08-8b3a-46a1d73c25af%2Foriginal.jpg%3Fv%3D63778552251&quality=85&w=320&h=0&mode=auto&format=&v=4',
                       createdAt='',
                       updatedAt='')

    coffee 37 = Coffee(name='Red Eye',
                       shopId='7',
                       description='Drip coffee, spiked with an additional double-shot of espresso.',
                       caffeine='350',
                       type='Hot',
                       imgSrc='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F29b7ef39-fdd3-4fba-9ea3-8fda5c05d93c%2Foriginal.jpg%3Fv%3D63778512427&quality=85&w=320&h=0&mode=auto&format=&v=4',
                       createdAt='',
                       updatedAt='')

    coffee 38 = Coffee(name='Cafe Au Lait',
                       shopId='7',
                       description="Drip coffee, with steamed milk, or 'au lait'.",
                       caffeine='125',
                       type='Hot',
                       imgSrc='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F2af30573-1a9a-49a5-9b06-79ba9ac8d92e%2Foriginal.jpg%3Fv%3D63778510859&quality=85&w=320&h=0&mode=auto&format=&v=4',
                       )


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
    db.session.add(coffee19)
    db.session.add(coffee20)
    db.session.add(coffee21)
    db.session.add(coffee22)
    db.session.add(coffee23)
    db.session.add(coffee24)
    db.session.add(coffee25)
    db.session.add(coffee26)
    db.session.add(coffee27)
    db.session.add(coffee28)
    db.session.add(coffee29)
    db.session.add(coffee30)
    db.session.add(coffee31)
    db.session.add(coffee32)
    db.session.add(coffee33)
    db.session.add(coffee34)
    db.session.add(coffee35)
    db.session.add(coffee36)
    db.session.add(coffee37)
    db.session.add(coffee38)

    db.session.commit()


def undo_coffees():
    db.session.execute('TRUNCATE coffees;')
    db.session.commit()
