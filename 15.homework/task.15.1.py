import logging

logging.basicConfig(filename="pytest_info.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class Rhombus:
    def __init__(self, сторона_а, кут_а):
        logger.info("Початок виконання програми")
        self.__setattr__('сторона_а', сторона_а)
        self.__setattr__('кут_а', кут_а)
        logger.info("Ромб успішно створено: сторона_а=%s, кут_а=%s, кут_б=%s", self.сторона_а, self.кут_а, self.кут_б)
        logger.info("Завершення виконання програми")

    def __setattr__(self, name, value):
        if name == 'сторона_а':
            if value <= 0:
                logger.error("Помилка: довжина сторони повинна бути більше 0.")
                raise ValueError("Довжина сторони повинна бути більше 0.")
            object.__setattr__(self, name, value)

        elif name == 'кут_а':
            if not (0 < value < 180):
                logger.error("Помилка: кут_а має бути в діапазоні (0, 180).")
                raise ValueError("Кут_а має бути в діапазоні (0, 180).")
            object.__setattr__(self, 'кут_а', value)
            computed_kut_b = 180 - value
            object.__setattr__(self, 'кут_б', computed_kut_b)
            logger.info(f"Користувач ввів кут_а={value}, тому кут_б автоматично змінився на {computed_kut_b}.")

        elif name == 'кут_б':
            logger.error("Помилка: кут_б не можна змінювати безпосередньо.")
            raise AttributeError(
                "Кут_б не можна змінювати безпосередньо. Він визначається автоматично на основі кут_а.")

        else:
            object.__setattr__(self, name, value)

    def __str__(self):
        return f"Ромб: сторона_а={self.сторона_а}, кут_а={self.кут_а}, кут_б={self.кут_б}"


if __name__ == "__main__":
    try:
        romb = Rhombus(10, 30)
        print(romb)

        romb.кут_а = 60
        print(romb)

    except ValueError as e:
        logger.error("Помилка при створенні ромба: %s", e)
    except AttributeError as e:
        logger.error("Помилка при зміні атрибуту ромба: %s", e)