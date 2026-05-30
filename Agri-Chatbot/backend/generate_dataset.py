import csv
import os
import random

os.makedirs("../data", exist_ok=True)

crops = [
    "rice", "wheat", "maize", "cotton", "sugarcane",
    "tomato", "potato", "groundnut", "millet", "banana"
]

soil_types = ["clay soil", "loamy soil", "sandy soil", "black soil", "red soil"]

fertilizers = {
    "rice": "Nitrogen-rich fertilizers such as urea and NPK",
    "wheat": "NPK and nitrogen fertilizers",
    "maize": "Nitrogen and phosphorus fertilizers",
    "cotton": "Balanced NPK fertilizer with micronutrients",
    "sugarcane": "Nitrogen-rich fertilizer and compost",
    "tomato": "Potassium-rich fertilizer with compost",
    "potato": "NPK fertilizer with organic manure",
    "groundnut": "Gypsum and phosphorus-based fertilizer",
    "millet": "Organic manure and balanced NPK",
    "banana": "Potassium-rich fertilizer and organic compost"
}

irrigation_methods = {
    "rice": "Flood irrigation or controlled irrigation",
    "wheat": "Sprinkler or furrow irrigation",
    "maize": "Drip or furrow irrigation",
    "cotton": "Drip irrigation",
    "sugarcane": "Furrow irrigation",
    "tomato": "Drip irrigation",
    "potato": "Sprinkler irrigation",
    "groundnut": "Light furrow irrigation",
    "millet": "Minimal irrigation depending on rainfall",
    "banana": "Drip irrigation"
}

pest_controls = {
    "rice": "Use resistant varieties, neem oil spray, and proper field sanitation",
    "wheat": "Monitor rust and aphids, use fungicides and bio-pesticides",
    "maize": "Control stem borer using biological agents and crop rotation",
    "cotton": "Use neem-based pesticide and integrated pest management for aphids and bollworms",
    "sugarcane": "Field sanitation and pest monitoring for borers",
    "tomato": "Neem oil spray and sticky traps for whiteflies and aphids",
    "potato": "Use fungicides for blight and maintain field hygiene",
    "groundnut": "Seed treatment and pest monitoring",
    "millet": "Crop rotation and bio-pesticides",
    "banana": "Remove infected leaves and use bio-control measures"
}

harvest_times = {
    "rice": "120 to 150 days",
    "wheat": "110 to 140 days",
    "maize": "90 to 120 days",
    "cotton": "150 to 180 days",
    "sugarcane": "10 to 18 months",
    "tomato": "60 to 90 days",
    "potato": "90 to 120 days",
    "groundnut": "100 to 130 days",
    "millet": "75 to 100 days",
    "banana": "9 to 12 months"
}

questions_templates = [
    "Which fertilizer is best for {crop}?",
    "How should I irrigate {crop}?",
    "What pest control is recommended for {crop}?",
    "What is the harvest time of {crop}?",
    "Which crop grows well in {soil}?",
    "How to prepare soil for {crop}?",
    "What are the seasonal tips for {crop} farming?",
    "How to improve yield in {crop} cultivation?",
    "What is the best soil type for {crop}?",
    "How to manage diseases in {crop}?"
]

def build_answer(crop, soil):
    return (
        f"For {crop}, suitable soil includes {soil}. "
        f"Recommended fertilizer: {fertilizers[crop]}. "
        f"Irrigation method: {irrigation_methods[crop]}. "
        f"Pest control: {pest_controls[crop]}. "
        f"Expected harvest time: {harvest_times[crop]}."
    )

dataset_path = "../data/agriculture_dataset.csv"

with open(dataset_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "crop_name", "soil_type", "fertilizer_recommendation",
        "irrigation_method", "pest_control_methods", "harvest_time",
        "question", "answer"
    ])

    count = 0
    while count < 500:
        crop = random.choice(crops)
        soil = random.choice(soil_types)
        question = random.choice(questions_templates).format(crop=crop, soil=soil)
        answer = build_answer(crop, soil)

        writer.writerow([
            crop,
            soil,
            fertilizers[crop],
            irrigation_methods[crop],
            pest_controls[crop],
            harvest_times[crop],
            question,
            answer
        ])
        count += 1

print(f"Dataset created successfully at {dataset_path}")