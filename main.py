from typing import Union
from fastapi import FastAPI
from utils.database import execute_query_json
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Patri"}

@app.get("/studentss")
async def get_all_studentss():
    sqlscript ="""
            SELECT [id]
            ,[firstname]
            ,[lastname]
            ,[idperson]
            ,[email]
            ,[age]
        FROM [academics].[studentss]
       """
    result = await execute_query_json(sqlscript)
    print(type(result))
    
    results_dict = json.loads(result)  

    return results_dict

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}