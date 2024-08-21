from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SetRequest(BaseModel):
    cards: List[str]

def is_valid_set(card1: str, card2: str, card3: str) -> bool:
    for i in range(4): 
        if not ((card1[i] == card2[i] == card3[i]) or 
                (card1[i] != card2[i] and card1[i] != card3[i] and card2[i] != card3[i])):
            return False
    return True

def find_combinations(cards: List[str]) -> List[List[str]]:
    valid_sets = []
    n = len(cards)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if is_valid_set(cards[i], cards[j], cards[k]):
                    valid_sets.append([cards[i], cards[j], cards[k]])
                    
    return valid_sets

@app.post("/find_sets/")
def find_sets(set_request: SetRequest):
    valid_sets = find_combinations(set_request.cards)
    return {"valid_sets": valid_sets}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
