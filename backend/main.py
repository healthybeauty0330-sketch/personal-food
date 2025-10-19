#（↓ここから下の Python を丸ごと貼る。最後に行頭の PY を入れて確定）
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Literal

app = FastAPI(title="Personal Food API (15Q)")

class Option(BaseModel):
    key: str
    label: str
    tags: List[str]

class Question(BaseModel):
    id: int
    text: str
    type: Literal["single","multi"] = "single"
    options: List[Option]

QUESTIONS: List[Question] = [
    Question(id=1, text="現在の主な目標は？", options=[
        Option(key="diet",   label="ダイエット",            tags=["A","B"]),
        Option(key="beauty", label="美肌・エイジングケア",  tags=["C","A"]),
        Option(key="muscle", label="筋トレ・ボディメイク",  tags=["D","B"]),
        Option(key="gut",    label="腸活・健康維持",        tags=["A"]),
    ]),
    Question(id=2, text="体質で当てはまるもの（複数可）", type="multi", options=[
        Option(key="cold",   label="冷えやすい", tags=["B"]),
        Option(key="const",  label="便秘気味",   tags=["A"]),
        Option(key="tired",  label="疲れやすい", tags=["B","C"]),
        Option(key="skin",   label="肌荒れ",     tags=["C","A"]),
        Option(key="none",   label="特になし",   tags=[]),
    ]),
    Question(id=3, text="朝の目覚めは？", options=[
        Option(key="good",   label="スッキリ", tags=["B"]),
        Option(key="normal", label="まあまあ", tags=[]),
        Option(key="bad",    label="だるい",   tags=["A","B"]),
    ]),
    Question(id=4, text="食後の状態は？", options=[
        Option(key="sleepy", label="眠くなる", tags=["B"]),
        Option(key="bloat",  label="お腹が張る", tags=["A"]),
        Option(key="none",   label="変化なし", tags=[]),
    ]),
    Question(id=5, text="運動習慣は？", options=[
        Option(key="daily",  label="ほぼ毎日", tags=["D","B"]),
        Option(key="weekly", label="週1-2回",   tags=["B"]),
        Option(key="rare",   label="ほとんどしない", tags=["A","C"]),
    ]),
    Question(id=6, text="平日の食事に近いのは？", options=[
        Option(key="home",   label="自炊が多い", tags=["C","A"]),
        Option(key="out",    label="外食/コンビニが多い", tags=["B"]),
        Option(key="skip",   label="食事を抜きがち", tags=["B"]),
    ]),
    Question(id=7, text="味の好みは？", options=[
        Option(key="spicy",  label="スパイシー", tags=["B"]),
        Option(key="fresh",  label="さっぱり/フレッシュ", tags=["A","C"]),
        Option(key="sweet",  label="やや甘め", tags=["C"]),
    ]),
    Question(id=8, text="タンパク質の摂取意識は？", options=[
        Option(key="high",   label="高タンパクを意識", tags=["D"]),
        Option(key="mid",    label="ほどほど", tags=["B"]),
        Option(key="low",    label="あまり意識しない", tags=["A","C"]),
    ]),
    Question(id=9, text="発酵食品は？", options=[
        Option(key="often",  label="よく食べる", tags=["A"]),
        Option(key="some",   label="時々",       tags=["A"]),
        Option(key="rare",   label="ほとんど食べない", tags=[]),
    ]),
    Question(id=10, text="間食は？", options=[
        Option(key="nuts",   label="ナッツ/ヨーグルト", tags=["C","A"]),
        Option(key="sweets", label="甘いもの", tags=["C"]),
        Option(key="none",   label="ほとんどしない", tags=["B"]),
    ]),
    Question(id=11, text="辛さの耐性は？", options=[
        Option(key="ok",     label="辛いのOK", tags=["B"]),
        Option(key="weak",   label="苦手",     tags=["A","C"]),
    ]),
    Question(id=12, text="フルーツは？", options=[
        Option(key="often",  label="よく食べる", tags=["C"]),
        Option(key="some",   label="時々",       tags=["C"]),
        Option(key="rare",   label="ほとんど食べない", tags=[]),
    ]),
    Question(id=13, text="水分量は？", options=[
        Option(key="2l",     label="1.5〜2L以上", tags=["A","B"]),
        Option(key="1l",     label="1L前後",       tags=["A"]),
        Option(key="low",    label="かなり少ない", tags=["A","C"]),
    ]),
    Question(id=14, text="睡眠時間は？", options=[
        Option(key="good",   label="7h以上", tags=["B","C"]),
        Option(key="mid",    label="5-6h",  tags=["C"]),
        Option(key="low",    label="〜4h",  tags=["B","A"]),
    ]),
    Question(id=15, text="目標の優先度は？", options=[
        Option(key="detox",  label="整える/デトックス", tags=["A"]),
        Option(key="burn",   label="燃やす/代謝UP",     tags=["B"]),
        Option(key="glow",   label="美肌/抗酸化",       tags=["C"]),
        Option(key="power",  label="筋力UP/体づくり",   tags=["D"]),
    ]),
]

