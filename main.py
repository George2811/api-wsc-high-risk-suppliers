from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.entity import entity

tags_metadata = [
    {
        "name": "Entity",
        "description": "Recolectar las entidades en listas de alto riesgo",
    },
]

app = FastAPI(
    title = "Web Scraping The World Bank API",
    version = "1.0",
    summary = "Herramienta automatizada que realiza búsquedas en línea para identificar entidades en listas de alto riesgo, como sanciones internacionales, listas de vigilancia y otras bases de datos relevantes",
    openapi_tags = tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entity)