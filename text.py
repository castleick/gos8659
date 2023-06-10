import sympy

s = sympy.symbols('s')
G = 100 / ((s + 2) * (s + 3))

H = 1  # 피드백 경로의 전달함수

closed_loop_tf = G * H

closed_loop_tf.simplify()
