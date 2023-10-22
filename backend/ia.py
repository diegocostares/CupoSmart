import numpy as np
import tensorflow as tf
import os
import joblib
import glob

save_loc_template = "../backend/models/model_{course}.keras"
save_loc_template_scalerx = "../backend/models/scaler_x_{course}.pkl"
save_loc_template_scalery = "../backend/models/scaler_y_{course}.pkl"


def load_data(course):
    inf_path = save_loc_template.format(course=course)

    scaler_x_path = save_loc_template_scalerx.format(course=course)
    scaler_y_path = save_loc_template_scalery.format(course=course)

    loaded_model = tf.keras.models.load_model(inf_path)

    scaler_x = joblib.load(scaler_x_path)
    scaler_y = joblib.load(scaler_y_path)

    return loaded_model, scaler_x, scaler_y


def load_and_predict(course, values_to_predict: list):
    loaded_model, scaler_x, scaler_y = load_data(course)

    values_to_predict_normalized = scaler_x.transform(np.array(values_to_predict).reshape(-1, 1))

    predictions_normalized = loaded_model.predict(values_to_predict_normalized)

    predictions = scaler_y.inverse_transform(predictions_normalized)

    predictions = [x[0] for x in predictions]

    return predictions


def calculate_score(course_scores, config):
    score = 0
    max_score1 = max([x[0] for x in course_scores.values()])
    max_score2 = max([x[1] for x in course_scores.values()])
    for idx, course in enumerate(config):
        if idx < 3:  # Primera toma
            score += course_scores[course][0] / max_score1
        else:  # El resto de las tomas
            score += course_scores[course][1] / max_score2
        # To-Do: Usar los reajustes

    return score


def find_best_order(course_scores, current_config=None):
    if current_config is None:
        current_config = []

    if len(course_scores.keys()) == len(current_config):
        sssscore = calculate_score(course_scores, current_config)
        # print(f"Reached max with score {sssscore} and config: {current_config}")
        return current_config, sssscore

    best_score = -9999
    best_config = current_config

    for course in course_scores.keys():
        if course in current_config:
            continue

        my_config = current_config.copy()
        my_config.append(course)
        new_config, new_score = find_best_order(course_scores, my_config)
        if new_score > best_score:
            best_config = new_config
            best_score = new_score

    return best_config, best_score


sections = {  # (1ra_vuelta, 2da_vuelta, 1er_reajuste, 2do_reajuste)
    '1': ((8 / 24), (8 / 24) + 5, (18.5 / 24) + 12, (8 / 24) + 14),
    '2': ((9.5 / 24) + 3, (9.5 / 24) + 5, (17 / 24) + 12, (8 / 24) + 14),
    '3': ((11 / 24) + 3, (11 / 24) + 5, (15.5 / 24) + 12, (9.5 / 24) + 14),
    '4': ((12.5 / 24) + 3, (12.5 / 24) + 5, (14 / 24) + 12, (9.5 / 24) + 14),
    '5': ((14 / 24) + 3, (14 / 24) + 5, (12.5 / 24) + 12, (11 / 24) + 14),  # 14:00
    '6': ((15.5 / 24) + 3, (15.5 / 24) + 5, (11 / 24) + 12, (11 / 24) + 14),
    '7': ((17 / 24) + 3, (17 / 24) + 5, (9.5 / 24) + 12, (12.5 / 24) + 14),
    '8': ((18.5 / 24) + 3, (18.5 / 24) + 5, (8 / 24) + 12, (12.5 / 24) + 14),
    '9': ((8 / 24) + 4, (8 / 24) + 6, (18.5 / 24) + 11, (14 / 24) + 14),
    '10': ((9.5 / 24) + 4, (9.5 / 24) + 6, (17 / 24) + 11, (14 / 24) + 14),
    '11': ((11 / 24) + 4, (11 / 24) + 6, (15.5 / 24) + 11, (15.5 / 24) + 14),
    '12': ((12.5 / 24) + 4, (12.5 / 24) + 6, (14 / 24) + 11, (15.5 / 24) + 14),
    '13': ((14 / 24) + 4, (14 / 24) + 6, (12.5 / 24) + 11, (17 / 24) + 14),
    '14': ((15.5 / 24) + 4, (15.5 / 24) + 6, (11 / 24) + 11, (17 / 24) + 14),
    '15': ((17 / 24) + 4, (17 / 24) + 6, (9.5 / 24) + 11, (18.5 / 24) + 14),
    '16': ((18.5 / 24) + 4, (18.5 / 24) + 6, (8 / 24) + 11, (18.5 / 24) + 14)
}


def get_best_order(courses, banner: int):
    for course in courses:
        save_loc = save_loc_template.format(course=course)

        if not os.path.exists(save_loc):
            raise ValueError(f"Course {course} doesn't exist in our database yet.")

    if banner < 1 or banner > 16:
        raise ValueError(f"Invalid section: {banner}")

    section = str(banner)
    time_data = sections[section]

    course_scores = {}

    for course in courses:
        predictions = load_and_predict(course, time_data)
        course_scores[course] = predictions

    return find_best_order(course_scores)


def get_all_available_courses():
    directory_path = '../backend/models/'  # Replace with the actual path to your "tmp" directory

    # Use glob to find files starting with "model_"
    file_list = glob.glob(f'{directory_path}/model_*')

    return [os.path.basename(file_path)[6:-6] for file_path in file_list]


# courses_to_predict = ['IIC2133', 'IBM2101', 'IBM2992', 'EYP1025', 'IMT2565', 'FIS1514']

# print(get_best_order(courses_to_predict, banner=2)[0])
