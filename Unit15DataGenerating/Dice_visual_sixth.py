import pygal


from dieSixth import Die
die=Die()
"""骰它几次"""
results=[]
for roll_num in range(1000):
    results.append(die.roll())


#分析结果
frequencies=[]
for value in range(1,die.num_sides+1):#range不包括结束值
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist=pygal.Bar()

hist.title="results of rolling one D6 1000 times "
hist.x_labels=['1','2','3','4','5','6']
hist._x_title='result'
hist._y_title='Frequency of Result'
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')

