def chek_time(d):
    jadval = []
    previous_end_time = '00:00'

    for start_time, end_time in d:
        jadval.append((previous_end_time, start_time))
        previous_end_time = end_time

    jadval.append((previous_end_time, '24:00'))

    return jadval


d = [
    ('8:00', '10:00'),
    ('14:00', '15:00'),
    ('15:30', '15:55'),
    ('17:00', '17:30')
]

jadval = chek_time(d)

for start_time, end_time in jadval:
    print(f"{start_time} - {end_time}")
