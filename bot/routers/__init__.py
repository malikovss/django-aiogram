from aiogram import Router

from .test import router as test_router

router = Router()
router.include_router(test_router)
