from datetime import datetime, timedelta, time


class Train:
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        expected_time = datetime.strptime(expected_time, '%H:%M')
        expected_time = time(expected_time.hour, expected_time.minute)
        expected_time = expected_time.strftime('%H:%M')
        self.expected_time = expected_time


def manage_delays(t, destination, delay):
    if destination in t.destinations:
        temp = datetime.strptime(t.expected_time, '%H:%M')
        dt = datetime.combine(datetime.today(), time(temp.hour, temp.minute)) + timedelta(minutes=delay)
        t.expected_time = time(dt.hour, dt.minute).strftime('%H:%M')


def main():
    trains = [Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
              Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
              Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")]
    for t in trains:
        manage_delays(t, "Lakeside Valley", 60)

    # Validate Test Cases
    assert trains[0].expected_time == "13:04"
    assert trains[1].expected_time == "14:20"
    assert trains[2].expected_time == "14:22"


if __name__ == '__main__':
    main()
