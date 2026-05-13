# [1] 라우터 : 특정 도메인(주소)한 묶어주는 역할
from fastapi import APIRouter

# APIRouter( prefix='/공통도메인')
# vs @RequestMapping("/공통도메인")
router = APIRouter( prefix="/api")

# [3] 서비스 불러오기
# private final BoardServivce boardService;
from service import item_service

# [2] REST API 정의
# (1) GET
@router.get("/item")
async def item(id : int):
    return item_service.item(id)

# (2) GET 
@router.get("/items")
async def items():
    return item_service.items()

# (3) POST
# {"id":3, "name":"제로콜라", "price":2000}
@router.post("/save")
async def save( item: dict ): # 파이썬은 (변수 : 타입명) 순서
    return item_service.save( item )

# (4) PUT
@router.put("/update")
async def update(item: dict):
    return item_service.update(item)

# (5) DELETE
@router.delete("/delete")
async def delete( id: int):
    return item_service.delete( id )