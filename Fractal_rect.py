from graphics import *

window = GraphWin('Fractal rectangle', 1000, 1000)
alpha = 0.05

def fractal_rectangle(A, B, C, D, depth=50):
	if depth < 1:
		return
	for M, N in (A, B), (B, C), (C, D), (D, A):
		Line(Point(*M), Point(*N)).draw(window)

	A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
	B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
	C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
	D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
	fractal_rectangle(A1, B1, C1, D1, depth-1)
	message = Text(Point(window.getWidth()/2, 30), 'Click on three points')
	message.setTextColor('red')
	message.setStyle('italic')
	message.setSize(20)
	message.draw(window)
	message.setText('Click on mouse to exit...')
	window.getMouse()
	window.close()

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))




	#gr.Line(gr.Point(*A), gr.Point(*B).draw(window)  Разворачивание списка/кортежа *A = A[0], A[1], т.к. каждой точке соответствует пара координат
	#gr.Line(gr.Point(*B), gr.Point(*C).draw(window)
	#gr.Line(gr.Point(*C), gr.Point(*D).draw(window)
	#gr.Line(gr.Point(*D), gr.Point(*A).draw(window)
	