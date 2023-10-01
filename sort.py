import json
from datetime import datetime, timedelta


def sort_shipper(data, sort_std, exact_date):
    exact_date = datetime.strptime(exact_date, "%Y/%m/%d")

    # 把deadline放进去
    for shipper in data:
        shipper['deadline'] = exact_date + timedelta(days=shipper["handle_time_with_shipper_delay"]-1)

    # 使用sort_std来sort
    sorted_data = sorted(data, key=lambda x: tuple(x[k] for k in sorted(sort_std, key=sort_std.get)))
    return sorted_data


with open('example_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

sort_std = {"goods_priority": 1, "contract_value": 2, "deadline": 3}
exact_date = "2023/10/14"

sorted_shippers = sort_shipper(data, sort_std, exact_date)

print(sorted_shippers)