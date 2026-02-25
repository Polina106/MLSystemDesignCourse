from fastapi import FastAPI
from app.planner import MealPlanner
from app.data_loader import load_recipes

app = FastAPI()

recipes_df = load_recipes("app/data/recipes.jsonl")

planner = MealPlanner(
    recipes_df=recipes_df,
    allergens=[
        'Белок коровьего молока', 'Злаки, содержащие глютен', 'Яйцо',
        'Рыба', 'Сельдерей', 'Соя', 'Пищевые добавки', 'Горчица',
        'Орехи', 'Клубника', 'Кунжут', 'Арахис', 'Ракообразные', 'Моллюски'
    ],
    cont_features=[
        'asian','european','eastern',
        'slavic','america','mexica'
    ],
    product_features=[
        'рыба','морепродукты','свинина','говядина','курица','сыр',
        'картофель','лук','чеснок','помидоры','печень','молоко','творог',
        'оливки','сельдерей','кинза','тыква','баклажан','орехи'
    ]
)

@app.post("/plan-day/")
def plan_day(user: dict):
    return planner.plan_day(user)
