#---------------------------------------------------------------
# CNM25 PiP Capacitor PCell for extraction
#---------------------------------------------------------------

from ui import *

def dpantenna_ex(cv, ptlist=[[0,0],[1000,0],[1000,1000],[0,1000]]) :
	lib = cv.lib()
	dbu = float(lib.dbuPerUU())
	npts = len(ptlist)

	# Calculate total area an perimeter for arbitrary Manhattan shapes
	asum = 0.0
	perimeter = 0.0
	i = npts-1
	j = 0
	while (j < npts) :
		dx  = float(ptlist[i][0]) / dbu
		dy  = float(ptlist[i][1]) / dbu
		dx1 = float(ptlist[j][0]) / dbu
		dy1 = float(ptlist[j][1]) / dbu
		# compute perimeter
		perimeter = perimeter + ((dx1 - dx) * (dx1 - dx) + (dy1 - dy) * (dy1 - dy))**0.5
		# compute area
		asum = asum + (dx + dx1) * (dy1 - dy)

		# increment vertex
		i = j
		j = j + 1
	area = asum / 2.0

	# Derive rectangular w and l properties:
	# area = w*l
	# perimeter = 2*(w+l)
	a = 1.0
	b = -perimeter / 2.0
	c = area
	l = float((-b+(b**2.0-4.0*a*c)**0.5)/(2.0*a))
	w = float(area/l)

	# Update the master pcell property.
	cv.dbAddProp("w", w*1e-6)
	cv.dbAddProp("l", l*1e-6)

	# Create the recognition region shape
	xpts = intarray(npts)
	ypts = intarray(npts)
	for i in range (npts) :
		xpts[i] = ptlist[i][0]
		ypts[i] = ptlist[i][1]
	cv.dbCreatePolygon(xpts, ypts, npts, TECH_Y0_LAYER);

	# Create pins
	top_net = cv.dbCreateNet("A")
	cv.dbCreatePin("A", top_net, DB_PIN_INPUT)
	bot_net = cv.dbCreateNet("C")
	cv.dbCreatePin("C", bot_net, DB_PIN_INPUT)

	# Setting device type to capacitor
	cv.dbAddProp("type", "dio")

	# Set the device modelName property for netlisting
	cv.dbAddProp("modelName", "dpantenna")

	# Set the NLP property for netlisting
	cv.dbAddProp("NLPDeviceFormat", "[@instName] [|A:%] [|C:%] [@modelName] [@w:w=%u] [@l:l=%u] [@m:m=%:m=1]")
	cv.dbAddProp("NLPDeviceFormatCDL", "x[@instName] [|A:%] [|C:%] [@modelName] [@w:w=%u] [@l:l=%u] [@m:m=%:m=1]")

	# Update the bounding box
	cv.update()