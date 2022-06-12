def combine(arr):
	def helper(cut):
		val = cut[0]
		new_cut = cut[1:]
		if len(cut) > 1:
			cur_repl = helper(new_cut)
			new_arr = []
			for i in val:
				for j in cur_repl:
					new_arr.append(f"{i}{j}")
			return new_arr
		else:
			return val
	
	all_variants = helper(arr)
	return all_variants
