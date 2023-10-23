import telebot;
bot = telebot.TeleBot('6457106032:AAG1Qjmt_RbS4d-bUea9RgBiywFOG2yR-Xs')
from telebot import types
@bot.message_handler(commands=['start'])
def start(message):

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помощник, который подскажет тебе, куда можно сходить в Нижнем Новгороде. Даю рекомендации по интересным местам и заведениям.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_massages(message):

    if message.text == "👋 Поздороваться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton("🇬🇧 English")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

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
        bot.send_message(message.from_user.id, "В Канавинском районе Вы можете посетить следующие клубы:\n\n🥂 Sexofon Club: клуб с прекрасным персоналом и приятной атмосферой. С более подробной информаеий можете ознакомиться перейдя по [ссылке](https://vk.com/sexofon_nn).\n\n🥂 Plan_B: актуальное место для тех, кто ценит стиль и качество во всех направлениях. Днем заведение работает как ресторан, а ночью клубом, причем является одним из лучших в Канавинском районе. С более подробной информаеий можете ознакомиться перейдя по [ссылке](https://planb-nn.ru/).", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)
        
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

bot.polling(none_stop=True, interval=0)
