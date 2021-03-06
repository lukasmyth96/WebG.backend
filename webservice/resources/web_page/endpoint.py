from fastapi import APIRouter

from models import WebPage
from services.web_capture.web_driver import WebDriver

router = APIRouter()


@router.get('/webPage', response_model=WebPage)
def get_web_page(url: str) -> WebPage:
    webdriver = WebDriver(use_virtual_display=True)
    web_page = webdriver.get_web_page(url)
    webdriver.close()
    return web_page
