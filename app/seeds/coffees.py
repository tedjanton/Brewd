from app.models import db, Coffee


def seed_coffees():
    coffee1 = Coffee(shop_id=1,
                     name="Golden Mylk Latte",
                     description="An ancient Indian Elixir. Almond Milk, Honey, Turmeric, Cinnamon, Ginger, Ashwagandha, Black Pepper, Espresso (Double Shot)",
                     caffeine=203,
                     type="hot",
                     img_src="/static/coffee-pics/01-golden-mylk-latte.jpeg")

    coffee2 = Coffee(shop_id=1,
                     name="Cold Brew + Hazelnut Truffle",
                     description="Cold Brew Coffee, Cacao, Frozen Bananas, House made Toasted Hazelnut Milk, Coconut Caramel, Vanilla, Sea Salt, Maple Syrup.",
                     caffeine=231,
                     type="cold",
                     img_src="/static/coffee-pics/02-cold-brew-hazelnult-truffle.jpeg")

    coffee3 = Coffee(shop_id=1,
                     name="Pistachio + Rose Latte",
                     description="Inspired by the Turkish Delight. Made with house made Pistachio Milk, Rose Syrup, Espresso (double shot)",
                     caffeine=167,
                     type="hot",
                     img_src="/static/coffee-pics/03-pistachio-rose-latte.jpeg")

    # Metric
    coffee4 = Coffee(shop_id=2,
                     name="Cappuccino",
                     description="Simple, yet tasty and rich.",
                     caffeine=170,
                     type="hot",
                     img_src="/static/coffee-pics/04-cappucino.jpeg")

    coffee5 = Coffee(shop_id=2,
                     name="Maple + Maca + Pecan",
                     description="House made Pecan Milk, Maple Syrup, Maca, Espresso (Double Shot)",
                     caffeine=210,
                     type="hot",
                     img_src="/static/coffee-pics/05-maple-maca-pecan.jpeg")

    coffee6 = Coffee(shop_id=2,
                     name="Hazelnut Horchata Latte",
                     description="House made Toasted Hazelnut Milk, Rice Milk, Coconut Milk, Vanilla, Cinnamon, Maple Syrup, Espresso (Double Shot)",
                     caffeine=212,
                     type="hot",
                     img_src="/static/coffee-pics/06-hazelnut-horchata-latte.jpeg")

    # Four Letter Word
    coffee7 = Coffee(shop_id=3,
                     name="Cinnamon Dolce Latte",
                     description="We add freshly steamed milk and cinnamon dolce-flavored syrup to our classic espresso, topped with sweetened whipped cream and a cinnamon dolce topping to bring you specialness in a treat.",
                     caffeine=95,
                     type="hot",
                     img_src="/static/coffee-pics/07-cinnamon-dolce-latte.jpeg")

    coffee8 = Coffee(shop_id=3,
                     name="Caramel Macchiato",
                     description="Freshly steamed milk with vanilla-flavored syrup marked with espresso and topped with a caramel drizzle for an oh-so-sweet finish.",
                     caffeine=104,
                     type="hot",
                     img_src="/static/coffee-pics/08-caramel-macchiato.jpeg")

    coffee9 = Coffee(shop_id=3,
                     name="Irish Cream Nitro Cold Brew",
                     description="This on-tap holiday drink awakens the merry: a velvety-smooth blend of Starbucks® Nitro Cold Brew with Irish cream syrup, topped with vanilla sweet cream cold foam and cocoa.",
                     caffeine=232,
                     type="cold",
                     img_src="/static/coffee-pics/09-irish-cream-nitro-cold-brew.jpeg")

    # Sip & Savor
    coffee10 = Coffee(shop_id=4,
                      name="Banana Mocha",
                      description="Chocolate sauce, banana syrup, 2 shots of espresso, steamed milk with whip cream.",
                      caffeine=62,
                      type="hot",
                      img_src="/static/coffee-pics/10-banana-mocha.jpeg")

    coffee11 = Coffee(shop_id=4,
                      name="Caramel Nut Shake",
                      description="Caramel sauce, caramel, and hazelnut syrup, 2 scoops of ice cream, a dash of milk, a cup of ice, 2 shots of espresso all blended and topped with whip cream.",
                      caffeine=84,
                      type="cold",
                      img_src="/static/coffee-pics/11-caramel-nut-shake.jpeg")

    coffee12 = Coffee(shop_id=4,
                      name="Tuxedo Mocha",
                      description="Dark and white chocolate sauce, coconut syrup, 2 shots of intense espresso and steamed milk with whip cream.",
                      caffeine=102,
                      type="hot",
                      img_src="/static/coffee-pics/12-tuxedo-mocha.jpeg")

    # The Wormhole
    coffee13 = Coffee(shop_id=5,
                      name="Honey Bear Latte",
                      description="Created with locally sourced honey and two shots of espresso.",
                      caffeine=188,
                      type="hot",
                      img_src="/static/coffee-pics/13-honey-bear-latte.jpeg")

    coffee14 = Coffee(shop_id=5,
                      name="Peanut Butter Koopa-Troopa",
                      description="Made with peanut mousse and local chocolate.",
                      caffeine=57,
                      type="cold",
                      img_src="/static/coffee-pics/14-peanut-butter-koopa-troopa.jpeg")

    coffee15 = Coffee(shop_id=5,
                      name="Homemade Vanilla Bean",
                      description="The House Special. A simple vanilla latte dusted with vanilla bean seeds.",
                      caffeine=103,
                      type="hot",
                      img_src="/static/coffee-pics/15-homemade-vanilla-bean.jpeg")

    # Caffé Streets
    coffee16 = Coffee(shop_id=6,
                      name="Macchiato",
                      description="An espresso with a dash of frothy steamed milk.",
                      caffeine=150,
                      type="hot",
                      img_src="/static/coffee-pics/16-macchiato.jpeg")

    coffee17 = Coffee(shop_id=6,
                      name="Espresso",
                      description="Our smooth signature Espresso Roast with rich flavor and caramelly sweetness is at the very heart of everything we do.",
                      caffeine=130,
                      type="hot",
                      img_src="/static/coffee-pics/17-espresso.jpeg")

    coffee18 = Coffee(shop_id=6,
                      name="Whipped Mocha Delight",
                      description="We blend mocha sauce and mocha chips with coffee, milk and ice, then top it off with whipped cream and a mocha drizzle to bring you endless java joy.",
                      caffeine=93,
                      type="cold",
                      img_src="/static/coffee-pics/18-whipped-mocha-delight.jpeg")

    # alfred
    coffee19 = Coffee(name='Iced Vanilla Latte',
                       shop_id=7,
                       description='Behold our “World Famous” Iced Vanilla Latte: a double shot of espresso over milk and a helping of housemade vanilla – made with real vanilla bean.',
                       caffeine=200,
                       type='Cold',
                       img_src='https://i.pinimg.com/originals/79/cd/a2/79cda2b03a10dc87c80266508033682c.jpg')

    coffee20 = Coffee(name='Iced Matcha Latte',
                       shop_id=7,
                       description='Alfred’s own shade-grown, single-origin, tea-master blended matcha with the milk of your choice. No simpler way to CRUSH the day.',
                       caffeine=100,
                       type='Cold',
                       img_src='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F13c18270-5519-4e9c-aa55-3cda9727fdf8%2Foriginal.jpg%3Fv%3D63778513865&quality=85&w=320&h=0&mode=auto&format=&v=4')

    coffee21 = Coffee(name='Cagaccino',
                       shop_id=7,
                       description='Chaga, the superhero of the mushroom world, stars here in our most popular special where it is blended with vanilla, cacao, cinnamon, monkfruit, and topped with espresso and milk.',
                       caffeine=80,
                       type='Hot',
                       img_src='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2Fb28bfc57-e7c7-4390-9bde-90ddd8b13d68%2Foriginal.jpg%3Fv%3D63778513030&quality=85&w=320&h=0&mode=auto&format=&v=4')

    # jo's
    coffee22 = Coffee(name='Iced Turbo',
                       shop_id=11,
                       description='Our signature sweet drink made with coffee, espresso, chocolate, hazelnut, and cream.',
                       caffeine=125,
                       type='Cold',
                       img_src='https://www.austin360.com/storyimage/TX/20170706/ENTERTAINMENT/307069804/AR/0/AR-307069804.jpg')

    coffee23 = Coffee(name='Cortado',
                       shop_id=11,
                       description='Double shot of espresso topped with 4oz of steamed milk.',
                       caffeine=110,
                       type='Hot',
                       img_src='https://perfectdailygrind.com/wp-content/uploads/2020/03/Cortadito-1.png')

    # merit
    coffee24 = Coffee(name='Dirty Chai Latte',
                       shop_id=8,
                       description='Chai tea with steamed milk and a shot of espresso.',
                       caffeine=85,
                       type='Hot',
                       img_src='https://raster-static.postmates.com/?url=com.postmates.img.prod.s3.amazonaws.com%2F2b616f0c-c417-4b5b-aea5-40ffef86a116%2Forig.jpg&quality=85&w=500&h=0&mode=auto&format=webp&v=4')

    coffee25 = Coffee(name='Iced Coffee',
                       shop_id=8,
                       description='Our signature Cold Brew coffee served over ice.',
                       caffeine=175,
                       type='Cold',
                       img_src='https://i5.walmartimages.com/asr/7e29785b-9858-4aae-be64-ba96bafe299d.485f44a394c1b2d4829872f1bfb2f3de.jpeg')


    coffee26 = Coffee(name='Caffe Americano',
                       shop_id=8,
                       description='Espresso shots topped with hot water create a light layer of crema culminating in this wonderfully rich cup with depth and nuance. Pro Tip: For an additional boost, ask your barista to try this with an extra shot.',
                       caffeine=225,
                       type='Hot',
                       img_src='https://globalassets.starbucks.com/assets/f12bc8af498d45ed92c5d6f1dac64062.jpg?impolicy=1by1_wide_1242')

    coffee27 = Coffee(name='Cappuccino',
                       shop_id=8,
                       description='Dark, rich espresso lies in wait under a smoothed and stretched layer of thick milk foam. An alchemy of barista artistry and craft.',
                       caffeine=150,
                       type='Hot',
                       img_src='https://globalassets.starbucks.com/assets/5c515339667943ce84dc56effdf5fc1b.jpg?impolicy=1by1_wide_1242')

    # houndstooth
    coffee28 = Coffee(name='Honey Almondmilk Flat White',
                       shop_id=9,
                       description='This flat white intentionally pairs almondmilk and Blonde Espresso Roast with a hint of honey, making a perfect amount of creamy, nutty sweetness.',
                       caffeine=150,
                       type='Hot',
                       img_src='https://globalassets.starbucks.com/assets/77801559b72b469583f4d484adc1bfa7.jpg?impolicy=1by1_wide_1242')

    coffee29 = Coffee(name='Salted Caramel Cream Cold Brew',
                       shop_id=9,
                       description="Here's a savory-meets-sweet refreshing beverage certain to delight: our signature, super-smooth cold brew, sweetened with a touch of caramel and topped with a salted, rich cold foam.",
                       caffeine=185,
                       type='Cold',
                       img_src='https://globalassets.starbucks.com/assets/6ffca0a4b4ec4af98d07c4e860baca45.jpg?impolicy=1by1_wide_1242')

    coffee30 = Coffee(name='Nitro Cold Brew',
                       shop_id=9,
                       description="Our small-batch cold brew—slow-steeped for a super-smooth taste—gets even better. We're infusing it with nitrogen to create a sweet flavor without sugar and cascading, velvety crema. Perfection is served.",
                       caffeine=280,
                       type='Cold',
                       img_src='https://globalassets.starbucks.com/assets/85ae42ce9eb5423d83c4410f7b561882.jpg?impolicy=1by1_wide_1242')

    coffee31 = Coffee(name='Nitro Flat White',
                       shop_id=9,
                       description='Our bold ristretto shots of espresso mingle with the perfect amount of cold, creamy nitrogen-infused whole milk. The end result: an irresistible velvety crema.',
                       caffeine=130,
                       type='Cold',
                       img_src='https://globalassets.starbucks.com/assets/44dfc376272044878f2c8ee32cc7ca7e.jpg')

    coffee32 = Coffee(name='Iced Cinnamon Dolce Latte',
                       shop_id=9,
                       description='We add freshly steamed milk and cinnamon dolce-flavored syrup to our classic espresso and ice, topped with sweetened whipped cream and a cinnamon dolce topping to bring you specialness in a treat.',
                       caffeine=150,
                       type='Cold',
                       img_src='https://globalassets.starbucks.com/assets/2a7651bc593044ba9043e90ddc20e3f1.jpg?impolicy=1by1_wide_1242')
    # halcyon
    coffee33 = Coffee(name='Iced Caramel Macchiato',
                       shop_id=10,
                       description='We combine our rich, full-bodied espresso with vanilla-flavored syrup, milk and ice, then top it off with a caramel drizzle for an oh-so-sweet finish.',
                       caffeine=150,
                       type='Cold',
                       img_src='https://globalassets.starbucks.com/assets/79bfec31ab7447f691b3c48f39cc7661.jpg?impolicy=1by1_wide_1242')

    coffee34 = Coffee(name='Blonde Roast',
                       shop_id=10,
                       description="Lightly roasted coffee that's soft, mellow and flavorful. Easy-drinking on its own and delicious with milk, sugar or flavored with vanilla, caramel or hazelnut.",
                       caffeine=360,
                       type='Hot',
                       img_src='https://globalassets.starbucks.com/assets/abb4f97948c948c28ea2dcaf933c4f6b.jpg?impolicy=1by1_wide_1242')

    coffee35 = Coffee(name='Iced Mocha',
                       shop_id=10,
                       description='Silky housemade dark chocolate (vegan, soy-free) mixed with a double shot of espresso, topped with ice and milk.',
                       caffeine=220,
                       type='Cold',
                       img_src='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F682f540e-5784-4838-a987-5162d9e7d96f%2Foriginal.jpg%3Fv%3D63771239607&quality=85&w=320&h=0&mode=auto&format=&v=4')
    # alfred
    coffee36 = Coffee(name='Iced Chai Latte',
                       shop_id=7,
                       description='Our signature spicy-sweet black tea brewed with cinnamon, ginger, cardamom, and molasses. Iced and mixed with milk.',
                       caffeine=95,
                       type='Cold',
                       img_src='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F3fb11e45-451d-4d08-8b3a-46a1d73c25af%2Foriginal.jpg%3Fv%3D63778552251&quality=85&w=320&h=0&mode=auto&format=&v=4')

    coffee37 = Coffee(name='Red Eye',
                       shop_id=7,
                       description='Drip coffee, spiked with an additional double-shot of espresso.',
                       caffeine=350,
                       type='Hot',
                       img_src='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F29b7ef39-fdd3-4fba-9ea3-8fda5c05d93c%2Foriginal.jpg%3Fv%3D63778512427&quality=85&w=320&h=0&mode=auto&format=&v=4')

    coffee38 = Coffee(name='Cafe Au Lait',
                       shop_id=7,
                       description="Drip coffee, with steamed milk, or 'au lait'.",
                       caffeine=125,
                       type='Hot',
                       img_src='https://raster-static.postmates.com/?url=https%3A%2F%2Fitems-static.postmates.com%2Fuploads%2Fmedia%2F2af30573-1a9a-49a5-9b06-79ba9ac8d92e%2Foriginal.jpg%3Fv%3D63778510859&quality=85&w=320&h=0&mode=auto&format=&v=4',
                       )

    #Brewed Awakenings Cafe

    coffee39 = Coffee(shop_id=13,
                      name="Almond Joy",
                      description="Dark chocolate, coconut, & almond; topped with whipped cream and chocolate drizzle. (Double Shot)",
                      caffeine=89,
                      type="cold",
                      img_src="https://sugarandcharm.com/wp-content/uploads/2017/12/Almond-Joy-Coffee-Recipe-_-Sugar-and-Charm-_4.jpg")

    coffee40 = Coffee(shop_id=13,
                      name="German Chocolate Cake",
                      description="A blend of dark chocolate, caramel, coconut, & hazelnut; topped with whipped cream, caramel drizzle, & chocolate drizzle. (Double Shot)",
                      caffeine=114,
                      type="cold",
                      img_src="https://mylifecookbook.com/wp-content/uploads/2017/08/german-chocolate-cake-cold-brew-closeup.jpg")

    coffee41 = Coffee(shop_id=13,
                      name="Snickerdoodle",
                      description="Brown sugar brewed with espresso; flavored with cinnamon & vanilla & topped with whipped cream & cinnamon sugar. (Double Shot)",
                      caffeine=140,
                      type="cold",
                      img_src="https://i2.wp.com/mildlymeandering.com/wp-content/uploads/2017/05/03-Snickerdoodle-Iced-Coffee.jpg?fit=2212%2C3318&ssl=1")

    # Backyard Beans Coffee Company

    coffee42 = Coffee(shop_id=14,
                      name="Cold Brew",
                      description="Nitro roasts from our tap!",
                      caffeine=38,
                      type="cold",
                      img_src="https://backyardbeansmenu.square.site/uploads/1/3/1/2/131295791/s344115646224029765_p93_i1_w667.jpeg")

    coffee43 = Coffee(shop_id=14,
                      name="Park",
                      description="Cold Coffee with Nitro",
                      caffeine=140,
                      type="cold",
                      img_src="https://backyardbeansmenu.square.site/uploads/1/3/1/2/131295791/s344115646224029765_p82_i11_w2250.jpeg?width=1280")

    coffee44 = Coffee(shop_id=14,
                      name="Stay Home A-Latte",
                      description='Check out our new seasonal latte jug! "Stay Home A-Latte" -- amazing lattee flavors in whole milk or oat milk',
                      caffeine=100,
                      type="cold",
                      img_src="https://backyardbeansmenu.square.site/uploads/1/3/1/2/131295791/s344115646224029765_p87_i1_w1280.jpeg")

    # Zingerman's Coffee Company

    coffee45 = Coffee(shop_id=15,
                      name="Honey Lavendar Latte",
                      description="Put some Spring in your step! Zingerman's Coffee Company Espresso with your choice of milk, a note of lavender, and a touch of honey.",
                      caffeine=72,
                      type="hot",
                      img_src="https://zingermanscoffee.square.site/uploads/1/3/1/2/131291948/s575944292690166176_p77_i1_w2451.png")

    coffee46 = Coffee(shop_id=15,
                      name="Café Au Lait",
                      description="Coffee with your choice of steamed milk.",
                      caffeine=100,
                      type="hot",
                      img_src="https://zingermanscoffee.square.site/uploads/1/3/1/2/131291948/s575944292690166176_p50_i1_w720.jpeg")

    coffee47 = Coffee(shop_id=15,
                      name="Fortissimo",
                      description="A cappuccino with an extra shot of espresso and your choice of steamed milk.",
                      caffeine=126,
                      type="hot",
                      img_src="https://zingermanscoffee.square.site/uploads/1/3/1/2/131291948/s575944292690166176_p48_i1_w720.jpeg")

    # RoosRoast Liberty
    coffee48 = Coffee(shop_id=16,
                      name="flat white",
                      description="espresso and steamed milk",
                      caffeine=100,
                      type="hot",
                      img_src="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/flat-white-d8ada0f.jpg?quality=90&webp=true&resize=440,400")

    coffee49 = Coffee(shop_id=16,
                      name="honey vanilla latte",
                      description="honey, milk, vanilla, topped with whipped cream",
                      caffeine=94,
                      type="hot",
                      img_src="https://bakingbites.com/wp-content/uploads/2019/01/DSC_4992-001.jpg")

    coffee50 = Coffee(shop_id=16,
                      name="hot choc cold brew",
                      description="",
                      caffeine=345,
                      type="cold",
                      img_src="https://chowhound3.cbsistatic.com/resize/b4ef5bef6258f7f835ced9287bd8fa6605884bb6/2020/08/how-to-make-better-iced-coffee-hot-bloom-cold-brew-chowhound.jpg?fit=bounds&width=800")

    # Elixr Coffee Roasters
    coffee51 = Coffee(shop_id=17,
                      name="Pourover",
                      description="Chemex hand pour! Single Origin coffee brewed to order. A more subtle, delicate cup of coffee.",
                      caffeine=89,
                      type="hot",
                      img_src="https://www.elixrpickup.com/uploads/1/3/1/2/131257535/s667221471220806671_p447_i1_w1200.jpeg")

    coffee52 = Coffee(shop_id=17,
                      name="Double Espresso",
                      description="One double shot of Beekeeper espresso blend.",
                      caffeine=164,
                      type="hot",
                      img_src="https://www.elixrpickup.com/uploads/1/3/1/2/131257535/s667221471220806671_p254_i2_w250.jpeg")

    coffee53 = Coffee(shop_id=17,
                      name="Mocha",
                      description="Espresso, Milk, Chocoloate = YUM!",
                      caffeine=72,
                      type="cold",
                      img_src="https://www.elixrpickup.com/uploads/1/3/1/2/131257535/s667221471220806671_p257_i2_w1280.jpeg")

    # ReAnimator Coffee
    coffee54 = Coffee(shop_id=18,
                      name="Malt Ball Latte",
                      description="A tasty treat made with malted milk powder! Contains dairy.",
                      caffeine=90,
                      type="hot",
                      img_src="https://www.reanimatorpickup.com/uploads/1/3/1/2/131268903/s226671392685346693_p288_i1_w977.png")

    coffee55 = Coffee(shop_id=18,
                      name="Americano",
                      description="Espresso + Hot Water",
                      caffeine=89,
                      type="hot",
                      img_src="https://www.reanimatorpickup.com/uploads/1/3/1/2/131268903/s226671392685346693_p33_i1_w977.png")

    coffee56 = Coffee(shop_id=18,
                      name="Cortado",
                      description="Espresso + 2 oz of Milk",
                      caffeine=89,
                      type="hot",
                      img_src="https://www.reanimatorpickup.com/uploads/1/3/1/2/131268903/s226671392685346693_p20_i2_w977.png")

    coffee57 = Coffee(shop_id=18,
                      name="Cappuccino",
                      description="Espresso + 3.5 oz of Milk",
                      caffeine=89,
                      type="hot",
                      img_src="https://www.reanimatorpickup.com/uploads/1/3/1/2/131268903/s226671392685346693_p2_i1_w977.png")

    # Americano Lounge
    coffee58 = Coffee(shop_id=19,
                      name="Feel'n Good",
                      description="Banhez Mezcal, Red Eye Eye, Espresso, Vanilla, and Cream.",
                      caffeine=203,
                      type="hot",
                      img_src="/static/coffee-pics/americano_lounge_feeln_good.jpg")

    coffee59 = Coffee(shop_id=19,
                      name="Espresso Martini",
                      description="Wheatley Vodka, Red Eye Eye, Espresso, and Vanilla.",
                      caffeine=210,
                      type="cold",
                      img_src="/static/coffee-pics/americano_lounge_espresso_martini.jpg")

    coffee60 = Coffee(shop_id=19,
                      name="Bohemia After Dark",
                      description="Wheatley vodka, Libre Mind Chocolate, Giffard Menthepastille, Fernet and Cream.",
                      caffeine=180,
                      type="hot",
                      img_src="/static/coffee-pics/americano_lounge_bohemia_after_dark.jpg")

    # 8th & Roast
    coffee61 = Coffee(shop_id=20,
                      name="Drip Coffee",
                      description="Simple, yet tasty and rich.",
                      caffeine=180,
                      type="hot",
                      img_src="/static/coffee-pics/8thandRoast_drip_coffee.jpg")

    coffee62 = Coffee(shop_id=20,
                      name="Dulce De Leche Latte",
                      description="House made latte infused with Dulce De Leche flavored organic syrup.",
                      caffeine=170,
                      type="hot",
                      img_src="/static/coffee-pics/8thandRoast_dulce_de_leche_latte.jpg")

    coffee63 = Coffee(shop_id=20,
                      name="Flash Chilled Nitro",
                      description="House made dripped chilled instantly with our unique nitro machine",
                      caffeine=212,
                      type="cold",
                      img_src="/static/coffee-pics/8thandRoast_flash_chilled_nitro.jpg")

    # Ugly Mugs
    coffee64 = Coffee(shop_id=21,
                      name="Hoodie",
                      description="Honey, Vanilla, & Cinnamon Latte.",
                      caffeine=190,
                      type="hot",
                      img_src="/static/coffee-pics/ugly_mugs_hoodie.jpg")

    coffee65 = Coffee(shop_id=21,
                      name="Bingster",
                      description="Latte with sweetened condensed milk.",
                      caffeine=182,
                      type="cold",
                      img_src="/static/coffee-pics/ugly_mugs_bingster.jpg")

    coffee66 = Coffee(shop_id=21,
                      name="Lavender Latte",
                      description="Made with housemade lavender syrup.",
                      caffeine=192,
                      type="hot",
                      img_src="/static/coffee-pics/ugly_mugs_lavender_latte.jpg")

    # Buddy Brew Coffee
    coffee67 = Coffee(shop_id=22,
                      name="Buddy Brew Screw",
                      description="So screwed up, it just might be the cup of joe you were looking to fix your broken day.",
                      caffeine=220,
                      type="hot",
                      img_src="/static/coffee-pics/buddy_brew_coffee_buddy_brew_screw.jpg")

    coffee68 = Coffee(shop_id=22,
                      name="Cortado",
                      description='Cortado (from the Spanish cortar, known as "Tallat" in Catalan, "Pingo" or "Garoto" in Portugal and "noisette" in France) is an espresso "cut" with a small amount of warm milk to reduce the acidity. The ratio of coffee to milk is between 1:1 - 1:2, and the milk is added after the espresso',
                      caffeine=220,
                      type="hot",
                      img_src="/static/coffee-pics/buddy_brew_coffee_cortado.jpg")

    coffee69 = Coffee(shop_id=22,
                      name="Cold Brew Float",
                      description="Our delicious house coffee steeped for 24 hours and then served over a refreshing cup of ice",
                      caffeine=190,
                      type="cold",
                      img_src="/static/coffee-pics/bennetts_fresh_roast_cold_brew.jpg")

    # Bennett's Fresh Roast
    coffee70 = Coffee(shop_id=23,
                      name="The Biscoff Latte",
                      description="We all love those delicious Biscoff Cookies. The Biscoff Latte is a Bennett's Latte with the special addition of Biscoff Butter, whipped cream and a crumbled Biscoff Cookie on top",
                      caffeine=188,
                      type="hot",
                      img_src="/static/coffee-pics/bennetts_fresh_roast_biscoff_latte.jpg")

    coffee71 = Coffee(shop_id=23,
                      name="Bennett's Colombian Cup In-House",
                      description="Served in a Bennett's Fresh Roast Mug, this in-shop fresh roasted coffee is brewed in bold, mild, or decaf.",
                      caffeine=190,
                      type="hot",
                      img_src="/static/coffee-pics/bennetts_fresh_roast_colombian_in-house_brew.jpg")

    coffee72 = Coffee(shop_id=23,
                      name="Bennet's Cold Brew",
                      description="Made in house and kept ice cold from start to finish, Bennett's Cold Brew steeps for up to 18 hours to bring out the smoothness of Cold Brew with all the flavor of Bennett's Fresh Roasted Coffee.",
                      caffeine=220,
                      type="cold",
                      img_src="/static/coffee-pics/bennetts_fresh_roast_cold_brew.jpg")

    # Canes Corner and Coffee Store
    coffee73 = Coffee(shop_id=24,
                      name="Coconut White Macchiato",
                      description="An espresso with a dash of frothy steamed coconut milk.",
                      caffeine=150,
                      type="hot",
                      img_src="/static/coffee-pics/canes_corner_and_coffee_store_coconut_macchiato.jpg")

    coffee74 = Coffee(shop_id=24,
                      name="Rasberry White Mocha",
                      description="An espresso with a dash of frothy steamed milk and rasberry topping.",
                      caffeine=130,
                      type="hot",
                      img_src="/static/coffee-pics/canes_corner_and_coffee_store_rasberry_white_mocha.jpg")

    coffee75 = Coffee(shop_id=24,
                      name="Peanut Butter Mocha",
                      description="We blend mocha sauce and chocolate mocha chips with coffee, milk and ice, then top it off with whipped cream and a peanut butter drizzle to bring you endless java joy.",
                      caffeine=93,
                      type="cold",
                      img_src="/static/coffee-pics/canes_corner_and_coffee_store_peanut_butter_mocha.jpg")

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
    db.session.add(coffee39)
    db.session.add(coffee40)
    db.session.add(coffee41)
    db.session.add(coffee42)
    db.session.add(coffee43)
    db.session.add(coffee44)
    db.session.add(coffee45)
    db.session.add(coffee46)
    db.session.add(coffee47)
    db.session.add(coffee48)
    db.session.add(coffee49)
    db.session.add(coffee50)
    db.session.add(coffee51)
    db.session.add(coffee52)
    db.session.add(coffee53)
    db.session.add(coffee54)
    db.session.add(coffee55)
    db.session.add(coffee56)
    db.session.add(coffee57)
    db.session.add(coffee58)
    db.session.add(coffee60)
    db.session.add(coffee61)
    db.session.add(coffee62)
    db.session.add(coffee63)
    db.session.add(coffee64)
    db.session.add(coffee65)
    db.session.add(coffee66)
    db.session.add(coffee67)
    db.session.add(coffee68)
    db.session.add(coffee69)
    db.session.add(coffee70)
    db.session.add(coffee71)
    db.session.add(coffee72)
    db.session.add(coffee73)
    db.session.add(coffee74)
    db.session.add(coffee75)

    db.session.commit()


def undo_coffees():
    db.session.execute('TRUNCATE coffees CASCADE;')
    db.session.commit()
