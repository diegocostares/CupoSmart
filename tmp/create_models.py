import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import datetime
from sklearn.preprocessing import StandardScaler
import os

quota_path = "../backend/data/quota.csv"

df = pd.read_csv(quota_path)

df['date'] = pd.to_datetime(df['date'], format="ISO8601")

courses_list = df['initials'].unique().tolist()
print(f"Amount of total courses: {len(courses_list)}.")
print(f"Sample: {courses_list[:5]}")

date_ranges = [
    ('2021-1', '2021-01-22', '2021-01-30'),
    ('2021-2', '2021-08-02', '2021-08-13'),
    ('2021-3', '2021-12-28', '2021-12-28'),
    ('2022-1', '2022-01-06', '2022-01-18'),
    ('2022-2', '2022-07-25', '2022-08-05'),
    ('2022-3', '2022-12-20', '2022-12-20'),
    ('2023-1', '2023-01-05', '2023-01-17'),
    ('2023-2', '2023-07-21', '2023-08-04')
]

dfs_dict = {}

# Iterate through the date ranges and extract the corresponding data
for name, start_date, end_date in date_ranges:
    mask = (df['date'] >= start_date) & (df['date'] <= end_date) & (df['category'] == 'Vacantes libres')
    dfs_dict[name] = df[mask].copy()

min_timesteps = 15

courses_timesteps = {}

for df_name, df_val in dfs_dict.items():
    print(f"Working on inscription period {df_name} (", end="")

    grouped = df_val.groupby("section_id")
    filtered_df = grouped.filter(lambda group: len(group) > min_timesteps)
    print(f"{filtered_df['section_id'].nunique()} elements after filter)")

    for initials, group in filtered_df.groupby(['initials', 'section_id']):
        initials, section_id = initials
        date_quota_list = list(zip(group['date'], group['quota']))

        # Check if the 'initials' key already exists in the dictionary
        if initials not in courses_timesteps:
            courses_timesteps[initials] = {section_id: date_quota_list}
        else:
            # Check if the 'section_id' key already exists for the 'initials'
            if section_id not in courses_timesteps[initials]:
                courses_timesteps[initials][section_id] = date_quota_list
            else:
                courses_timesteps[initials][section_id].extend(date_quota_list)

courses_timesteps['ACO256E'][19123][0]

for course in list(courses_timesteps.keys()):
    for nrc in list(courses_timesteps[course].keys()):
        if sum([x for _, x in courses_timesteps[course][nrc]]) == 0:
            del courses_timesteps[course][nrc]
            continue

        base_timestamp = pd.Timestamp(courses_timesteps[course][nrc][0][0].date())

        for ts_id in range(len(courses_timesteps[course][nrc])):
            courses_timesteps[course][nrc][ts_id] = (
            (courses_timesteps[course][nrc][ts_id][0].replace(tzinfo=None) - base_timestamp).to_pytimedelta(),
            courses_timesteps[course][nrc][ts_id][1])

type(courses_timesteps['ACO256E'][19123][0][0])

flat_courses = {}

for course, course_data in list(courses_timesteps.items()):
    for nrc, timestamp_value in course_data.items():
        if course in flat_courses:
            flat_courses[course].extend(list(timestamp_value))
        else:
            flat_courses[course] = list(timestamp_value)


def build_model(x_values_normalized, y_values_normalized):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(7, activation='relu', input_shape=(1,)))
    model.add(tf.keras.layers.Dense(7, activation='relu'))
    model.add(tf.keras.layers.Dense(1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Define EarlyStopping callback
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='loss',  # Monitor validation loss
        patience=20,  # Number of epochs with no improvement after which training will be stopped
        restore_best_weights=True  # Restore model weights from the epoch with the best value of the monitored quantity
    )

    # Train the model with early stopping
    history = model.fit(
        x_values_normalized, y_values_normalized,
        epochs=1000,
        callbacks=[early_stopping],  # Pass the EarlyStopping callback
        verbose=0
    )

    return model, history

save_loc_template = "../backend/models/model_{course}.keras"

print(save_loc_template.format(course="test"))

# data = flat_courses['ACO256E']

for idx, (course_name, data) in enumerate(list(flat_courses.items())):

    print(f"Training {course_name}. ({idx+1}/{len(flat_courses.keys())})", end="")

    course_name_parsed = course_name.strip()

    save_loc = save_loc_template.format(course=course_name_parsed)

    print(save_loc)

    if os.path.exists(save_loc):
        print(" Already trained, skipping...")
        continue

    print("")

    x_values = [x.total_seconds() / 86400.0 for x, y in data]  # Convert timedelta to days (86400 seconds per day)
    y_values = [y for x, y in data]

    x_values = np.array(x_values)
    y_values = np.array(y_values)

    # Normalize x and y
    scaler_x = StandardScaler()
    scaler_y = StandardScaler()

    x_values_normalized = scaler_x.fit_transform(x_values.reshape(-1, 1))
    y_values_normalized = scaler_y.fit_transform(y_values.reshape(-1, 1))

    # Create a single plot for all combinations

    model, hist = build_model(x_values_normalized, y_values_normalized)

    if hist.history['loss'][-1] > 0.1:
        print(f"Loss too big {course_name}: {hist.history['loss'][-1]}")
        continue

    # Inverse transform the normalized predictions to get the actual predictions in the original scale
    # predictions = scaler_y.inverse_transform(predictions_normalized)

    model.save(save_loc)

    # Plot the predictions for the current combination with a different color
    # plt.plot(x_new, predictions, label=f'Neurons: (1x7x7x1)')

    # plt.scatter(x_values, y_values, label='Data Points', color='black', marker='o')
    # plt.xlabel('Time (days)')
    # plt.ylabel('Y Values')
    # plt.legend()
    # plt.grid(True)
    # plt.show()