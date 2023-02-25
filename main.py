#main.py
from supabase import create_client, Client
from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# def root():
#     return {"message": "Hello World Test"}


url ="https://ojrbirzktvctdfiwrota.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9qcmJpcnprdHZjdGRmaXdyb3RhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY3Njc4Mzk0MCwiZXhwIjoxOTkyMzU5OTQwfQ.2QC-jb4RICVuZtvVFgleJmPXXJs-tBfrm979L888PaA"

supabase: Client = create_client(url, key)
@app.get("/ipl")
def themes():
    themes = supabase.table('iplmatches').select('*').execute()
    return themes