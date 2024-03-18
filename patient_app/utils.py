def cleaning_latest_record(data):
    final_data = {}
    for k, v in data.items():
        for value in v.values():
            final_data[k] = value
    return final_data