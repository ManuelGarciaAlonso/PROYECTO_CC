from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

app = FastAPI()

class Service(BaseModel):
    name: str
    description: str
    price: float
    category: str

class Rating(BaseModel):
    service_name: str
    score: int
    review: Optional[str] = None

class ServiceMarketplace:
    def __init__(self):
        self.services = []
        self.ratings = []

    def add_service(self, service: Service):
        self.services.append(service)

    def search_service(self, name: str) -> Optional[Service]:
        for service in self.services:
            if service.name.lower() == name.lower():
                return service
        return None

    def add_rating(self, rating: Rating):
        self.ratings.append(rating)
        return rating

marketplace = ServiceMarketplace()

@app.on_event("startup")
def startup_event():
    logger.info("Logging is configured.")

@app.post("/services/", response_model=Service)
def add_service(service: Service):
    marketplace.add_service(service)
    logger.info(f"Service added: {service.name}")
    return service

@app.get("/services/{name}", response_model=Service)
def get_service(name: str):
    service = marketplace.search_service(name)
    if service:
        logger.info(f"Service found: {name}")
        return service
    logger.warning(f"Service not found: {name}")
    raise HTTPException(status_code=404, detail="Service not found")

@app.post("/ratings/", response_model=Rating)
def add_rating(rating: Rating):
    service = marketplace.search_service(rating.service_name)
    if not service:
        logger.warning(f"Service not found for rating: {rating.service_name}")
        raise HTTPException(status_code=404, detail="Service not found")
    marketplace.add_rating(rating)
    logger.info(f"Rating added for service: {rating.service_name}")
    return rating
