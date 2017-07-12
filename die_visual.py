from die import Die
import pygal

# Create a D6 (six-sided die)
die = Die()

# Make a few rolls and store results in a list.
results = []	
results = [die.roll() for roll_num in range(1000)]

# Analyze frequencies of numbers
frequencies = []
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 (six-sided die) 1000 times"
hist.x_labels = [str(value) for value in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

