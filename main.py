
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/calculo")
async def calculo(toneladas: float = Query(..., description="Toneladas"),
                   ley: float = Query(..., description="Ley")):
    resultado = toneladas * ley * 50
    return {"resultado": resultado}
