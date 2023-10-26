from fastapi import APIRouter, HTTPException
from services.web_scraping import get_entities, createDriver
from schemas.key import Key
from validators.auth import authenticated
from pydantic import ValidationError


entity = APIRouter()

@entity.post("/firm/{name}", tags=["Entity"])
async def get_list(name: str, key: Key):
    try:
        key_value = key.key

        if not key_value:
            # Personaliza la respuesta cuando el campo key.key no está incluido en el JSON
            raise HTTPException(status_code=400, detail="PLEASE, ENTER A KEY")

        if not authenticated(key_value):
            raise HTTPException(status_code=401, detail="INCORRECT KEY VALUE")
        
        driver=createDriver()
        
        response = get_entities(name, driver)
        driver.quit()

        return response
    
    except ValidationError:
        raise HTTPException(status_code=422)
     
    except HTTPException as http_exception:
        return http_exception
        
    