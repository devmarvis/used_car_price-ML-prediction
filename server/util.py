import joblib
import json
import numpy as np


__model = None
__columns_dict = None
__numerical_features = None
__min_car_year = None

def load_saved_artifacts():
    print("Loading saved artifacts...Start")

    global __model, __columns_dict, __numerical_features, __min_car_year

    if __model is None:
        try:
            with open("./artifacts/predictor.pkl", "rb") as f:
                __model = joblib.load(f)
        except:
            print("Couldn't load model")

    with open("./artifacts/columns_dict.json", "r") as f:
        __columns_dict = json.load(f)

    with open("./artifacts/numerical_features.json", "r") as f:
        __numerical_features = json.load(f)

    with open("./artifacts/minimum_car_year.json", "r") as f:
        __min_car_year = json.load(f)

    print("Loading saved artifacts...Done")


def data_processor(user_inputs):
    processed_inputs = __columns_dict

    for col, val in user_inputs.items():
        if col in __numerical_features:
            if col == "Driven_kms":
                processed_inputs["Driven_kms_log"] = np.log1p(int(val) * 1000)
            elif col == "Year":
                processed_inputs[col] = int(val) - __min_car_year["min_car_year"]
            else:
                processed_inputs[col] = float(val)
        else:
            processed_inputs[col + "_" + val] = 1

    return processed_inputs


def predict_price(car_details):
    X_features = np.array(list(car_details.values())).reshape(1, -1)
    price = __model.predict(X_features)

    return {
        "price": round(price[0], 2)
    }


if __name__ == "__main__":
    load_saved_artifacts()
