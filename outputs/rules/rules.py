def findDecision(obj): #obj[0]: sepallength, obj[1]: sepalwidth, obj[2]: petallength, obj[3]: petalwidth
	# {"feature": "petallength", "instances": 150, "metric_value": 1.585, "depth": 1}
	if obj[2]>2.000137483261145:
		# {"feature": "petalwidth", "instances": 100, "metric_value": 1.0, "depth": 2}
		if obj[3]<=1.7:
			# {"feature": "sepallength", "instances": 54, "metric_value": 0.4451, "depth": 3}
			if obj[0]<=7.036246710058401:
				# {"feature": "sepalwidth", "instances": 53, "metric_value": 0.386, "depth": 4}
				if obj[1]<=2.8:
					return 'Iris-versicolor'
				elif obj[1]>2.8:
					return 'Iris-versicolor'
				else: return 'Iris-versicolor'
			elif obj[0]>7.036246710058401:
				return 'Iris-virginica'
			else: return 'Iris-virginica'
		elif obj[3]>1.7:
			# {"feature": "sepallength", "instances": 46, "metric_value": 0.1511, "depth": 3}
			if obj[0]>5.9:
				return 'Iris-virginica'
			elif obj[0]<=5.9:
				# {"feature": "sepalwidth", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[1]<=3.0:
					return 'Iris-virginica'
				elif obj[1]>3.0:
					return 'Iris-versicolor'
				else: return 'Iris-versicolor'
			else: return 'Iris-virginica'
		else: return 'Iris-virginica'
	elif obj[2]<=2.000137483261145:
		return 'Iris-setosa'
	else: return 'Iris-setosa'
