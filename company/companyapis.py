from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def get_company_name():
    return {"company_name": "Example company"}


@router.get("/employees")
async def get_employees_numer():
    return {"employees" : 1241}
