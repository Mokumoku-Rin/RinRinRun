import usecases.today


class TodayService:
    @staticmethod
    async def get_today_record(uid, date):
        return usecases.today.get_today_record(uid, date)
