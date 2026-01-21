
# test_main.py
from fastapi.testclient import TestClient
from main import app  # Importa la aplicación FastAPI desde main.py

client = TestClient(app)

def test_calculo_endpoint():
    """
    Test para el endpoint /calculo con parámetros válidos.
    """
    response = client.get("/calculo?toneladas=100&ley=0.5")
    assert response.status_code == 200
    assert response.json() == {"resultado": 2500.0}

def test_calculo_endpoint_zero_toneladas():
    """
    Test para el endpoint /calculo con toneladas igual a cero.
    """
    response = client.get("/calculo?toneladas=0&ley=0.5")
    assert response.status_code == 200
    assert response.json() == {"resultado": 0.0}

def test_calculo_endpoint_zero_ley():
    """
    Test para el endpoint /calculo con ley igual a cero.
    """
    response = client.get("/calculo?toneladas=100&ley=0")
    assert response.status_code == 200
    assert response.json() == {"resultado": 0.0}

def test_calculo_endpoint_negative_toneladas():
    """
    Test para el endpoint /calculo con toneladas negativas.
    """
    response = client.get("/calculo?toneladas=-100&ley=0.5")
    assert response.status_code == 200
    assert response.json() == {"resultado": -2500.0}

def test_calculo_endpoint_negative_ley():
    """
    Test para el endpoint /calculo con ley negativa.
    """
    response = client.get("/calculo?toneladas=100&ley=-0.5")
    assert response.status_code == 200
    assert response.json() == {"resultado": -2500.0}

def test_calculo_endpoint_large_values():
    """
    Test para el endpoint /calculo con valores grandes.
    """
    response = client.get("/calculo?toneladas=1000000&ley=1.0")
    assert response.status_code == 200
    assert response.json() == {"resultado": 50000000.0}

def test_calculo_endpoint_decimal_values():
    """
    Test para el endpoint /calculo con valores decimales.
    """
    response = client.get("/calculo?toneladas=10.5&ley=0.25")
    assert response.status_code == 200
    assert response.json() == {"resultado": 131.25}


# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/calculo")
async def calculo(toneladas: float, ley: float):
    """
    Endpoint para calcular el resultado basado en toneladas y ley.
    """
    resultado = toneladas * ley * 50
    return {"resultado": resultado}
