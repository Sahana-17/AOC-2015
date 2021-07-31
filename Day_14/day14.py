#Reindeer can only either be flying (always at their top speed) or resting (    not moving at all), and always spend whole seconds in either state.
 
#For example, suppose you have the following Reindeer:
 
#Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
#Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
#After one second, Comet has gone 14 km, while Dancer has gone 16 km. After     ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the ele    venth second, Comet begins resting (staying at 140 km), and Dancer continues     on for a total distance of 176 km. On the 12th second, both reindeer are re    sting. They continue to rest until the 138th second, when Comet flies for an    other ten seconds. On the 174th second, Dancer flies for another 11 seconds.
 
#In this example, after the 1000th second, both reindeer are resting, and Co    met is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that p    oint). So, in this situation, Comet would win (if the race ended at 1000 sec    onds).

c_dist = 0
total = 0
i = 1

comet = [0] *1000

while total <= 1000:
	if i <= 10:
		i = i + 1
		total = total +1
		c_dist = c_dist + 14
		comet[total] = c_dist
		print(comet[total])
	else:
		total = total + 127
		for x in range(0
		i = 1
		comet[total] = c_dist
		print(comet[total])
print("Dist : ", c_dist)

