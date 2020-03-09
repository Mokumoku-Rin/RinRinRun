from fastapi import APIRouter, Depends
from schemas.today import TodayRequest, TodayResponse
from services.today import TodayService
from depends.auth import FirebaseToken


router = APIRouter()


@router.post("/", response_model=TodayResponse)
async def get_today_record(requset_model: TodayRequest,
                           fbToken: FirebaseToken = Depends()):
    uid = fbToken.uid
    date = requset_model.date
    response: TodayRequest = {
        "date": date,
        "datas": await TodayService.get_today_record(uid, date + '%')
    }
    # response: TodayRequest = TodayService.get_today_record(uid, date)
    return response
