import sqlalchemy
import matplotlib.pyplot as pyplot
import numpy as np

def plot_delay_airline():
    query = sqlalchemy.text(
        'SELECT a.AIRLINE AS airline, AVG(f.DEPARTURE_DELAY) AS avg_delay '
        'FROM flights AS f '
        'JOIN airlines AS a ON f.AIRLINE = a.ID '
        'WHERE f.DEPARTURE_DELAY IS NOT NULL '
        'GROUP BY a.AIRLINE '
        'HAVING avg_delay > 0'
    )

    engine = sqlalchemy.create_engine('sqlite:///data/data.sqlite3')
    with engine.connect() as connection:
        results = connection.execute(query).mappings().all()

    airlines = []
    avg_delays = []
    for row in results:
        airlines.append(row['airline'])
        avg_delays.append(row['avg_delay'])

    x_pos = np.arange(len(airlines))
    pyplot.bar(x_pos, avg_delays, align='center')
    pyplot.xticks(x_pos, airlines, rotation=45, ha='right')
    pyplot.ylabel('Average Departure Delay (min)')
    pyplot.title('Average Departure Delay by Airline')
    pyplot.tight_layout()
    pyplot.show()

plot_delay_airline()