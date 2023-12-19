from bboard.models import Bb


single_record = Bb(list_field = "Some text to be written~")
single_record.save()

data_to_insert = ["Запись 1", "Запись 2", "Запись 3"]
for item in data_to_insert:
    record = Bb(list_field = item)
    record.save()