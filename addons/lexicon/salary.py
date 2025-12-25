class SalaryLexicon:
    EMPL_MSG: str = "Укажите кол-во сотрудников для кадрового учёта"
    EMPL_ERROR_MSG: str = "⚠️ <b>Ошибка:</b> введите корректное <b>числовое значение</b> количества сотрудников."
    EMPL_RESULT_MSG: str = "\n\n📄 <b>Количество сотрудников:</b> {empl}\n"

    WHITE_MSG: str = (
        "💰 <b>Будет ли производиться официальное начисление заработной платы?</b>"
    )
    WHITE_ERROR_MSG: str = "⚠️ <b>Ошибка:</b> пожалуйста, выберите <b>один из предложенных типов</b> выплат."

    YES_WHITE_BTN_TEXT: str = "🏢 Официально"
    NO_WHITE_BTN_TEXT: str = "👥 Неофициально"

    BACK_TO_EMPL_BTN_TEXT: str = "⬅️ К количеству сотрудников"

    BACK_TO_TYPE_BTN_TEXT: str = "⬅️ К типу выплаты зарплаты"

    ACCOUNTANT_TUP = (
        YES_WHITE_BTN_TEXT,
        NO_WHITE_BTN_TEXT,
    )

    RESULT_MSG: str = (
        "📊 <b> Расчёт кадрового учёта</b>\n\n"
        "<b>Указанные параметры:</b>\n"
        "📄 <b>Количество сотрудников:</b> {empl}\n"
        "💼 <b>Тип выплат:</b> {white}\n\n"
        "💰 <b> Итого:</b> {total}"
    )