RECOMMEND: Dict[str, List[Dict]] = {
    "A": [
        {"id":"salad01","name":"発酵デトックスサラダ","type":"salad","price":980},
        {"id":"acai01","name":"抗酸化アサイーボウル","type":"acai","price":900},
        {"id":"salad02","name":"食物繊維たっぷりサラダ","type":"salad","price":1000},
    ],
    "B": [
        {"id":"curry01","name":"スパイスチキンカレー","type":"curry","price":1200},
        {"id":"curry02","name":"豆と野菜のキーマ","type":"curry","price":1100},
        {"id":"salad03","name":"高タンパクチキンサラダ","type":"salad","price":1080},
    ],
    "C": [
        {"id":"acai01","name":"抗酸化アサイーボウル","type":"acai","price":900},
        {"id":"salad04","name":"ビタミンリッチサラダ","type":"salad","price":1020},
        {"id":"smooth01","name":"美肌ベリースムージー","type":"smoothie","price":780},
    ],
    "D": [
        {"id":"curry03","name":"タンパク強化カレー","type":"curry","price":1250},
        {"id":"salad03","name":"高タンパクチキンサラダ","type":"salad","price":1080},
        {"id":"smooth02","name":"プロテインスムージー","type":"smoothie","price":820},
    ],
}

class Answer(BaseModel):
    qid: int
    value: str

class DiagnoseRequest(BaseModel):
    answers: List[Answer]

class DiagnoseResult(BaseModel):
    type: Literal["A","B","C","D"]
    score: Dict[str, int]
    recommend: List[Dict]

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/questions", response_model=List[Question])
def get_questions():
    return QUESTIONS

@app.post("/diagnose", response_model=DiagnoseResult)
def diagnose(req: DiagnoseRequest):
    score = {"A":0, "B":0, "C":0, "D":0}
    qmap: Dict[int, Dict[str, List[str]]] = {}
    for q in QUESTIONS:
        qmap[q.id] = {opt.key: opt.tags for opt in q.options}
    for a in req.answers:
        keys = [k.strip() for k in a.value.split(",")] if "," in a.value else [a.value]
        for k in keys:
            for t in qmap.get(a.qid, {}).get(k, []):
                if t in score:
                    score[t] += 1
    t = max(["A","B","C","D"], key=lambda x: (score[x], {"A":4,"B":3,"C":2,"D":1}[x]))
    return {"type": t, "score": score, "recommend": RECOMMEND[t]}

@app.get("/menus")
def menus():
    # 全タイプのメニューからID重複を排除して一覧化
    items: Dict[str, Dict] = {}
    for vs in RECOMMEND.values():
        for e in vs:
            items[e["id"]] = e
    return {"items": list(items.values())}

class OrderItem(BaseModel):
    id: str
    qty: int

class CreateOrderRequest(BaseModel):
    items: List[OrderItem]
    delivery_slot: str

@app.post("/orders")
def create_order(req: CreateOrderRequest):
    price_map = {}
    for vs in RECOMMEND.values():
        for e in vs:
            price_map[e["id"]] = e["price"]
    total = sum(price_map.get(it.id, 0) * it.qty for it in req.items)
    return {"status":"pending", "amount": total, "slot": req.delivery_slot}
