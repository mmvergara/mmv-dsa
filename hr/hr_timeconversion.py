def timeConversion(s):
	hour_conversion = {
	"01": 13,
	"02": 14,
	"03": 15,
	"04": 16,
	"05": 17,
	"06": 18,
	"07": 19,
	"08": 20,
	"09": 21,
	"10": 22,
	"11": 23,
	"12": 12,
	}

	arr = s.split(":")
	h = arr[0]
	minutes = arr[1]
	sec = arr[2][:2]
	m = arr[2][2:]
	
	if m == "AM":
		h = f"{abs(int(h) - 12)}"
		if 1 == len(h):
			h = "0"+h
	elif m == "PM":
		h = hour_conversion[h]
	print(f"{h}:{minutes}:{sec}")
	return f"{h}:{minutes}:{sec}"

timeConversion("04:59:59AM")

