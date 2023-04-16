from ninja import Router
from app_api.schemas import EncourageSchema, ErrorSchema
from app_api.models import Encourage
import datetime

router = Router()

# tmp Data
# data = [
#     EncourageSchema(encourage="จงเรียนรู้ที่จะให้กำลังใจตัวเองบ้าง ในวันที่เหนื่อย ท้อ"),
#     EncourageSchema(encourage="ช่วงนี้อาจจะเหนื่อยหน่อยนะ สู้ๆ นะตัวเอง"),
#     EncourageSchema(encourage="คนเราเลือกที่จะเป็นได้เสมอ"),
#     EncourageSchema(encourage="การมีเป้าหมายที่ชัดเจน คือ จุดเริ่มต้นในทุกๆ ความสำเร็จ"),
#     EncourageSchema(encourage="จงบอกโลกให้รู้ในสิ่งที่คุณต้องการ แทนที่จะบอกในสิ่งที่คุณไม่ต้องการ"),
#     EncourageSchema(encourage="ไม่ว่าปัญหาจะหนักแค่ไหน เดี่ยวมันก็ผ่านไป"),
#     EncourageSchema(encourage="ท้องฟ้าสดใสเสมอ หากเรามองมันด้วยใจ"),
# ]

@router.get('/', response=list[EncourageSchema])
def all_encourage(request):
    return Encourage.objects.all()

@router.get('/{int:idx}', response=EncourageSchema)
def get_encourage(request, idx: int):
    data = Encourage.objects.all()
    if idx >= len(data):
        dtime = datetime.datetime.now()
        idx = int(dtime.strftime('%S')) % len(data)
    return {"encourage": Encourage.objects.get(id=(idx + 1)).title}

@router.post('/')
def add_encourage(request, payload: EncourageSchema):
    Encourage.objects.create(title=payload.encourage)

@router.put('/{int:idx}', response={200: EncourageSchema, 404: ErrorSchema})
def update_encourage(request, idx: int, payload: EncourageSchema):
    try:
        data = Encourage.objects.get(pk=idx)
        setattr(data, 'title', payload.encourage)
    except:
        return 404, {"error": "Not Found"}
    data.save()
    return 200, {"encourage": payload.encourage}

@router.delete('/{int:idx}', response={200: EncourageSchema, 404: ErrorSchema})
def delete_encourage(request, idx: int):
    try:
        data = Encourage.objects.get(pk=idx)
    except:
        return 404, {"error": "Not Found"}
    data.delete()
    return 200, {"encourage": "Deleted"}