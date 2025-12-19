import asyncio

from apscheduler.triggers.interval import IntervalTrigger

from config import TelegramConfig
from config import ApschedulerConfig

from module import routers

from data import update_extract
from data import update_without
from data import update_with
from data import update_accounting

from tools.logger import LoggerTools

BOT = TelegramConfig.BOT
DISPATCHER = TelegramConfig.DISPATCHER

SCHEDULER = ApschedulerConfig.scheduler

logger = LoggerTools.get_logger(name=__name__, info=True, error=True, critical=True)


async def main():
    SCHEDULER.add_job(
        func=update_extract,
        trigger=IntervalTrigger(seconds=5),
        id='update_extract',
        misfire_grace_time=60
    )

    SCHEDULER.add_job(
        func=update_with,
        trigger=IntervalTrigger(seconds=5),
        id='update_with',
        misfire_grace_time=60
    )

    SCHEDULER.add_job(
        func=update_without,
        trigger=IntervalTrigger(seconds=5),
        id='update_without',
        misfire_grace_time=60
    )

    SCHEDULER.add_job(
        func=update_accounting,
        trigger=IntervalTrigger(seconds=5),
        id='update_accounting',
        misfire_grace_time=60
    )

    try:
        print("COMPILING")

        SCHEDULER.start()

        print("SCHEDULER START")

        DISPATCHER.include_routers(*routers)

        logger.info("SESSION OPEN")
        print("SESSION OPEN")

        await DISPATCHER.start_polling(BOT, polling_timeout=30)
    except asyncio.CancelledError:
        logger.info("Polling cancelled")
    except Exception as ex:
        logger.critical(f"Unexpected error: {ex}", exc_info=True)
    finally:
        SCHEDULER.shutdown()

        print("SCHEDULER SHUTDOWN")

        logger.info("SESSION CLOSE")
        print("SESSION CLOSE")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("PROGRAM INTERRUPTED")
    except SystemExit:
        logger.info("SYSTEM EXIT")
    except Exception as e:
        logger.critical(f"EXTREMAL ERROR: {e}", exc_info=True)
