for j in range(0, epoch):
		print("epoch", j)
			for i in range(0, fitur.shape[0]):

	actual = hipertensi [i]
	instance = fitur[i]
	
	x0 = instance[0]
	x1 = instance[1]

	sum_unit = x0 * w[0] + x1 * w[1]
	
	if sum_unit > treshold:
		fire = 1
	else:
		fire = 0

	deltane = actual - fire

	w[0] = w[0] + delta * lr
	w[1] = w[1] + delta * lr

	print("y diinginkan :", actual, " y sbenernya", fire, " (error:", deltane, ")" " w1 baru :", w[0], "w2 baru :", w[1])