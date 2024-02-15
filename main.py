# import os
# from PyPDF2 import PdfReader
from secrets import token_hex
import psycopg2
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name='static')

templates = Jinja2Templates(directory="templates")

db_name = "test"
db_user = "postgres"
db_pass = "Dhameliya8548"
db_host = "localhost"
db_port = "5432"
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_pass,
    host=db_host,
    port=db_port
)


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')


async def create_upload_files(file: UploadFile = File(...)):
    file_ext = file.filename.split(".").pop()
    file_name = token_hex(10)

    file_path = f"reports/{file_name}.{file_ext}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return file_path


# using PyPDF2 library
# @app.post("/getData/")
# async def get_data(file: UploadFile = File(...)):
#     file_path = await create_upload_files(file)
#     try:
#         with open(file_path, "rb") as f:
#             reader = PdfReader(f)
#             result = []
#             page = 0
#             total_pages = len(reader.pages)
#
#             while page != total_pages:
#                 selected_page = reader.pages[page]
#                 text = selected_page.extract_text()
#                 text = text.split('\n')
#                 result.append(page)
#                 result.append(text)
#                 page += 1
#     finally:
#         os.remove(file_path)
#
#     return result
