import telebot;
bot = telebot.TeleBot('6457106032:AAG1Qjmt_RbS4d-bUea9RgBiywFOG2yR-Xs')
from telebot import types
@bot.message_handler(commands=['start'])
def start(message):

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton("🇬🇧 English")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_massages(message):

    #Russian language

    if message.text == "🇷🇺 Русский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍿 Кино")
        btn2 = types.KeyboardButton("🎭 Театр")
        btn3 = types.KeyboardButton("🏛️ Музей")
        btn4 = types.KeyboardButton("🌳 Городские парки")
        btn5 = types.KeyboardButton("🍽️ Кафе")
        btn6 = types.KeyboardButton("🥂 Клубы")
        btn7 = types.KeyboardButton("🔙 Вернуться к выбору языка")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "👀 Выберите интересующий Вас раздел", reply_markup=markup)

    elif message.text == "🔙 Вернуться к выбору языка":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton("🇬🇧 English")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == "🍿 Кино":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍿 Нижегородский")
        btn2 = types.KeyboardButton("🍿 Советский")
        btn3 = types.KeyboardButton("🍿 Приокский")
        btn4 = types.KeyboardButton("🍿 Сормовский")
        btn5 = types.KeyboardButton("🍿 Московский")
        btn6 = types.KeyboardButton("🍿 Канавинский")
        btn7 = types.KeyboardButton("🍿 Ленинский")
        btn8 = types.KeyboardButton("🍿 Автозаводский")
        btn9 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "⬇ Выберите район Нижнего Новгорода, в котором Вы проживаете", reply_markup=markup)

    elif message.text == "🍿 Нижегородский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn221 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn221)
        bot.send_message(message.from_user.id, "В Нижегородском районе мы советуем следующие кинотеатры:\n\n🎬 Синема Парк в ТРК «Фантастика»: кинотеатр «Синема Парк» в торгово-развлекательном комплексе «Фантастика» предлагает посетителям 8 комфортабельных залов с большим количеством посадочных мест. "
                                               "Зрители откроют для себя огромный выбор киноновинок, а новые сеансы здесь стартуют каждые 15 минут. Пять залов из восьми оснащены современным оборудованием для показа фильмов в формате RealD 3D, завоевавшем популярность зрителей всех возрастов. "
                                               "Для тех, кто предпочитает смотреть фильмы в более уединённой обстановке, предусмотрен зал Relax, рассчитанный на 34 зрителя. Ознакомиться с проводимыми сеансами Вы можете по [ссылке](https://clck.ru/QgHkQ)."
                                               "\n\n🎬 Империя Грез в ТРК «Небо»: современный 8-зальный мультиплекс «Империя грез» в ТРК «Небо» на пл. Лядова, включающий в себя 7 залов, которые оборудованы ультрасовременной системой 3D Master image и акустической системой JBL. "
                                               "Зал ATMOS, оснащен инновационной технологией Dolby Atmos, которая, по мнению экспертов, становится «новой вехой в развитии кинотеатров». Ознакомиться с проводимыми сеансами Вы можете по [ссылке](https://clck.ru/36BNwo).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🍿 Советский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn331 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn331)
        bot.send_message(message.from_user.id, "🎬 В Советском районе не так много хороших кинотеатров, советуем для посещения Арлекино в ТРЦ «Жар-Птица»: это первый семейный кинотеатр в Нижнем Новгороде. Семь уютных кинозалов, новейшее кинопроекционное и звуковое оборудование, "
                                               "активная система 3D изображения, удобное расстояние между рядами в залах и мягкие кресла с поднимающимися подлокотниками с подставками для напитков и всегда ароматный свежеприготовленный попкорн в кинобаре – всё для комфортного отдыха в этом кинотеатре. "
                                               "Ознакомиться с проводимыми сеансами Вы можете по [ссылке](https://clck.ru/36BQ9K).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🍿 Приокский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn441 = types.KeyboardButton("🍿 Нижегородский")
        btn442 = types.KeyboardButton("🍿 Советский")
        btn443 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn441, btn442, btn443)
        bot.send_message(message.from_user.id, "🎬 В Приокском районе, к сожалению, нет кинотеатров. Советуем посетить кинотеатры в близлежащих районах Нижнего Новогода — Нижегородском и Советском.", reply_markup=markup)

    elif message.text == "🍿 Сормовский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn551 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn551)
        bot.send_message(message.from_user.id, "🎬 В Сормовском районе можем посоветовать кинотеатр Империя Грез в ТРК «Золотая Миля»: современный 5-ти зальный кинотеатр. Для посетителей открыты 5 кинозалов на 798 мест для просмотра фильмов в 2D и 3D формате, "
                                               "для приятного ожидания есть удобное и просторное фойе, а также детские игровые автоматы., Ознакомиться с проводимыми сеансами Вы можете по [ссылке](https://clck.ru/36BQvh).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🍿 Московский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn661 = types.KeyboardButton("🍿 Сормовский")
        btn662 = types.KeyboardButton("🍿 Канавинский")
        btn663 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn661, btn662, btn663)
        bot.send_message(message.from_user.id, "🎬 В Московском районе, к сожалению, нет кинотеатров. Советуем посетить кинотеатры в близлежащих районах Нижнего Новогода — Сормовском и Канавинском.", reply_markup=markup)

    elif message.text == "🍿 Канавинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn771 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn771)
        bot.send_message(message.from_user.id, "В Нижегородском районе мы советуем следующие кинотеатры:\n\n🎬 Синема Парк в ТРЦ «Седьмое небо»: кинотеатр предлагает посетителям 10 комфортабельных залов с большим количеством посадочных мест. "
                                               "Мультиплекс Синема Парк сочетает в себе все актуальные на данный момент мировые тенденции кинопоказа, включая суперзал IMAX и 4DX™. Помимо суперзала IMAX, еще семь кинозалов оснащены цифровым оборудованием для демонстрации фильмов в формате 3D. "
                                               "Для просмотра фильма в неформальной обстановке предусмотрены специальные залы повышенной комфортности. Зал RELAX дает возможность насладиться просмотром фильмов в комфортных кожаных креслах, расслабиться в баре премиум-класса. "
                                               "Зал JOLLY отличает необычный дизайн, уютные двух- и четырёхместные диванчики, а также мягкие кресла-трансформеры. Атмосфера домашнего тепла и комфорта подходит как для большой компании друзей, так и для незабываемого романтического вечера влюблённой пары. "
                                               "Ознакомиться с проводимыми сеансами Вы можете по [ссылке](https://clck.ru/36BRX6).\n\n🎬 Синема в ТРЦ «Рио»: Пятизальный мультиплекс СИНЕМА соответствует самым высоким мировым стандартам кинопоказа. "
                                               "Цифровое качество формата Dolby Digital Surround EX позволяет насладится самыми тонкими оттенками звучания при просмотре фильма. Широкие кресла с качающимися спинками «rwin Seating» и оптимальное расстояние между рядами (1500 мм) "
                                               "позволяют посетителям чувствовать себя удобно во время просмотра даже самого продолжительного фильма. Ознакомиться с проводимыми сеансами Вы можете по [ссылке](https://clck.ru/36BRd5).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🍿 Ленинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn881 = types.KeyboardButton("🍿 Автозаводский")
        btn882 = types.KeyboardButton("🍿 Канавинский")
        btn883 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn881, btn882, btn883)
        bot.send_message(message.from_user.id, "🎬 В Ленинском районе, к сожалению, нет кинотеатров. Советуем посетить кинотеатры в близлежащих районах Нижнего Новогода — Автозаводском и Канавинском.", reply_markup=markup)

    elif message.text == "🍿 Автозаводский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn991 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn991)
        bot.send_message(message.from_user.id, "🎬 В Автозаводском районе можем посоветовать кинотеатр Имерия Грез «Мир»: кинотеатр располагается в здании, являющемся памятником архитектуры. Все внутренние элементы, представляющие собой историческую ценность, полностью отреставрированы. "
                                               "В кинотеатре есть уютное кафе, суши-бар, бильярд и караоке клуб. В холле первого этажа установлены игровые автоматы. Удобная транспортная развязка позволяет быстро добраться до кинотеатра на любом виде транспорта. "
                                               "В кинотеатре «Мир» установлены кинопроекторы Christie для показа цифровых 2D и 3D фильмов. Ознакомиться с проводимыми сеансами Вы можете по [ссылке](https://clck.ru/36BSPa).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🔙 Главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍿 Кино")
        btn2 = types.KeyboardButton("🎭 Театр")
        btn3 = types.KeyboardButton("🏛️ Музей")
        btn4 = types.KeyboardButton("🌳 Городские парки")
        btn5 = types.KeyboardButton("🍽️ Кафе")
        btn6 = types.KeyboardButton("🥂 Клубы")
        btn7 = types.KeyboardButton("🔙 Вернуться к выбору языка")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "👀 Выберите интересующий Вас раздел", reply_markup=markup)


    elif message.text == "🎭 Театр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn111 = types.KeyboardButton("🎭 Нижегородский")
        btn112 = types.KeyboardButton("🎭 Советский")
        btn113 = types.KeyboardButton("🎭 Приокский")
        btn114 = types.KeyboardButton("🎭 Сормовский")
        btn115 = types.KeyboardButton("🎭 Московский")
        btn116 = types.KeyboardButton("🎭 Канавинский")
        btn117 = types.KeyboardButton("🎭 Ленинский")
        btn118 = types.KeyboardButton("🎭 Автозаводский")
        btn9 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn111, btn112, btn113, btn114, btn115, btn116, btn117, btn118, btn9)
        bot.send_message(message.from_user.id, "⬇ Выберите район Нижнего Новгорода, в котором Вы проживаете", reply_markup=markup)

    elif message.text == "🎭 Нижегородский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Большинство театров города находится в исторической части города — в Нижегородском районе, здесы мы советуем посетить следующие театры:\n\n🎭 Нижегородский государственный академический театр драмы им. М. Горького: старейший театр Нижнего Новгорода, история которого началась больше 200 лет назад. "
                                               "Сегодня театр получил мировое признание, а классический репертуар постоянно обновляется яркими премьерами по современным произведениям. Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/LGizT)."
                                               "\n\n🎭 Нижегородский Дом актера им. В.В. Вихрова: творческая площадка, где проводятся спектакли, мастер-классы и театральные эксперименты. Недавно здесь открылась студия актёрского мастерства. "
                                               "Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/36BTDS).\n\n🎭 Нижегородский государственный академический театр оперы и балета имени А.С. Пушкина: старейший театр Нижнего Новгорода основан в 1931 году. "
                                               "В основе репертуара – классические произведения, причём не только самые популярные спектакли, но и те, о которых начали забывать. Уровень профессионализма режиссёров и актёров не оставляет равнодушным ни одного зрителя, "
                                               "поэтому театр считается одним из лучших в Нижнем Новгороде. Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/34YHLu).\n\n🎭 Нижегородский государственный академический театр кукол: Нижегородский театр кукол – лучшее место для детского праздника. "
                                               "Расположен в историческом здании 1912 года. За богатую историю в театре поставлено больше 320 спектаклей, и репертуар постоянно обновляется. Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/36BTUC)."
                                               "\n\n🎭 Театр юного зрителя: созданный в начале XX века театр делает акцент на постановке спектаклей для детей, но в репертуаре есть современные постановки для взрослых. ТЮЗ основан в 1928 году известным актёром "
                                               "и режиссёром Н. Собольщиковым-Самариным, имеет удобное расположение в центре города. Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/36BTZn).\n\n🎭 Нижегородский театр «Комедія»: театр основан в послевоенное время в качестве мини-театра «Снайпер», "
                                               "но со временем он стал ведущей театральной сценой с постановками в комедийном жанре. В театре работают талантливые режиссёры, лауреаты многочисленных премий. Любят «Комедію» за разнообразие репертуара и потрясающий интерьер. "
                                               "Репертуар театра многогранен и включает народные комедии, мюзикл-комиксы, трагифарсы, фантасмагорию и комедии-притчи. Спектакли проходят на нескольких сценах. Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/36BTjs).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🎭 Советский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎭 Нижегородский")
        btn2 = types.KeyboardButton("🎭 Сормовский")
        btn3 = types.KeyboardButton("🎭 Канавинский")
        btn4 = types.KeyboardButton("🎭 Ленинский")
        btn5 = types.KeyboardButton("🎭 Автозаводский")
        btn6 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, "🎭 В Советском районе нет театров. Но Вы всегда можете посетить театр в близлежащем районе — Нижегородском или в любой другой части города, мы уверены, что Вы обязательно найдете там что-то подходящее для себя😉", reply_markup=markup)

    elif message.text == "🎭 Приокский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎭 Нижегородский")
        btn2 = types.KeyboardButton("🎭 Сормовский")
        btn3 = types.KeyboardButton("🎭 Канавинский")
        btn4 = types.KeyboardButton("🎭 Ленинский")
        btn5 = types.KeyboardButton("🎭 Автозаводский")
        btn6 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, "🎭 В Приокском районе нет театров. Но Вы всегда можете посетить театр в близлежащем районе — Нижегородском или в любой другой части города, мы уверены, что Вы обязательно найдете там что-то подходящее для себя😉", reply_markup=markup)

    elif message.text == "🎭 Сормовский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🎭 В Сормовском районе к посещению можем посоветовать Нижегородский камерный музкальный театр им. В. Степанова: создатель музыкального театра – Владимир Степанов, в прошлом ведущий солист оперы и балета в России и за рубежом. "
                                               "Репертуар театра – классические балеты и мюзиклы. Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/36BUND).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🎭 Московский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎭 Нижегородский")
        btn2 = types.KeyboardButton("🎭 Сормовский")
        btn3 = types.KeyboardButton("🎭 Канавинский")
        btn4 = types.KeyboardButton("🎭 Ленинский")
        btn5 = types.KeyboardButton("🎭 Автозаводский")
        btn6 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, "🎭 В Московском районе нет театров. Но Вы всегда можете посетить театр в близлежащих районах — Сормовском и Канавинском или в любой другой части города.", reply_markup=markup)

    elif message.text == "🎭 Канавинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "В Канавинском районе к посещению можем посоветовать следующие театры:\n\n🎭 Театр нового поколения «Зазеркалье»: уникальный театр, в котором играют взрослые артисты и дети. В репертуаре театра есть спектакли как "
                                               "для самых маленьких зрителей (от 2 лет) и школьников, так и серьезные постановки для взрослых. Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/b78cq).\n\n 🎭 Театр Вера: театр предлагает разнообразный репертуар "
                                               "для маленьких зрителей. Возникший из обычной студии под руководством Веры Горшковой в 1976 году театр на сегодняшний день передвижной, ставит представления по всему Нижнему Новгороду. Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/36BV5v).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🎭 Ленинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🎭 В Ленинском районе к посещению можем посоветовать Театр музыкально-пластической драмы «Преображение»: театр возник в конце XX века и занимается профессиональным развитием музыкально-пластического жанра. В репертуаре фантасмагории, драмы, комедии, авторские спектакли, детская классика и концерты. "
                                               "Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/36BVHS).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🎭 Автозаводский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🎭 В Автозаводском районе к посещению можем посоветовать Нижегородский Независимый Театр на Счастливой: здесь подготовлено все необходимое для вашего досуга, а также тут возможно получить полезные навыки. Нижегородский Независимый Театр на Счастливой окажет содействие в достижении Вами поставленных целей. "
                                               "Ознакомиться с афишей Вы можете по [ссылке](https://clck.ru/36BVXg).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Музей":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton("🏛️ Нижегородский")
        btn12 = types.KeyboardButton("🏛️ Советский")
        btn13 = types.KeyboardButton("🏛️ Приокский")
        btn14 = types.KeyboardButton("🏛️ Сормовский")
        btn15 = types.KeyboardButton("🏛️ Московский")
        btn16 = types.KeyboardButton("🏛️ Канавинский")
        btn17 = types.KeyboardButton("🏛️ Ленинский")
        btn18 = types.KeyboardButton("🏛️ Автозаводский")
        btn9 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn9)
        bot.send_message(message.from_user.id, "⬇ Выберите район Нижнего Новгорода, в котором Вы проживаете", reply_markup=markup)

    elif message.text == "🏛️ Нижегородский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "В Нижегородском районе можем преложить Вам пойти в следующие музеи:\n\n 🏛️Нижегородский государственный художественный музей: здесь Вы увидите исторические картины и так же можете побывать в VR шлеме и рассмотреть картины вблизи и можете посетить их сайт перейдя по [ссылке](https://artmuseumnn.ru/)."
                                               "\n\n🏛️ Музей-филиал НГИАМЗ Нижегородский Кремль: здесь Вы можете посмотреть на множество техники нашей необъятной страны, а также можете посмотреть на великие стены Нижегородского Кремля, который таит в своих стенах многовековую историю. Можете больше ознакомиться перейдя по [ссылке](https://ngiamz.ru/nizhegorodskiy-kreml)."
                                               "\n\n🏛️ Технический музей: здесь Вы можете увидеть изобретения прошлых веков, которые теперь уже не используются в повседневной жизни. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://ngiamz.ru/tekhnicheskiy-muzey)."
                                               "\n\n🏛️ Музей живой бумаги: здесь Вы можете увидеть множество различных фигурок, созданных только с помощью обычной бумаги. Можете ближе ознакомиться с произведениями перейдя по [ссылке](https://vk.com/muzeyzhivoybumagi)."
                                               "\n\n🏛️ Игрушечный музей: здесь Вы можете увидеть много игрушек прошлого века и наглядно сравнить какие были раньше игрушки у детей, нежели чем сейчас. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://ngiamz.ru/igrushechnyy-muzey)."
                                               "\n\n🏛️ Музей техники и оборонной промышленности: здесь Вы можете посмотреть и потрогать вонную технику нашей великой державы! С более подробной информацией можете ознакомиться перейдя по [ссылке](https://park-pobeda-nn.ru/).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Советский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🏛️ В Советском районе можем преложить Вам пойти в Зоологический музей: здесь Вы можете увидеть множество макетов различных животных и погрузиться с головой в мир животных. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://museum.unn.ru/).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Приокский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🏛️ В Приокском районе можем преложить Вам пойти в Музей А. Д. Сахарова: здесь Вы можете познакомиться с жизнью советского физика-теоретика, академика АН СССР, общественного деятеля, диссидента и правозащитника. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://vk.com/sakharovmuseum).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Сормовский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🏛️ В Сормовском районе можем преложить Вам посетить музей «Назад в СССР»: здесь Вы можете прочувствовать на себе атмосферу СССР. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://ссср-музей.com/).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)


    elif message.text == "🏛️ Московский":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🏛️ Нижегородский")
        btn2 = types.KeyboardButton("🏛️ Сормовский")
        btn3 = types.KeyboardButton("🏛️ Канавинский")
        btn4 = types.KeyboardButton("🏛️ Ленинский")
        btn5 = types.KeyboardButton("🏛️ Автозаводский")
        btn6 = types.KeyboardButton("🏛️ Сормовский")
        btn7 = types.KeyboardButton("🏛️ Приокский")
        btn8 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, "🏛️ В Московском районе, к сожалению, нет музеев, но Вы можете посетить музей в любом другом районе Нижнего Новгорода.", reply_markup=markup)

    elif message.text == "🏛️ Канавинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🏛️ В Канавинском районе можем преложить Вам пойти в Кварки: здесь Вы познакомиться поближе с наукой и ее интересными фактами. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://kvarky.ru/).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Ленинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🏛️ В Ленинском районе можем преложить Вам пойти в Музей истории МПВО-ГО-РСЧС: здесь Вы можете посмотреть на старые и также до сих пор применяемые огнестрельные оружия. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://вдпо.рф/museum/169).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Автозаводский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "В Автозаводском районе можем преложить Вам пойти в следующие музей:\n\n🏛️ Музей истории ГАЗ: здесь Вы можете посмотреть на старые, но довольно известные машины, созданные раньше нашими инженерами строителями, которые вкладывали свою душу для создания этих легендарных машин. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://museum.gaz.ru/)."
                                               "\n\n🏛️ Музей Нижегородского метрополитена: здесь Вы можете ознакомиться как же строился и строится ВЕЛИКИЙ метрополитен Нижнего Новгорода. С более подробной информацией можете ознакомиться перейдя по [ссылке](http://metronn.ru/museum/).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🌳 Городские парки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn21 = types.KeyboardButton("🌳 Нижегородский")
        btn22 = types.KeyboardButton("🌳 Советский")
        btn23 = types.KeyboardButton("🌳 Приокский")
        btn24 = types.KeyboardButton("🌳 Сормовский")
        btn25 = types.KeyboardButton("🌳 Московский")
        btn26 = types.KeyboardButton("🌳 Канавинский")
        btn27 = types.KeyboardButton("🌳 Ленинский")
        btn28 = types.KeyboardButton("🌳 Автозаводский")
        btn9 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn9)
        bot.send_message(message.from_user.id, "⬇ Выберите район Нижнего Новгорода, в котором Вы проживаете", reply_markup=markup)

    elif message.text == "🌳 Нижегородский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌳 В Нижегородском районе можем посоветовать Вам прогуляться в парке «Александровский сад», где Вы так же сможете пройтись по всеми известной Чклаловской лестнице и, конечно же, увидеть памятник имени В.П. Чкалова. Парк находится рядом с рекой Волга, так что можно будет полюбоваться красивым видом."
        "\n\n🌳 Парк 800-летия Нижнего Новгорода, место подходящее для прогулок с детьми, в компании, влюбленных пар и просто одному. Безумно красивое место, советуем побывать там имеено в закат. Для детей имеются детские площадки, спортивные площадки для взрослых и тихие места, где можно уедениться и насладиться красотами города.", reply_markup=markup)

    elif message.text == "🌳 Советский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌳 В Советском районе советуем посетить Щёлоковский хутор. Это отличное место для прогулок и пикников. Есть грунтовые дорожки для велосипеда, которые зимой превращаются в лыжную трассу. В парке имеется 3 озера, где можно понаблюдать за уточками и даже можно их покормить, что очень нравится детям. Из минусов только отсутствие парковки для личного транспорта.", reply_markup=markup)

    elif message.text == "🌳 Приокский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌳 В Приокском районе можем посоветовать посетить парк Швейцария. Очень приятный парк, можно почувствовать себя в лесу, имеются различные виды развлечений для детей любого возраста, для детей постарше имеется специальная полоса препятствий. Великолепный вид на реку Оку с откоса. В случае если проголодаетесь, имеются кафешки с мороженным и кофе, а также крупные, как Хачапурия или Самурай. Из минусов только парковка, мест для машин точно меньше, чем желающих припаковаться рядом с парком.", reply_markup=markup)

    elif message.text == "🌳 Сормовский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌳 В Сормовском районе советуем посетить Сормовский парк: отличное место чтобы провести время с семьей или друзьями. Парк находится в зеленой зоне города, что создает атмосферу для отдыха и релакса. Для детей имеется несколько детских площадок. Так же в парке находится пруд с птицами и зоопарк, Вы сможете увидеть много разных видов птиц и животных. А если Вам хочется немного экстрима, в Сормовском парке имеются аттракционы, которые очень понравятся людям, которые хотят немного развлечься.", reply_markup=markup)

    elif message.text == "🌳 Московский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌳 В Московском районе можем посоветовать Бурнаковский сквер. Маленький парк, где можно просто прогуляться, посидеть и полюбоваться цветочками. Приятный для прогулок вечером одному или компанией.", reply_markup=markup)

    elif message.text == "🌳 Канавинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌳 В Канавинском районе советуем посетить Парк культуры и отдыха имени 1 Мая — отличный парк для времяпрепровождения с семьей или друзьями. Здесь Вы найдете развлечения на любой вкус, можете прокатиться на аттракционах, можете посетить живой уголок и посмотреть и покормить животных, можете покрмить уточек на пруду. В парке есть парк Тарзания, можете лазить и играть несколько часов, напротив парка есть классная площадка, современная и детям есть чем там заняться.", reply_markup=markup)

    elif message.text == "🌳 Ленинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌳 В Ленинском районе можем посоветовать Парк Дубки. Очень уютный и оживленный парк, отличное место для прогулок вечером. Парк отличается от других своей искренней природой, особенно осенью. Имеются детские площадки и отдельно огороженная зона для спортивных занятий, в праздничные дни здесь проводятся мероприятия."
        "\n\n🌳 Парк имени Маяковского — очень хороший парк для посещения с детьми. Здесь имеется корт для игры в баскетбол и воллейбол, есть эстрадная площадка, где часто проходят различные мероприятия. Приятное место чтобы пройтись, взяв стаканчик кофе."
        "\n\n🌳 Сквер Техноткань — благоустроенный сквер, где можно отдохнуть с детьми, так как в будние дни зачастую здесь проводятся мероприятия для детей. Место, которое оставит после себя хорошие впечатления.", reply_markup=markup)

    elif message.text == "🌳 Автозаводский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🌳 В Автозаводском районе можем посоветовать Парк имени 777-летия Нижнего Новгорода, довольно хорошее место чтобы просто пройтись с маленькими детьми, но также имеются развлечения и для детей повзрослее: тир, батуты и другие. Парк находится на берегу пруда с утками и чайками. Можно прогуляться по берегу."
        "\n\n🌳 Парк Культбаза — отличное место для прогулок. После реконструкции здесь стало намного лучше и можно с удовольствием прогуляться. Для любителей спорта здесь есть теннисный корт."
        "\n\n🌳 Парк Славы — тихое и спокойное место, для любителей посидеть в своей удовольствие. В центре парка есть холм с мозаичной стеллой, внутри которого горит вечный огонь. Рядом имеется мемориал воинам-афганцам. Если пройти чуть дальше можно обнаружить лавочки и площадки для экстремальных катаний на коньках и BMX."
        "\n\n🌳 Автозаводский парк — великолпный парк, отлично подходит для семейных прогулок, имеются аттракционы для маленьких детишек, хорошие спортивные зоны для ребятишек постарше с хорошей  огороженной футбольной площадкой и рампами для езды на роликах, самокатах, велосипедах и скейтбордах. Рядом расположено озеро, где можно покормить уточек, совершить спортивную пробежку или просто пройтись. То самое место, где можно отдохнуть душой, насладиться общением и природой.", reply_markup=markup)

    elif message.text == "🍽️ Кафе":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn41 = types.KeyboardButton("🍽️ Нижегородский")
        btn42 = types.KeyboardButton("🍽️ Советский")
        btn43 = types.KeyboardButton("🍽️ Приокский")
        btn44 = types.KeyboardButton("🍽️ Сормовский")
        btn45 = types.KeyboardButton("🍽️ Московский")
        btn46 = types.KeyboardButton("🍽️ Канавинский")
        btn47 = types.KeyboardButton("🍽️ Ленинский")
        btn48 = types.KeyboardButton("🍽️ Автозаводский")
        btn9 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn41, btn42, btn43, btn44, btn45, btn46, btn47, btn48, btn9)
        bot.send_message(message.from_user.id, "⬇ Выберите район Нижнего Новгорода, в котором Вы проживаете", reply_markup=markup)

    elif message.text == "🍽️ Нижегородский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🍽️ В Нижегородском районе советуем посетить ресторан «Джани ресторани», очень хорошее и атмосферное местечко. Готовят очень вкусно и подача блюд довольная интересная, например при заказе борща, его приносят в котелочке. Обязательно стоит попробовать большой хачапури. Есть детское меню. Повара и официанты работают отлично. Окружение сделано в стиле грузинского дворика - очень уютно."
        "\n\n🍽️ Ресторан Red Wall — отличное место чтобы вкусно поесть. Особенностью этого места является вид с веранды на реку и на Кремль. Средний чек выше, чем в многих других местах, но оно того стоит."
        "\n\n🍽️ Кафе Безухов — уютное кафе чтобы посидеть с друзьями, насладиться домашней едой и не только."
        "\n\n🍽️ Ресторан Пяткин — замечательный ресторан, с очень вкусной русской кухней и атмосферным интерьером."
        "\n\n🍽️ Для любителей быстрых перекусов в Нижегородском районе имеются КFC, БУРГЕР КИНГ и Вкусно — и точка.", reply_markup=markup)

    elif message.text == "🍽️ Советский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🍽️ В Советском районе советуем посетить ресторан «Ностальгия» — очень атмсферное место, изысканное меню, вкусно и красиво."
        "\n\n🍽️ Ресторан «Ле Гриль» — шикарное место, с виду неприметный ресторан, но внутри очень уютно и стильно. Вкусная еда, особенно стейки.", reply_markup=markup)

    elif message.text == "🍽️ Приокский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🍽️ В Приокском районе можем посоветовать посетить ресторан «Хачапурия», который нахоится в парке «Швейцария». После прогулки по парку, очень хорошее место чтобы отведать хинкали и хачапури."
        "\n\n🍽️ Кафе «Dark Side» — идеальное место для того, чтобы вкусно и не очень дорого поесть. Кафе сделано в стиле фильма «Star wars», так что фанаты оценят."
        "\n\n🍽️ Кафе «Самурай» — суши-бар. Отличное месточко, для любителей роллов."
        "\n\n🍽️ Кафе «Золотое кольцо» — хорошее место с красивым видом с веранды. Вкусная еда, огромный зал, вежливый персонал."
        "\n\n🍽️ Кафе «Принц» — отличное заведение с приятной атмосферой и приемлимыми ценами.", reply_markup=markup)

    elif message.text == "🍽️ Сормовский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🍽️ В Сормовском районе можем посоветовать ресторан «Смородина». Атмосферное место, интересный интерьер, приятная фоновая музыка и вкусная еда."
        "\n\n🍽️ Кафе «Dark Side» — идеальное место для того, чтобы вкусно и не очень дорого поесть. Кафе сделано в стиле фильма «Star wars», так что фанаты оценят."
        "\n\n🍽️ Пиццерия «Мир Пиццы» для любителей пицц. Вкусные пиццы и хорошая атмосфера."
        "\n\n🍽️ Кафе «Самурай» — суши-бар. Отличное месточко, для любителей роллов."
        "\n\n🍽️ Для любителей быстрых перекусов в Сормовском районе имеются КFC, БУРГЕР КИНГ и Вкусно — и точка.", reply_markup=markup)

    elif message.text == "🍽️ Московский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🍽️ В Московском районе советуем посетить ресторан «Salvadori Dali» - приятное место, вкусная кухня, уютная атмосфера."
        "\n\n🍽️ Кафе «Mexico» для любителей мексиканской кухни, приемлемые цены и хорошее обслуживание.", reply_markup=markup)

    elif message.text == "🍽️ Канавинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🍽️ В Канавинском районе советуем посетить ресторан «Plan_B» — ресторан с большим залом. Изысканная кухня, стильный интерьер, приятная и уютная атмосфера. Примечательно, что в ночное время суток рестон работает как ночной клуб, с отличной музыкой, хорошим фейсконтролем и баром."
        "\n\n🍽️ Ресторан «Хачапури тетушки Марико» — отличное место для встречи с друзьями. Хорошая кухня, чудесная атмосфера и приветливый персонал."
        "\n\n🍽️ Кафе «Самоварная» — шикарное место, сочетание цены-качества. Блюда высшего сорта, обслуживание на высшем уровне."
        "\n\n🍽️ Кафе «Dark Side» — идеальное место для того, чтобы вкусно и не очень дорого поесть. Кафе сделано в стиле фильма «Star wars», так что фанаты оценят."
        "\n\n🍽️ Для любителей быстрых перекусов в Канавинском районе имеются КFC, БУРГЕР КИНГ и Вкусно — и точка.", reply_markup=markup)

    elif message.text == "🍽️ Ленинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🍽️ В Ленинском районе советуем посетить кафе «Самоваръ» — хорошее уютное место чтобы плотно поесть."
        "\n\n🍽️ Ресторан «Хачапурия» — очень хорошее место чтобы отведать хинкали или хачапури."
        "\n\n🍽️ Кафе «Мимино» — уютное место для перекусов. Максимальное одомашненное кафе, дружелюбный персонал и вкусная кухня."
        "\n\n🍽️ Кафе «Шаурма по-турецки» — отличное место чтобы поесть вкусных донеров и почувствовать весь колорит и аутентичность турецкой кухни."
        "\n\n🍽️ Кафе «Dark Side» — идеальное место для того, чтобы вкусно и не очень дорого поесть. Кафе сделано в стиле фильма «Star wars», так что фанаты оценят."
        "\n\n🍽️ Для любителей быстрых перекусов в Ленинском районе имеются КFC, БУРГЕР КИНГ и Вкусно — и точка.", reply_markup=markup)

    elif message.text == "🍽️ Автозаводский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "🍽️ В Автозаводском районе советуем посетить ресторан «Домашняя Италия» — очень уютный ресторан с вкусной едой. Чудесный капучино вместе с тирамису и малино-шоколадное пирожное."
        "\n\n🍽️ Кафе «Чито Гврито» — отличное место чтобы сытно поесть. Соотношение цены-качества."
        "\n\n🍽️ Кафе «Kebab House» — для любителей хорошенько покушать. Чистое помещение и очень добрый персонал, а блюда на высшем уровне."
        "\n\n🍽️ Кафе «Dark Side» — идеальное место для того, чтобы вкусно и не очень дорого поесть. Кафе сделано в стиле фильма «Star wars», так что фанаты оценят."
        "\n\n🍽️ Для любителей быстрых перекусов в Автозаводском районе имеются КFC, БУРГЕР КИНГ и Вкусно — и точка.", reply_markup=markup)

    elif message.text == "🥂 Клубы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn61 = types.KeyboardButton("🥂 Нижегородский")
        btn62 = types.KeyboardButton("🥂 Советский")
        btn63 = types.KeyboardButton("🥂 Приокский")
        btn64 = types.KeyboardButton("🥂 Сормовский")
        btn65 = types.KeyboardButton("🥂 Московский")
        btn66 = types.KeyboardButton("🥂 Канавинский")
        btn67 = types.KeyboardButton("🥂 Ленинский")
        btn68 = types.KeyboardButton("🥂 Автозаводский")
        btn9 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn61, btn62, btn63, btn64, btn65, btn66, btn67, btn68, btn9)
        bot.send_message(message.from_user.id, "⬇ Выберите район Нижнего Новгорода, в котором Вы проживаете", reply_markup=markup)

    elif message.text == "🥂 Нижегородский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "В Нижегородском районе Вы можете посетить следущие клубы:\n\n🥂 Декольте: клуб с прекрасным персоналом и приятной атмосферой, тут Вы точно хорошо проведете время. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://бар-декольте.рф/)."
                                               "\n\n🥂 Burlesque: клуб с прекрасным персоналом и приятной атмосферой. С более подробной информацией можете ознакомиться перейдя по [ссылке](http://bur-52.ru/)."
                                               "\n\n🥂 ПМ-бар: здесь Вы прекрасно проведете свое время со своей команией. С более подробной информацией можете ознакомиться перейдя по [ссылке](https://pivomanbar.ru/)."
                                               "\n\n🥂 Zажигалка: прекрасное место с прекрасным персоналом! С более подробной информацией можете ознакомиться перейдя по [ссылке](https://russtriptease.com/nizhnii-novgorod/zazhigalka/).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🥂 Советский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Нижегородский")
        btn2 = types.KeyboardButton("🥂 Канавинский")
        btn3 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "🥂 В Советском районе, к сожалению, нет клубов, но Вы можете потусить в любом другом районе Нижнего Новгорода из предложенного ниже списка.", reply_markup=markup)

    elif message.text == "🥂 Приокский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Нижегородский")
        btn2 = types.KeyboardButton("🥂 Канавинский")
        btn3 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "🥂 В Приокском районе, к сожалению, нет клубов, но Вы можете потусить в любом другом районе Нижнего Новгорода из предложенного ниже списка.", reply_markup=markup)

    elif message.text == "🥂 Сормовский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Нижегородский")
        btn2 = types.KeyboardButton("🥂 Канавинский")
        btn3 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "🥂 В Сормовском районе, к сожалению, нет клубов, но Вы можете потусить в любом другом районе Нижнего Новгорода из предложенного ниже списка.",reply_markup=markup)

    elif message.text == "🥂 Московский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Нижегородский")
        btn2 = types.KeyboardButton("🥂 Канавинский")
        btn3 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "🥂 В Московском районе, к сожалению, нет клубов, но Вы можете потусить в любом другом районе Нижнего Новгорода из предложенного ниже списка.", reply_markup=markup)

    elif message.text == "🥂 Канавинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "В Канавинском районе Вы можете посетить следующие клубы:\n\n🥂 Sexofon Club: клуб с прекрасным персоналом и приятной атмосферой. С более подробной информаеий можете ознакомиться перейдя по [ссылке](https://vk.com/sexofon_nn).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
        
    elif message.text == "🥂 Ленинский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Нижегородский")
        btn2 = types.KeyboardButton("🥂 Канавинский")
        btn3 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "🥂 В Ленинском районе, к сожалению, нет клубов, но Вы можете потусить в любом другом районе Нижнего Новгорода из предложенного ниже списка.", reply_markup=markup)

    elif message.text == "🥂 Автозаводский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Нижегородский")
        btn2 = types.KeyboardButton("🥂 Канавинский")
        btn3 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "🥂 В Автозаводском районе, к сожалению, нет клубов, но Вы можете потусить в любом другом районе Нижнего Новгорода из предложенного ниже списка.", reply_markup=markup)

    # English language

    elif message.text == "🇬🇧 English":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍿 Cinema Parks")
        btn2 = types.KeyboardButton("🎭 Theatres")
        btn3 = types.KeyboardButton("🏛️ Museums")
        btn4 = types.KeyboardButton("🌳 City parks")
        btn5 = types.KeyboardButton("🍽️ Cafes")
        btn6 = types.KeyboardButton("🥂 Clubs")
        btn7 = types.KeyboardButton("🔙 Back to choosing of language")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "👀 Select the section you are interested in", reply_markup=markup)

    elif message.text == "🔙 Back to choosing of language":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton("🇬🇧 English")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == "🍿 Cinema Parks":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍿 Nijegorodsky district")
        btn2 = types.KeyboardButton("🍿 Sovetsky district")
        btn3 = types.KeyboardButton("🍿 Prioksky district")
        btn4 = types.KeyboardButton("🍿 Sormovsky district")
        btn5 = types.KeyboardButton("🍿 Moskovsky district")
        btn6 = types.KeyboardButton("🍿 Kanavinsky district")
        btn7 = types.KeyboardButton("🍿 Leninsky district")
        btn8 = types.KeyboardButton("🍿 Autozavodsky district")
        btn9 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "⬇ Choose the area of Nizhny Novgorod where you live",
                         reply_markup=markup)

    elif message.text == "🍿 Nijegorodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn221 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn221)
        bot.send_message(message.from_user.id,
                         "In the Nijegorodsky district, we recommend the following cinemas:\n\n🎬 Cinema Park in the Fantastika shopping mall: Cinema Park cinema in the Fantastika shopping and entertainment complex offers visitors 8 comfortable halls with a large number of seats. "
                        "Viewers will discover a huge selection of new movies, and new sessions start here every 15 minutes. Five halls out of eight are equipped with modern equipment for showing films in RealD 3D format, which has gained popularity among viewers of all ages. "
                         "For those who prefer to watch movies in a more private setting, there is a Relax hall designed for 34 spectators. You can get acquainted with the sessions held at [link](https://clck.ru/QgHkQ)."
                         "\n\n🎬 Empire of Dreams in the Sky shopping mall: a modern 8-hall multiplex Empire of Dreams in the Sky shopping mall on Lyadova Square, which includes 7 halls equipped with an ultra-modern 3D Master image system and a JBL speaker system. ATMOS Hall is equipped with innovative Dolby Atmos technology, which, according to experts, is becoming a new milestone in the development of cinemas. You can get acquainted with the sessions held at [link](https://clck.ru/36BNwo).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🍿 Sovetsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn331 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn331)
        bot.send_message(message.from_user.id,
                         "🎬 There are not so many good cinemas in the Sovetsky district, we advise you to visit Harlekino in the Zhar-Ptitsa shopping center: this is the first family cinema in Nizhny Novgorod. Seven cozy cinema halls, the latest cinema projection and sound equipment, "
                        "an active 3D image system, a convenient distance between the rows in the halls and upholstered chairs with lifting armrests with drink stands and always fragrant freshly prepared popcorn in the cinema bar – everything for a comfortable stay in this cinema. "
                        "You can get acquainted with the sessions held at [link](https://clck.ru/36BQ9K).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🍿 Prioksky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn441 = types.KeyboardButton("🍿 Nijegorodsky district")
        btn442 = types.KeyboardButton("🍿 Sovetsky district")
        btn443 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn441, btn442, btn443)
        bot.send_message(message.from_user.id, "🎬 Unfortunately, there are no cinemas in the Prioksky district. We recommend visiting cinemas in the nearby districts of Nizhny Novogod — Nijegorodsky and Sovetsky.", reply_markup=markup)

    elif message.text == "🍿 Sormovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn551 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn551)
        bot.send_message(message.from_user.id,
                         "🎬 In the Sormovsky district, we can recommend the Empire of Dreams cinema in the Golden Mile shopping mall: modern 5-room cinema. 5 cinemas with 798 seats are open for visitors to watch movies in 2D and 3D format, "
                         "for a pleasant wait there is a comfortable and spacious lobby, as well as children's slot machines., You can get acquainted with the sessions held at [link](https://clck.ru/36BQvh).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🍿 Moskovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn661 = types.KeyboardButton("🍿 Kanavinsky district")
        btn662 = types.KeyboardButton("🍿 Sormovsky district")
        btn663 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn661, btn662, btn663)
        bot.send_message(message.from_user.id,
                         "🎬 Unfortunately, there are no cinemas in the Moskovsky district. We recommend visiting cinemas in the nearby districts of Nizhny Novogod — Sormovsky and Kanavinsky.", reply_markup=markup)

    elif message.text == "🍿 Kanavinsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn771 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn771)
        bot.send_message(message.from_user.id,
                         "In the Nizhny Novgorod region, we recommend the following cinemas:\n\n🎬 Cinema Park in the Seventh Heaven shopping center: the cinema offers visitors 10 comfortable halls with a large number of seats.  "
                         "Multiplex Cinema Park combines all the currently relevant global film screening trends, including the IMAX and 4DX ™ Super Hall. In addition to the IMAX cinema hall, seven more cinemas are equipped with digital equipment for showing films in 3D format. "
                         "There are special high-comfort halls for watching the film in an informal setting. The RELAX lounge gives you the opportunity to enjoy watching movies in comfortable leather armchairs, relax in the premium bar. "
                         "The JOLLY hall is distinguished by an unusual design, cozy two- and four-seater sofas, as well as soft transformer chairs. The atmosphere of home warmth and comfort is suitable both for a large group of friends and for an unforgettable romantic evening of a couple in love. "
                         "You can get acquainted with the sessions held at [link](https://clck.ru/36BRX6 ).\n\n🎬 Cinema in the Rio shopping center: The five-hall multiplex CINEMA meets the highest international standards of film screening. The digital quality of the Dolby Digital Surround EX format allows you to enjoy the most subtle shades of sound when watching a movie. You can get acquainted with the sessions held at [link](https://clck.ru/36BRd5).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🍿 Leninsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn881 = types.KeyboardButton("🍿 Autozavodsky district")
        btn882 = types.KeyboardButton("🍿 Kanavinsky district")
        btn883 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn881, btn882, btn883)
        bot.send_message(message.from_user.id,"🎬 Unfortunately, there are no cinemas in Leninsky district. We recommend visiting cinemas in the nearby districts of Nizhny Novogod — Avtozavodsky and Kanavinsky.", reply_markup=markup)

    elif message.text == "🍿 Autozavodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn991 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn991)
        bot.send_message(message.from_user.id,
                         "🎬 In the Avtozavodsky district, we can advise the cinema Imeria of Dreams Mir: the cinema is located in a building that is an architectural monument. All internal elements of historical value have been completely restored.  "
                         "The cinema has a cozy cafe, sushi bar, billiards and karaoke club. There are slot machines in the lobby of the first floor. Convenient transport interchange allows you to quickly get to the cinema by any type of transport. "
                         "Christie cinema projectors are installed in the Mir cinema to show digital 2D and 3D films. You can get acquainted with the sessions held at [link](https://clck.ru/36BSPa).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🔙 The main menu":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🍿 Cinema Parks")
        btn2 = types.KeyboardButton("🎭 Theatres")
        btn3 = types.KeyboardButton("🏛️ Museums")
        btn4 = types.KeyboardButton("🌳 City parks")
        btn5 = types.KeyboardButton("🍽️ Cafes")
        btn6 = types.KeyboardButton("🥂 Clubs")
        btn7 = types.KeyboardButton("🔙 Back to choosing of language ")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "👀 Select the section you are interested in", reply_markup=markup)


    elif message.text == "🎭 Theatres":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn111 = types.KeyboardButton("🎭 Nijegorodsky district")
        btn112 = types.KeyboardButton("🎭 Sovetsky district")
        btn113 = types.KeyboardButton("🎭 Prioksky district")
        btn114 = types.KeyboardButton("🎭 Sormovsky district")
        btn115 = types.KeyboardButton("🎭 Moskovsky district")
        btn116 = types.KeyboardButton("🎭 Kanavinsky district")
        btn117 = types.KeyboardButton("🎭 Leninsky district")
        btn118 = types.KeyboardButton("🎭 Autozavodsky district")
        btn9 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn111, btn112, btn113, btn114, btn115, btn116, btn117, btn118, btn9)
        bot.send_message(message.from_user.id, "⬇ Choose the district of Nizhny Novgorod where you live", reply_markup=markup)

    elif message.text == "🎭 Nijegorodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "Most of the theaters of the city are located in the historical part of the city — in the Nizhny Novgorod district, here we recommend visiting the following theaters:\n\n 🎭 Nizhny Novgorod State Academic Drama Theater named after M. Gorky: the oldest theater in Nizhny Novgorod, whose history began more than 200 years ago. "
                         "Today, the theater has received worldwide recognition, and the classical repertoire is constantly being updated with bright premieres of modern works. You can get acquainted with the poster at [link](https://clck.ru/LGizT )."
                         "\n\n 🎭 Nizhny Novgorod Actor's House named after V.V. Vikhrov: a creative platform where performances, master classes and theatrical experiments are held. An acting studio has recently opened here. "
                         "You can get acquainted with the poster at [link](https://clck.ru/36BTDS ).\n\n 🎭 Nizhny Novgorod State Academic Opera and Ballet Theater named after A.S. Pushkin: the oldest theater in Nizhny Novgorod was founded in 1931. "
                         "The repertoire is based on classical works, and not only the most popular performances, but also those that have begun to be forgotten. The level of professionalism of directors and actors does not leave any viewer indifferent, "
                         "therefore, the theater is considered one of the best in Nizhny Novgorod. You can get acquainted with the poster at [link](https://clck.ru/34YHLu ).\n\n 🎭 Nizhny Novgorod State Academic Puppet Theater: Nizhny Novgorod Puppet Theater is the best place for a children's holiday. "
                         "Located in a historic building from 1912. Over the rich history of the theater, more than 320 performances have been staged, and the repertoire is constantly being updated. You can get acquainted with the poster at [link](https://clck.ru/36BTUC )."
                         "\n\n 🎭 Theater of the young spectator: created at the beginning of the XX century, the theater focuses on staging performances for children, but there are modern productions for adults in the repertoire. TYUZ was founded in 1928 by a famous actor "
                         "and directed by N. Sobolshchikov-Samarin, has a convenient location in the city center. You can get acquainted with the poster at [link](https://clck.ru/36BTZn ).\n\n 🎭 Nizhny Novgorod Comedy Theater: the theater was founded in the post-war period as a mini-theater Sniper, "
                         "but over time it became the leading theater stage with productions in the comedy genre. The theater employs talented directors, winners of numerous awards. They love Comedy for the variety of repertoire and stunning interior. "
                         "The repertoire of the theater is multifaceted and includes folk comedies, musical comics, tragi-farces, phantasmagoria and comedy-parables. The performances take place on several stages.You can get acquainted with the poster at [link](https://clck.ru/36BTjs).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🎭 Sovetsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎭 Nijegorodsky district")
        btn2 = types.KeyboardButton("🎭 Sormovsky district")
        btn3 = types.KeyboardButton("🎭 Kanavinsky district")
        btn4 = types.KeyboardButton("🎭 Leninsky district")
        btn5 = types.KeyboardButton("🎭 Autozavodsky district")
        btn6 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id,
                         "🎭 There are no theaters in the Sovetsky district. But you can always visit the theater in the nearby Nizhny Novgorod district or in any other part of the city, we are sure that you will definitely you find something suitable for yourself there😉",
                         reply_markup=markup)

    elif message.text == "🎭 Prioksky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎭 Nijegorodsky district")
        btn2 = types.KeyboardButton("🎭 Sormovsky district")
        btn3 = types.KeyboardButton("🎭 Kanavinsky district")
        btn4 = types.KeyboardButton("🎭 Leninsky district")
        btn5 = types.KeyboardButton("🎭 Autozavodsky district")
        btn6 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id,
                         "🎭 There are no theaters in the Prioksky district. But you can always visit the theater in the nearby Nizhny Novgorod district or in any other part of the city, we are sure that you will definitely find something suitable for yourself😉",
                         reply_markup=markup)

    elif message.text == "🎭 Sormovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🎭 In the Sormovsky district, we can recommend the Nizhny Novgorod Chamber Music Theater named after V. Stepanov: the creator of the musical theater is Vladimir Stepanov, formerly a leading soloist of opera and ballet in Russia and abroad. "
                         "The repertoire of the theater is classical ballets and musicals. You can get acquainted with the poster at [link](https://clck.ru/36BUND).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🎭 Moskovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🎭 Nijegorodsky district")
        btn2 = types.KeyboardButton("🎭 Sormovsky district")
        btn3 = types.KeyboardButton("🎭 Kanavinsky district")
        btn4 = types.KeyboardButton("🎭 Leninsky district")
        btn5 = types.KeyboardButton("🎭 Autozavodsky district")
        btn6 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id,
                         "🎭 There are no theaters in the Moscow district. But you can always visit the theater in the nearby areas — Sormovsky and Kanavinsky or in any other part of the city.",
                         reply_markup=markup)

    elif message.text == "🎭 Kanavinsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "In the Kanavinsky district , we can recommend the following theaters to visit:\n\n 🎭 Theater of the new generation Through the Looking Glass: a unique theater in which adult artists and children play. In the repertoire of the theater there are performances both "
                         " for the youngest viewers (from 2 years old) and schoolchildren, and serious productions for adults. You can get acquainted with the poster at [link](http://clck.ru/b78cq ).\n\n 🎭 Vera Theater: the theater offers a diverse repertoire "
                         "for young viewers. Originated from an ordinary studio under the direction of Vera Gorshkova in 1976, the theater is currently mobile, puts on performances throughout the Nizhny Novgorod. You can get acquainted with the poster at [link](https://clck.ru/36BV5v).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🎭 Leninsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🎭 In the Leninsky district, we can advise you to visit the Theater of musical and plastic drama Transfiguration: the theater appeared at the end of the XX century and is engaged in the professional development of the musical and plastic genre. The repertoire includes phantasmagoria, dramas, comedies, original performances, children's classics and concerts. "
                         "You can get acquainted with the poster at [link](https://clck.ru/36BVHS).", reply_markup=markup,
                         parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🎭 Autozavodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🎭 In the Avtozavodsky district, we can advise you to visit the Nizhny Novgorod Independent Theater on Happy Street: everything you need for your leisure is prepared here, and it is also possible to get useful skills here. Nizhny Novgorod Independent Theater on Happy Street will assist you in achieving your goals. "
                         "You can get acquainted with the poster at [link](https://clck.ru/36BVXg).", reply_markup=markup,
                         parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Museums":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton("🏛️ Nijegorodsky district")
        btn12 = types.KeyboardButton("🏛️ Sovetsky district")
        btn13 = types.KeyboardButton("🏛️ Prioksky district")
        btn14 = types.KeyboardButton("🏛️ Sormovsky district")
        btn15 = types.KeyboardButton("🏛️ Moskovsky district")
        btn16 = types.KeyboardButton("🏛️ Kanavinsky district")
        btn17 = types.KeyboardButton("🏛️ Leninsky district")
        btn18 = types.KeyboardButton("🏛️ Autozavodsky district")
        btn9 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn9)
        bot.send_message(message.from_user.id, "⬇ Choose the district of Nizhny Novgorod where you live",
                         reply_markup=markup)

    elif message.text == "🏛️ Nijegorodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "In the Nijegorodsky district, we can offer you to go to the following museums:\n\n🏛️ Nizhny Novgorod State Art Museum: here you will see historical paintings and you can also visit the VR helmet and view the paintings up close and you can visit their website by clicking on [link](https://artmuseumnn.ru/)."
                         "\n\n🏛️ Museum-branch of the Nizhny Novgorod Kremlin: here you can look at a lot of equipment of our vast country, and you can also look at the great walls of the Nizhny Novgorod Kremlin, which conceals a centuries-old history within its walls. You can read more by clicking on [link](https://ngiamz.ru/nizhegorodskiy-kreml)."
                         "\n\n🏛️ Technical Museum: here you can see the inventions of the past centuries, which are no longer used in everyday life. More detailed information can be found by clicking on [link](https://ngiamz.ru/tekhnicheskiy-muzey)."
                         "\n\n🏛️ Museum of Living Paper: here you can see many different figures created only with ordinary paper. You can get a closer look at the works by clicking on [link](https://vk.com/muzeyzhivoybumagi)."
                         "\n\n🏛️ Toy Museum: here you can see a lot of toys of the last century and visually compare what toys children had before, rather than what they have now. More detailed information can be found by clicking on [link](https://ngiamz.ru/igrushechnyy-muzey)."
                         "\n\n🏛️ Museum of Technology and Defense Industry: here you can see and touch the wonky equipment of our great power! More detailed information can be found by clicking on [link](https://park-pobeda-nn.ru/).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Sovetsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🏛️ In the Sovetsky district, we can offer you to go to the Zoological Museum: here you can see many models of various animals and immerse yourself in the world of animals. More detailed information can be found by clicking on [link](https://museum.unn.ru/).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Prioksky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🏛️ In the Prioksky district, we can offer you to go to the A.D. Sakharov Museum: here you can get acquainted with the life of a Soviet theoretical physicist, academician of the USSR Academy of Sciences, public figure, dissident and human rights activist. More detailed information can be found by clicking on [link](https://vk.com/sakharovmuseum).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Sormovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🏛️ In Sormovsky district we can offer you to visit the museum Back to the USSR: here you can experience the atmosphere of the USSR. More detailed information can be found by clicking on [link](https://ссср-музей.com/).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)


    elif message.text == "🏛️ Moskovsky district":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🏛️ Nijegorodsky district")
        btn2 = types.KeyboardButton("🏛️ Sovetsky district")
        btn3 = types.KeyboardButton("🏛️ Kanavinsky district")
        btn4 = types.KeyboardButton("🏛️ Leninsky district")
        btn5 = types.KeyboardButton("🏛️ Autozavodsky district")
        btn6 = types.KeyboardButton("🏛️ Sormovsky district")
        btn7 = types.KeyboardButton("🏛️ Prioksky district")
        btn8 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id,
                         "🏛️ Unfortunately, there are no museums in the Moskovsky district, but you can visit a museum in any other district of Nizhny Novgorod.",
                         reply_markup=markup)

    elif message.text == "🏛️ Kanavinsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🏛️ In the Kanavinsky district, we can offer you to go to Quarks: here you can get to know science and its interesting facts better. More detailed information can be found by clicking on [link](https://kvarky.ru/).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Leninsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🏛️ In the Leninsky district, we can offer you to go to the Museum of the History of the MPVO-GO-RSChS: here you can look at old and also still used firearms. More detailed information can be found by clicking on [link](https://вдпо.рф/museum/169).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🏛️ Autozavodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "In Avtozavodsky district we can offer you to go to the following museum:\n\n🏛️ GAZ History Museum: here you can look at the old, but quite famous machines created earlier by our civil engineers who put their soul into creating these legendary machines. More detailed information can be found by clicking on [link](http://museum.vaz.ru/)."
                         "\n\n🏛️ Nizhny Novgorod Metro Museum: here you can find out how the GREAT Metro of Nizhny Novgorod was built and is being built. More detailed information can be found by clicking on [link](http://metronn.ru/museum/).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🌳 City parks":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn21 = types.KeyboardButton("🌳 Nijegorodsky district")
        btn22 = types.KeyboardButton("🌳 Sovetsky district")
        btn23 = types.KeyboardButton("🌳 Prioksky district")
        btn24 = types.KeyboardButton("🌳 Sormovsky district")
        btn25 = types.KeyboardButton("🌳 Moskovsky district")
        btn26 = types.KeyboardButton("🌳 Kanavinsky district")
        btn27 = types.KeyboardButton("🌳 Leninsky district")
        btn28 = types.KeyboardButton("🌳 Autozavodsky district")
        btn9 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn9)
        bot.send_message(message.from_user.id, "⬇ Choose the district of Nizhny Novgorod where you live",
                         reply_markup=markup)

    elif message.text == "🌳 Nijegorodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🌳 In the Nizhny Novgorod district, we can advise you to take a walk in the Alexander Garden Park, where you can also walk along the well-known Chkalov Stairs and, of course, see the monument named after V.P. Chkalov. The park is located next to the Volga River, so you can admire the beautiful view."
                         "\n\n🌳 The park of the 800th anniversary of Nizhny Novgorod, a place suitable for walking with children, in company, couples in love and just alone. Insanely beautiful place, we advise you to visit it at sunset. There are playgrounds for children, sports grounds for adults and quiet places where you can retire and enjoy the beauty of the city.",
                         reply_markup=markup)

    elif message.text == "🌳 Sovetsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🌳 In the Sovetsky district, we recommend visiting the Shchelokovsky farm. This is a great place for walks and picnics. There are dirt bike paths that turn into a ski track in winter. There are 3 lakes in the park where you can watch ducks and even feed them, which children really like. Of the minuses, only the lack of Parking for personal transport.",
                         reply_markup=markup)

    elif message.text == "🌳 Prioksky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🌳 In the Prioksky district, we can advise you to visit the Switzerland Park. A very pleasant park, you can feel yourself in the forest, there are various types of entertainment for children of any age, there is a special obstacle course for older children. Magnificent view of the Oka River from the slope. If you get hungry, there are cafes with ice cream and coffee, as well as large ones like Khachapuri or Samurai. Of the minuses, only parking is available, there are definitely fewer places for cars than those who want to park next to the park.",
                         reply_markup=markup)

    elif message.text == "🌳 Sormovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🌳 In Sormovsky district, we recommend visiting Sormovsky Park: a great place to spend time with family or friends. The park is located in the green zone of the city, which creates an atmosphere for rest and relaxation. There are several playgrounds for children. There is also a pond with birds and a zoo in the park, you can see many different species of birds and animals. And if you want a little extreme, there are attractions in Sormovsky Park that people who want to have a little fun will really like.",
                         reply_markup=markup)

    elif message.text == "🌳 Moskovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🌳 In the Moscow district, we can advise Burnakovsky Square. A small park where you can just walk, sit and admire the flowers. Pleasant for walking in the evening alone or in company.",
                         reply_markup=markup)

    elif message.text == "🌳 Kanavinsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🌳 In the Kanavinsky district, we recommend visiting the Park of Culture and Recreation named after May 1 — an excellent park for spending time with family or friends. Here you will find entertainment for every taste, you can ride the rides, you can visit the living area and watch and feed the animals, you can feed the ducks on the pond. There is a Tarzania park in the park, you can climb and play for several hours, there is a cool playground opposite the park, modern and children have something to do there.",
                         reply_markup=markup)

    elif message.text == "🌳 Leninsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🌳 In the Leninsky district, we can recommend the Dubki Park. A very cozy and lively park, a great place to walk in the evening. The park differs from others by its sincere nature, especially in autumn. There are playgrounds and a separate fenced area for sports activities, events are held here on holidays."                        
                         "\n\n🌳 Mayakovsky Park is a very good park to visit with children. There is a basketball and volleyball court, there is a variety ground where various events are often held. A nice place to walk around, taking a cup of coffee."
                         "\n\n🌳 Technotkan Square is a well-maintained square where you can relax with children, since on weekdays events for children are often held here. A place that will leave behind a good impression.",
                         reply_markup=markup)

    elif message.text == "🌳 Autozavodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🌳 In Avtozavodsky district we can advise the Park named after the 777th anniversary of Nizhny Novgorod, a pretty good place to just walk with young children, but there are also entertainment for older children: shooting range, trampolines and others. The park is located on the shore of a pond with ducks and seagulls. You can walk along the shore."
                         "\n\n🌳 Kultbaza Park is a great place for walking. After the reconstruction, it has become much better here and you can walk with pleasure. For sports lovers there is a tennis court."
                         "\n\n🌳 Glory Park is a quiet and peaceful place for those who like to sit in their pleasure. In the center of the park there is a hill with a mosaic stele, inside of which the eternal flame burns. There is a memorial to the Afghan soldiers nearby. If you go a little further, you can find benches and playgrounds for extreme skating and BMX."
                         "\n\n🌳 Avtozavodsky Park is a large-scale park, great for family walks, there are attractions for small children, good sports areas for older children with a good fenced football field and ramps for roller skating, scooters, bicycles and skateboards. There is a lake nearby where you can feed ducks, take a sports run or just walk. The very place where you can relax your soul, enjoy communication and nature.",
                         reply_markup=markup)

    elif message.text == "🍽️ Cafes":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn41 = types.KeyboardButton("🍽️ Nijegorodsky district")
        btn42 = types.KeyboardButton("🍽️ Sovetsky district")
        btn43 = types.KeyboardButton("🍽️ Prioksky district")
        btn44 = types.KeyboardButton("🍽️ Sormovsky district")
        btn45 = types.KeyboardButton("🍽️ Moskovsky district")
        btn46 = types.KeyboardButton("🍽️ Kanavinsky district")
        btn47 = types.KeyboardButton("🍽️ Leninsky district")
        btn48 = types.KeyboardButton("🍽️ Autozavodsky district")
        btn9 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn41, btn42, btn43, btn44, btn45, btn46, btn47, btn48, btn9)
        bot.send_message(message.from_user.id, "⬇ Choose the district of Nizhny Novgorod where you live",
                         reply_markup=markup)

    elif message.text == "🍽️ Nijegorodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🍽️ In the Nizhny Novgorod region, we recommend visiting the restaurant Jani restaurant, a very nice and atmospheric place. They cook very tasty and the serving of dishes is quite interesting, for example, when ordering borscht, it is brought in a pot. You should definitely try the big khachapuri. There is a children's menu. Cooks and waiters work perfectly. The surroundings are made in the style of a Georgian courtyard — very cozy."
                         "\n\n🍽️ The Red Wall Restaurant is a great place to eat delicious food. A special feature of this place is the view from the veranda of the river and the Kremlin. The average check is higher than in many other places, but it's worth it."
                         "\n\n🍽️ Cafe Bezukhov is a cozy cafe to sit with friends, enjoy homemade food and not only."
                         "\n\n🍽️ Pyatkin Restaurant is a wonderful restaurant with very tasty Russian cuisine and an atmospheric interior."
                         "\n\n🍽️ For lovers of quick snacks in the Nizhny Novgorod district there are KFC, BURGER KING and Delicious — and that's it.",
                         reply_markup=markup)

    elif message.text == "🍽️ Sovetsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🍽️ In the Sovetsky district, we recommend visiting the Nostalgia restaurant — a very atmospheric place, an exquisite menu, delicious and beautiful."
                         "\n\n🍽️ The restaurant Le Grill is a chic place, a seemingly inconspicuous restaurant, but inside it is very cozy and stylish. Delicious food, especially steaks.",
                         reply_markup=markup)

    elif message.text == "🍽️ Prioksky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🍽️ In the Prioksky district, we can advise you to visit the Khachapuria restaurant, which is located in the Switzerland Park. After a walk in the park, a very good place to taste khinkali and khachapuri."
                         "\n\n🍽️ Cafe Dark Side is an ideal place to eat delicious and not very expensive. The cafe is made in the style of the movie Star Wars, so fans will appreciate it."
                         "\n\n🍽️ Cafe Samurai — sushi bar. A great place for fans of rolls."
                         "\n\n🍽️ Cafe Golden Ring is a good place with a beautiful view from the veranda. Delicious food, a huge hall, polite staff."
                         "\n\n🍽️ Cafe Prince is a great place with a pleasant atmosphere and reasonable prices.",
                         reply_markup=markup)

    elif message.text == "🍽️ Sormovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🍽️ In the Sormovsky district, we can recommend the restaurant Currant. An atmospheric place, an interesting interior, pleasant background music and delicious food."
                         "\n\n🍽️ Cafe Dark Side is an ideal place to eat delicious and not very expensive. The cafe is made in the style of the movie Star Wars, so fans will appreciate it."
                         "\n\n🍽️ Pizzeria Pizza World for pizza lovers. Delicious pizzas and a good atmosphere."
                         "\n\n🍽️ Cafe Samurai — sushi bar. A great place for fans of rolls."
                         "\n\n🍽️ For lovers of quick snacks in the Sormovsky district there are KFC, BURGER KING and Delicious — and that's it.",
                         reply_markup=markup)

    elif message.text == "🍽️ Moskovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🍽️ In the Moskovsky district, we recommend visiting the Salvadori Dali restaurant - a pleasant place, delicious cuisine, cozy atmosphere."
                         "\n\n🍽️ Cafe Mexico for lovers of Mexican cuisine, reasonable prices and good service.",
                         reply_markup=markup)

    elif message.text == "🍽️ Kanavinsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🍽️ In the Kanavinsky district, we recommend visiting the Plan_B restaurant — a restaurant with a large hall. Exquisite cuisine, stylish interior, pleasant and cozy atmosphere. It is noteworthy that at night Reston works as a nightclub, with excellent music, good face control and a bar."
                         "\n\n🍽️ The restaurant Aunt Mariko's Khachapuri is a great place to meet friends. Good cuisine, wonderful atmosphere and friendly staff."
                         "\n\n🍽️ Cafe Samovarnaya is a chic place, a combination of price and quality. Top-class dishes, top-level service."
                         "\n\n🍽️ Cafe Dark Side is an ideal place to eat delicious and not very expensive. The cafe is made in the style of the movie Star Wars, so fans will appreciate it."
                         "\n\n🍽️ For lovers of quick snacks in the Kanavinsky district there are KFC, BURGER KING and Delicious — and that's it.",
                         reply_markup=markup)

    elif message.text == "🍽️ Leninsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🍽️ In the Leninsky district, we recommend visiting the cafe Samovar — a nice cozy place to eat a hearty meal."
                         "\n\n🍽️ Khachapuria Restaurant is a very good place to taste khinkali or khachapuri."
                         "\n\n🍽️ Mimino Cafe is a cozy place for snacks. Maximum domesticated cafe, friendly staff and delicious cuisine."
                         "\n\n🍽️ Cafe Shawarma in Turkish is a great place to eat delicious doners and feel all the flavor and authenticity of Turkish cuisine."
                         "\n\n🍽️ Cafe Dark Side is an ideal place to eat delicious and not very expensive. The cafe is made in the style of the movie Star Wars, so fans will appreciate it."
                         "\n\n🍽️ For lovers of quick snacks in the Leninsky district there are KFC, BURGER KING and Delicious — and that's it.",
                         reply_markup=markup)

    elif message.text == "🍽️ Autozavodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "🍽️ In Avtozavodsky district, we recommend visiting the restaurant Home Italy — a very cozy restaurant with delicious food. Wonderful cappuccino with tiramisu and raspberry-chocolate cake."
                         "\n\n🍽️ Cafe Chito Gwrito is a great place to have a hearty meal. Price-quality ratio."
                         "\n\n🍽️ Cafe Kebab House is for lovers of a good meal. Clean room and very kind staff, and the dishes are at the highest level."
                         "\n\n🍽️ Cafe Dark Side is an ideal place to eat delicious and not very expensive. The cafe is made in the style of the movie Star Wars, so fans will appreciate it."
                         "\n\n🍽️ For lovers of quick snacks in the Avtozavodsky district there are KFC, BURGER KING and Delicious — and that's it.",
                         reply_markup=markup)

    elif message.text == "🥂 Clubs":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn61 = types.KeyboardButton("🥂 Nijegorodsky district")
        btn62 = types.KeyboardButton("🥂 Sovetsky district")
        btn63 = types.KeyboardButton("🥂 Prioksky district")
        btn64 = types.KeyboardButton("🥂 Sormovsky district")
        btn65 = types.KeyboardButton("🥂 Moskovsky district")
        btn66 = types.KeyboardButton("🥂 Kanavinsky district")
        btn67 = types.KeyboardButton("🥂 Leninsky district")
        btn68 = types.KeyboardButton("🥂 Autozavodsky district")
        btn9 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn61, btn62, btn63, btn64, btn65, btn66, btn67, btn68, btn9)
        bot.send_message(message.from_user.id, "⬇ Choose the district of Nizhny Novgorod where you live",
                         reply_markup=markup)

    elif message.text == "🥂 Nijegorodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "In the Nizhny Novgorod district you can visit the following clubs:\n\n🥂 Cleavage: a club with excellent staff and a pleasant atmosphere, here you will definitely have a good time. More detailed information can be found by clicking on [link](https://бар-декольте.рф/)."
                         "\n\n🥂 Burlesque: a club with excellent staff and a pleasant atmosphere. More detailed information can be found by clicking on [link](http://bur-52.ru/)."
                         "\n\n🥂 PM-bar: here you will have a great time with your company. More detailed information can be found by clicking on [link](https://pivomanbar.ru/)."
                         "\n\n🥂 Zажигалка: a wonderful place with wonderful staff! More detailed information can be found by clicking on [link](https://russtriptease.com/nizhnii-novgorod/zazhigalka/).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🥂 Sovetsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Nijegorodsky district")
        btn2 = types.KeyboardButton("🥂 Kanavinsky district")
        btn3 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         "🥂 Unfortunately, there are no clubs in the Sovetsky district, but you can hang out in any other district of Nizhny Novgorod from the list below.",
                         reply_markup=markup)

    elif message.text == "🥂 Prioksky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Nijegorodsky district")
        btn2 = types.KeyboardButton("🥂 Kanavinsky district")
        btn3 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         "🥂 Unfortunately, there are no clubs in the Prioksky district, but you can hang out in any other district of Nizhny Novgorod from the list below.",
                         reply_markup=markup)

    elif message.text == "🥂 Sormovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Nijegorodsky district")
        btn2 = types.KeyboardButton("🥂 Kanavinsky district")
        btn3 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         "🥂 Unfortunately, there are no clubs in Sormovsky district, but you can hang out in any other district of Nizhny Novgorod from the list below.",
                         reply_markup=markup)

    elif message.text == "🥂 Moskovsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Nijegorodsky district")
        btn2 = types.KeyboardButton("🥂 Kanavinsky district")
        btn3 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         "🥂 Unfortunately, there are no clubs in the Moskovsky district, but you can hang out in any other district of Nizhny Novgorod from the list below.",
                         reply_markup=markup)

    elif message.text == "🥂 Kanavinsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "In Kanavinsky district you can visit the following clubs:\n\n🥂 Sexofon Club: a club with excellent staff and a pleasant atmosphere. More detailed information can be found by clicking on [link](https://vk.com/sexofon_nn).",
                         reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)

    elif message.text == "🥂 Leninsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Nijegorodsky district")
        btn2 = types.KeyboardButton("🥂 Kanavinsky district")
        btn3 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         "🥂 Unfortunately, there are no clubs in Leninsky district, but you can hang out in any other district of Nizhny Novgorod from the list below.",
                         reply_markup=markup)

    elif message.text == "🥂 Autozavodsky district":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🥂 Nijegorodsky district")
        btn2 = types.KeyboardButton("🥂 Kanavinsky district")
        btn3 = types.KeyboardButton("🔙 The main menu")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         "🥂 Unfortunately, there are no clubs in Avtozavodsky district, but you can hang out in any other district of Nizhny Novgorod from the list below.",
                         reply_markup=markup)

bot.polling(none_stop=True, interval=0)
