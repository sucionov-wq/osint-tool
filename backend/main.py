from fastapi import FastAPI, UploadFile, File
from modules.username import check_username
from modules.email import check_email
from modules.domain import analyze_domain
from modules.geoint import extract_exif
import io

app = FastAPI()

@app.get("/")
def root():
    return {"status": "OSINT Tool Running"}

# USERNAME
@app.get("/username/{username}")
def username_lookup(username: str):
    return check_username(username)

# EMAIL
@app.get("/email/{email}")
def email_lookup(email: str):
    return check_email(email)

# DOMAIN
@app.get("/domain/{domain}")
def domain_lookup(domain: str):
    return analyze_domain(domain)

# GEOINT (EXIF)
@app.post("/geoint")
async def geoint(file: UploadFile = File(...)):
    contents = await file.read()
    return extract_exif(contents)
