import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from keras import layers, models

# Load Data
filename = 'cargo_ship_factors_with_delay.csv'
df = pd.read_csv(filename)

# Convert 'Start Date' and 'Contract Arrival Time' to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['Contract Arrival Time'] = pd.to_datetime(df['Contract Arrival Time'])

# Create new feature: difference in days between 'Start Date' and 'Contract Arrival Time'
df['Date Difference'] = (df['Contract Arrival Time'] - df['Start Date']).dt.total_seconds() / (24 * 60 * 60)

# Define preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), df.select_dtypes(include=['float64']).columns),
        ('cat', OneHotEncoder(drop='first'), ['Ship Routine', 'Ship type'])
    ])

early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',  # 监控验证集上的损失
    patience=10,  # 如果连续 10 个 epoch 验证损失没有改善，就停止训练
    restore_best_weights=True  # 恢复最佳权重
)

# Drop the datetime columns after creating the 'Date Difference' feature
X = df.drop(columns=['Start Date', 'Contract Arrival Time', 'Delay'])
X = preprocessor.fit_transform(X)
y = df['Delay']

# Convert Labels to one-hot encoding
y = tf.keras.utils.to_categorical(y)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(5, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the Model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.1,callbacks=[early_stopping])

# Example new_data, you will replace it with actual new data
new_data = pd.DataFrame({
    'Start Date': [pd.Timestamp('2023-10-01')],
    'Weather Conditions': [0.5],
    'Port Congestion': [0.6],
    'Navigational Issues': [0.7],
    'Mechanical Breakdowns': [0.2],
    'Maintenance and Repairs': [0.1],
    'Customs and Documentation': [0.4],
    'Labor Strikes': [0.3],
    'Piracy and Security Concerns': [0.5],
    'Traffic and Navigation Regulations': [0.7],
    'Fuel Availability and Costs': [0.2],
    'Cargo Handling': [0.4],
    'Trade Volume': [0.8],
    'Geopolitical Factors': [0.1],
    'Global Events': [0.6],
    'Seasonal Factors': [0.3],
    'Contract Arrival Time': [pd.Timestamp('2023-10-05')],
    'Ship Routine': ['b'],  # Add corresponding value
    'Ship type': ['y']  # Add corresponding value
})

new_data['Date Difference'] = (new_data['Contract Arrival Time'] - new_data['Start Date']).dt.total_seconds() / (24 * 60 * 60)
new_data.drop(columns=['Start Date', 'Contract Arrival Time'], inplace=True)
new_data_scaled = preprocessor.transform(new_data)
predictions = model.predict(new_data_scaled)
predictions_dict = {str(i): f"{predictions[0][i] * 100:.2f}%" for i in range(5)}
print(predictions_dict)