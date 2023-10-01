from datetime import datetime, timedelta
import pandas as pd
import random


def data_generate():
    num_data_points = 10000
    data = pd.DataFrame(columns=[
        'Start Date',
        'Weather Conditions',
        'Port Congestion',
        'Navigational Issues',
        'Mechanical Breakdowns',
        'Maintenance and Repairs',
        'Customs and Documentation',
        'Labor Strikes',
        'Piracy and Security Concerns',
        'Traffic and Navigation Regulations',
        'Fuel Availability and Costs',
        'Cargo Handling',
        'Trade Volume',
        'Geopolitical Factors',
        'Global Events',
        'Seasonal Factors',
        'Contract Arrival Time',
        'Ship Routine',  # New column
        'Ship type',  # New column
        'Delay'
    ])

    ship_routines = ['a', 'b', 'c']
    ship_types = ['x', 'y', 'z']

    for _ in range(num_data_points):
        year = 2023
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        start_date = datetime(year, month, day)

        contract_days = random.randint(5, 28)
        contract_arrival_time = start_date + timedelta(days=contract_days)

        delay = random.randint(0, 4)  # Delay in days. It can be negative, zero, or positive.
        actual_arrival_time = contract_arrival_time + timedelta(days=delay)

        ship_routine = random.choice(ship_routines)  # Randomly select ship routine
        ship_type = random.choice(ship_types)  # Randomly select ship type

        row = {
            'Start Date': start_date.strftime('%Y-%m-%d'),
            'Weather Conditions': random.uniform(0, 1),
            'Port Congestion': random.uniform(0, 1),
            'Navigational Issues': random.uniform(0, 1),
            'Mechanical Breakdowns': random.uniform(0, 1),
            'Maintenance and Repairs': random.uniform(0, 1),
            'Customs and Documentation': random.uniform(0, 1),
            'Labor Strikes': random.uniform(0, 1),
            'Piracy and Security Concerns': random.uniform(0, 1),
            'Traffic and Navigation Regulations': random.uniform(0, 1),
            'Fuel Availability and Costs': random.uniform(0, 1),
            'Cargo Handling': random.uniform(0, 1),
            'Trade Volume': random.uniform(0, 1),
            'Geopolitical Factors': random.uniform(0, 1),
            'Global Events': random.uniform(0, 1),
            'Seasonal Factors': random.uniform(0, 1),
            'Contract Arrival Time': contract_arrival_time.strftime('%Y-%m-%d'),
            'Ship Routine': ship_routine,  # Add ship routine to row
            'Ship type': ship_type,  # Add ship type to row
            'Delay': delay
        }

        data = pd.concat([data, pd.DataFrame(row, index=[0])], ignore_index=True)

    data.to_csv('cargo_ship_factors_with_delay.csv', index=False)


if __name__ == '__main__':
    data_generate()