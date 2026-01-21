
# test_main.py
from fastapi.testclient import TestClient
from main import app  # Importa la aplicación FastAPI desde main.py

client = TestClient(app)


def test_calculo_endpoint():
    """
    Test para el endpoint /calculo con parámetros válidos.
    """
    toneladas = 10.0
    ley = 2.5
    response = client.get(f"/calculo?toneladas={toneladas}&ley={ley}")
    assert response.status_code == 200
    data = response.json()
    assert "resultado" in data
    assert data["resultado"] == toneladas * ley * 50


def test_calculo_endpoint_zero_toneladas():
    """
    Test para el endpoint /calculo con toneladas igual a cero.
    """
    toneladas = 0.0
    ley = 2.5
    response = client.get(f"/calculo?toneladas={toneladas}&ley={ley}")
    assert response.status_code == 200
    data = response.json()
    assert "resultado" in data
    assert data["resultado"] == 0.0


def test_calculo_endpoint_zero_ley():
    """
    Test para el endpoint /calculo con ley igual a cero.
    """
    toneladas = 10.0
    ley = 0.0
    response = client.get(f"/calculo?toneladas={toneladas}&ley={ley}")
    assert response.status_code == 200
    data = response.json()
    assert "resultado" in data
    assert data["resultado"] == 0.0


def test_calculo_endpoint_negative_toneladas():
    """
    Test para el endpoint /calculo con toneladas negativas.
    """
    toneladas = -10.0
    ley = 2.5
    response = client.get(f"/calculo?toneladas={toneladas}&ley={ley}")
    assert response.status_code == 200
    data = response.json()
    assert "resultado" in data
    assert data["resultado"] == toneladas * ley * 50


def test_calculo_endpoint_negative_ley():
    """
    Test para el endpoint /calculo con ley negativa.
    """
    toneladas = 10.0
    ley = -2.5
    response = client.get(f"/calculo?toneladas={toneladas}&ley={ley}")
    assert response.status_code == 200
    data = response.json()
    assert "resultado" in data
    assert data["resultado"] == toneladas * ley * 50


def test_calculo_endpoint_missing_toneladas():
    """
    Test para el endpoint /calculo sin el parámetro toneladas.
    """
    ley = 2.5
    response = client.get(f"/calculo?ley={ley}")
    assert response.status_code == 422  # Unprocessable Entity


def test_calculo_endpoint_missing_ley():
    """
    Test para el endpoint /calculo sin el parámetro ley.
    """
    toneladas = 10.0
    response = client.get(f"/calculo?toneladas={toneladas}")
    assert response.status_code == 422  # Unprocessable Entity


def test_calculo_endpoint_invalid_toneladas():
    """
    Test para el endpoint /calculo con un valor inválido para toneladas.
    """
    ley = 2.5
    response = client.get(f"/calculo?toneladas=abc&ley={ley}")
    assert response.status_code == 422  # Unprocessable Entity


def test_calculo_endpoint_invalid_ley():
    """
    Test para el endpoint /calculo con un valor inválido para ley.
    """
    toneladas = 10.0
    response = client.get(f"/calculo?toneladas={toneladas}&ley=abc")
    assert response.status_code == 422  # Unprocessable Entity


# main.py
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()


@app.get("/calculo")
async def calculo(toneladas: float = Query(..., description="Cantidad de toneladas"),
                  ley: float = Query(..., description="Ley del material")):
    """
    Calcula el resultado basado en las toneladas y la ley.
    """
    resultado = toneladas * ley * 50
    return {"resultado": resultado}
