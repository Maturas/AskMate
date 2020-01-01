import csv
import os.path


def load(filename, cls):
    data = []

    if os.path.exists(filename):
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = cls.from_dict(row)
                data.append(obj)

    return data


def save(filename, fieldnames, data):
    with open(filename, 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()

        for obj in data:
            fields = obj.to_dict()
            writer.writerow(fields)
