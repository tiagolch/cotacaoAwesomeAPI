from fastapi import FastAPI
from cotacao import main, gravar_em_arquivo

app = FastAPI()

@app.get("/cotacao/{moeda}")
def read_cotacao(moeda: str):
    gravar_em_arquivo(main(moeda))
    return main(moeda)

