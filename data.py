import pendulum

class TestData:
    SCOOTER_URL = "https://qa-scooter.praktikum-services.ru/"
    SCOOTER_URL_ORDER = "https://qa-scooter.praktikum-services.ru/order"
    DZEN_URL = "dzen.ru"

    tomorrow = pendulum.tomorrow('Europe/Moscow').format('DD.MM.YYYY') # завтра
    two_tomorrow = pendulum.now().add(days=2).format('DD.MM.YYYY') # через 2 дня
    # Данные для заказа самоката
    ORDER_DATA_SETS = [
        {
            "firstname": "Анна",
            "lastname": "Петрова",
            "address": "Юбилейная, 1",
            "metro_station": "Маяковская",
            "phone_number": "+79997654321",
            "delivery_date": tomorrow,
            "rental_period": "двое суток",
            "color": "grey",
            "comment": "Домофон не работает",
        },
        {
            "firstname": "Иван",
            "lastname": "Иванов",
            "address": "Москва, ул. Пушкина, д. Колотушкина",
            "metro_station": "Тропарёво",
            "phone_number": "+79991234567",
            "delivery_date": two_tomorrow,
            "rental_period": "сутки",
            "color": "black",
            "comment": "Позвоните за час до доставки",
        },
    ]

    # Данные для вопросов FAQ
    FAQ_DATA = [
        {
            "question_index": 0,
            "expected_answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        },
        {
            "question_index": 1,
            "expected_answer": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        },
        {
            "question_index": 2,
            "expected_answer": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        },
        {
            "question_index": 3,
            "expected_answer": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        },
        {
            "question_index": 4,
            "expected_answer": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        },
        {
            "question_index": 5,
            "expected_answer": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        },
        {
            "question_index": 6,
            "expected_answer": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        },
        {
            "question_index": 7,
            "expected_answer": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        }
    ]