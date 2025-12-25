class AccountantLexicon:
    RESULT_MSG: str = (
        "📊 <b> Расчёт стоимости бухгалтерского сопровождения</b>\n\n"
        "<b>Указанные параметры:</b>\n"
    )

    TOTAL_MSG: str = "💰 <b> Итого:</b> {total}"

    BACK_TO_RES_BTN_TEXT: str = "⬅️ Вернуться к бух. сопровождению"

    DOCS_COUNTER_MSG: str = (
        "📄 <b>Укажите количество документов</b> "
        "для расчёта (от <b>200</b> до <b>2000</b>).\n\n"
    )
    DOCS_ERROR_MSG: str = (
        "⚠️ <b>Ошибка:</b> введите корректное "
        "<b>числовое значение</b> количества документов "
        "в диапазоне от <b>200</b> до <b>2000</b>."
    )
    DOCS_RESULT_MSG: str = "📄 <b>Количество документов:</b> {docs}\n"

    TYPE_MSG: str = "💼 <b>Выберите тип налогообложения</b> для расчёта стоимости.\n\n"
    TYPE_ERROR_MSG: str = "⚠️ <b>Ошибка:</b> пожалуйста, выберите <b>один из предложенных типов</b> налогообложения."
    TYPE_RESULT_MSG: str = "💼 <b>Тип налогообложения:</b> {type}\n"

    # ACCOUNTANT_MSG: str = "👤 <b>Требуются ли услуги главного бухгалтера?</b>\n\n"
    # ACCOUNTANT_ERROR_MSG: str = "⚠️ <b>Ошибка:</b> пожалуйста, укажите, <b>нужны ли вам услуги главного бухгалтера</b>."
    # ACCOUNTANT_RESULT_MSG: str = "👤 <b>Услуги главного бухгалтера:</b> {accountant}\n"

    EXTRACT_COUNTER_MSG: str = "🧾 <b>Укажите количество банковских выписок</b>.\n\n"
    EXTRACT_ERROR_MSG: str = "⚠️ <b>Ошибка:</b> пожалуйста, выберите <b>один из предложенных вариантов</b> количества выписок."
    EXTRACT_RESULT_MSG: str = "🧾 <b>Количество выписок:</b> {extract}\n\n"

    YES_ACCOUNTANT_BTN_TEXT: str = "✅ Да"
    NO_ACCOUNTANT_BTN_TEXT: str = "❌ Нет"

    ACCOUNTANT_TUP = (
        YES_ACCOUNTANT_BTN_TEXT,
        NO_ACCOUNTANT_BTN_TEXT,
    )

    BACK_TO_DOCS_BTN_TEXT: str = "⬅️ К количеству документов"

    BACK_TO_TYPE_BTN_TEXT: str = "⬅️ К типу налогообложения"

    BACK_TO_ACCOUNTANT_BTN_TEXT: str = "⬅️ К выбору главного бухгалтера"

    BACK_TO_EXTRACT_COUNTER_BTN_TEXT: str = "⬅️ К количеству выписок"

