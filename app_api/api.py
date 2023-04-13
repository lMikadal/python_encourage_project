from ninja import Router
from app_api.schemas import EncourageSchema
import datetime

router = Router()

# Data
data = [
    EncourageSchema(encourage="จงเรียนรู้ที่จะให้กำลังใจตัวเองบ้าง ในวันที่เหนื่อย ท้อ"),
    EncourageSchema(encourage="ช่วงนี้อาจจะเหนื่อยหน่อยนะ สู้ๆ นะตัวเอง"),
    EncourageSchema(encourage="คนเราเลือกที่จะเป็นได้เสมอ"),
    EncourageSchema(encourage="การมีเป้าหมายที่ชัดเจน คือ จุดเริ่มต้นในทุกๆ ความสำเร็จ"),
    EncourageSchema(encourage="จงบอกโลกให้รู้ในสิ่งที่คุณต้องการ แทนที่จะบอกในสิ่งที่คุณไม่ต้องการ"),
    EncourageSchema(encourage="ไม่ว่าปัญหาจะหนักแค่ไหน เดี่ยวมันก็ผ่านไป"),
    EncourageSchema(encourage="ท้องฟ้าสดใสเสมอ หากเรามองมันด้วยใจ"),
]

@router.get('/all', response=list[EncourageSchema])
def encourage_all(request):
    return data

@router.get('/{int:e_idx}', response=EncourageSchema)
def encourage_id(request, e_idx: int):
    if e_idx >= len(data):
        dtime = datetime.datetime.now()
        e_idx = int(dtime.strftime('%S')) % len(data)
    return data[e_idx]