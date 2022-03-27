from fastapi import FastAPI
import reconigzedIMA as anIma
from pydantic import BaseModel
import statistics
import json
class links (BaseModel):
    lks:list
app = FastAPI()


@app.post("/analizeImg")
async def root(lksw:links):
    lsResult= anIma.analizeregsiters(lksw.lks)
    avr = statistics.mean(lsResult)
    thisdict = {"predperimage": lsResult,"averageS":avr}
    jsonString = json.dumps(thisdict)
    return thisdict